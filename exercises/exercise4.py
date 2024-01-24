import io
import sqlite3
import zipfile
from urllib.request import urlretrieve

import numpy as np
import pandas as pd


def write_to_db(df: pd.DataFrame):
    conn = sqlite3.connect('temperatures.sqlite')
    dtypes = {
        'Geraet': 'INTEGER',
        'Hersteller': 'TEXT',
        'Model': 'TEXT',
        'Monat': 'INTEGER',
        'Temperatur': 'REAL',
        'Batterietemperatur': 'REAL',
        'Geraet aktiv': 'TEXT',
    }
    df.to_sql('temperatures', conn, index=False, if_exists='replace', dtype=dtypes)
    conn.close()


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    # add the header
    df.columns = df.iloc[0]
    df = df[1:]

    columns_to_use = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)",
                      "Batterietemperatur in °C", "Geraet aktiv"]

    # Remove all columns to the right of 'Geraet aktiv'
    column_index_bool_mask = df.columns.get_loc('Geraet aktiv')
    first_occ_geraet_index = np.argmax(column_index_bool_mask)
    df = df.iloc[:, :first_occ_geraet_index + 1]
    df = df[columns_to_use]

    df = df.rename(columns={
        "Temperatur in °C (DWD)": "Temperatur",
        "Batterietemperatur in °C": "Batterietemperatur",
    })

    # Change the dtypes from str to their correct type
    df['Geraet'] = df['Geraet'].astype(int)
    df['Monat'] = df['Monat'].astype(int)
    df['Temperatur'] = df['Temperatur'].str.replace(',', '.').astype(float)
    df['Batterietemperatur'] = df['Batterietemperatur'].str.replace(',', '.').astype(float)

    # Transform temperatures in Celsius to Fahrenheit
    for column in ['Temperatur', 'Batterietemperatur']:
        df[column] = (df[column] * 9 / 5) + 32

    return df


def download_and_unzip_data(zip_url):
    zip_file, _ = urlretrieve(zip_url)
    with zipfile.ZipFile(zip_file) as zip_ref:
        zip_content = {
            name: zip_ref.read(name) for name in zip_ref.namelist()
        }

    if data := zip_content.get("data.csv"):
        data_b = io.BytesIO(data)
        df = pd.read_csv(
            data_b,
            delimiter=";",
            usecols=range(0, 14),
            lineterminator='\n',
            header=None
        )

        return df
    else:
        raise Exception('Error: data.csv not found in the ZIP file')


def execute_battery_temperatures_pipeline():
    url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"

    data = download_and_unzip_data(url)
    df = process_data(data)

    write_to_db(df)


if __name__ == "__main__":
    execute_battery_temperatures_pipeline()
