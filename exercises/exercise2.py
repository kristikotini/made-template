import sqlite3

import pandas as pd


def write_to_db(df: pd.DataFrame):
    conn = sqlite3.connect('trainstops.sqlite')
    dtypes = {
        'EVA_NR': 'INTEGER',
        'DS100': 'TEXT',
        'IFOPT': 'TEXT',
        'Verkeher': 'TEXT',
        'Laenge': 'REAL',
        'Breite': 'REAL',
        'Betreiber_Name': 'TEXT',
        'Betreiber_Nr': 'INTEGER',
    }
    df.to_sql('trainstops', conn, index=False, if_exists='replace', dtype=dtypes)
    conn.close()


def execute_trainstops_pipeline():
    url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    df = pd.read_csv(url, delimiter=';')
    df.drop(['Status'], axis=1, inplace=True)
    df.dropna(how='any', inplace=True)

    ifopt_pattern = '^[A-Za-z]{2}:\d*:\d*(?::\d*)?$'
    df = df.drop(df[(~df['Verkehr'].isin(['FV', 'RV', 'nur DPN']))].index)

    df['Laenge'] = df['Laenge'].str.replace(',', '.').astype(float)
    df['Breite'] = df['Breite'].str.replace(',', '.').astype(float)
    df = df.drop(df[(~df['Laenge'].between(-90, 90, inclusive=True))].index)
    df = df.drop(df[(~df['Breite'].between(-90, 90, inclusive=True))].index)

    df = df.drop(df[(~df['IFOPT'].str.contains(ifopt_pattern))].index)

    write_to_db(df)


if __name__ == "__main__":
    execute_trainstops_pipeline()
