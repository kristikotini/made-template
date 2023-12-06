import pandas as pd

from project.custom_types import ProcessorReplaceConfig

ALL_COLUMNS = 'replace_on_all_columns'


class DataFrameService:

    @classmethod
    def df_to_pickle(cls, df: pd.DataFrame, file_path: str):
        print('Saving transformed data in pickle...')
        df.to_pickle(file_path)
        print('Saving finished')

    @classmethod
    def columns_to_str(cls, df: pd.DataFrame, column_names: list[str]) -> pd.DataFrame:
        df[column_names] = df[column_names].astype(str)
        return df

    @classmethod
    def replace(cls, df: pd.DataFrame, fields: list[ProcessorReplaceConfig]):
        for field in fields:
            if field['column_name'] == ALL_COLUMNS:
                df.replace({**field['values']}, inplace=True)
            else:
                df[field['column_name']].replace({**field['values']}, inplace=True)
