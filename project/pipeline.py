from collections import defaultdict

import pandas as pd


class Pipeline:
    traffic_accident_data = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46241-0024_00.csv"
    weather_data_dir = "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation"

    def execute_pipeline(self):
        print('------Pipeline started------')
        self.create_traffic_accident_data_csv_file()
        self.create_weather_data_csv_file()
        print('------Pipeline finished------')

    def create_traffic_accident_data_csv_file(self):
        print('Loading traffic data from remote...')
        df = pd.read_csv(
            self.traffic_accident_data,
            delimiter=";",
            encoding="latin",
            skiprows=4,
            skipfooter=3,
        )
        print('Data loaded')

        months_list = self._get_months_for_traffic_data(df)
        new_header = ["state", "place", "severity"] + months_list

        new_header = [el.lower() for el in new_header]
        df = df[2:]
        df.columns = new_header
        df.drop(df.columns[-1], axis=1, inplace=True)
        df.iloc[:, 3:] = df.iloc[:, 3:].replace({'-': 0})
        str_columns = ["state", "place", "severity"]

        df[str_columns] = df[str_columns].astype(str)
        df[months_list[:-1]] = df[months_list[:-1]].astype(int)
        df = self._get_translated_traffic_data(df)
        print('Saving transformed data in csv...')
        df.to_csv('data/traffic_accident.csv', sep=';', index=False)
        print('Saving finished')

    def create_weather_data_csv_file(self):
        states_info = {
            'Brandenburg/Berlin': 'Berlin',  #
            'Brandenburg': 'Brandenburg',
            'Baden-Wuerttemberg': 'Baden-Württemberg',  #
            'Bayern': 'Bayern',  #
            'Hessen': 'Hessen',
            'Mecklenburg-Vorpommern': 'Mecklenburg-Vorpommern',
            'Niedersachsen': 'Niedersachsen',
            'Niedersachsen/Hamburg/Bremen': ['Bremen', 'Hamburg'],
            'Nordrhein-Westfalen': 'Nordrhein-Westfalen',
            'Rheinland-Pfalz': 'Rheinland-Pfalz',
            'Schleswig-Holstein': 'Schleswig-Holstein',
            'Saarland': 'Saarland',
            'Sachsen': 'Sachsen',
            'Sachsen-Anhalt': 'Sachsen-Anhalt',
            'Thueringen/Sachsen-Anhalt': None,
            'Thueringen': 'Thüringen',
        }
        data = defaultdict(dict)
        print('Creating rain data from remote...')
        for month in range(1, 13):
            if month < 10:
                filename = f'regional_averages_rr_{0}{month}.txt'
            else:
                filename = f'regional_averages_rr_{month}.txt'
            df = pd.read_csv(
                f'{self.weather_data_dir}/{filename}',
                delimiter=';',
                skiprows=1,
                encoding='latin',
            )
            df.drop(df.columns[-2:], axis=1, inplace=True)
            df = df[df['Jahr'].isin([2021, 2022])]
            for state, translation in states_info.items():
                if type(translation) is str:
                    df.rename(columns={state: translation}, inplace=True)

                elif type(translation) is list:
                    for el in translation:
                        df[el] = df[state]
                    df.drop(state, axis=1, inplace=True)

                elif translation is None:
                    df.drop(state, axis=1, inplace=True)
            df['date'] = '1-' + df['Monat'].astype(str) + '-' + df['Jahr'].astype(str)
            df.drop(['Jahr', 'Monat'], axis=1, inplace=True)

            for row_dict in df.to_dict(orient='records'):
                prec_date = row_dict.pop('date')
                for state, amount in row_dict.items():
                    data[state][prec_date] = amount
        print('Data constructed')

        rain_prec_df = self._construct_rain_prec_df(data)
        print('Saving transformed data in csv...')
        rain_prec_df.to_csv('data/precipitation.csv', sep=';', index=False)
        print('Saving finished')

    @staticmethod
    def _get_months_for_traffic_data(df) -> list[str]:
        years = df.iloc[0, 3:].values.tolist()
        months = df.iloc[1, 3:].values.tolist()
        year_months_first_line = []

        months_int = {
            'Januar': 1,
            'Februar': 2,
            'März': 3,
            'April': 4,
            'Mai': 5,
            'Juni': 6,
            'Juli': 7,
            'August': 8,
            'September': 9,
            'Oktober': 10,
            'November': 11,
            'Dezember': 12,
        }

        for year, month in zip(years, months):
            month_year_str = f"1-{months_int[month]}-{year}"
            year_months_first_line.append(month_year_str)

        return year_months_first_line

    @staticmethod
    def _get_translated_traffic_data(df):
        place_translation = {
            'innerorts': 'inner town',
            'außerorts (ohne Autobahnen)': 'out of town (without motorways)',
            'auf Autobahnen': 'on highways',
            'Insgesamt': 'In total',
        }
        severity_translation = {
            'Getötete': 'Killed',
            'Leichtverletzte': 'Slightly injured',
            'Schwerverletzte': 'Seriously injured',
            'Insgesamt': 'In total',
        }

        df['place'] = df['place'].replace(place_translation)
        df['severity'] = df['severity'].replace(severity_translation)
        return df

    @staticmethod
    def _construct_rain_prec_df(data: dict):
        dates = []
        for year in ['2021', '2022']:
            for month in range(1, 13):
                dates.append(f'1-{month}-{year}')

        columns = ['state'] + dates
        empty_df = pd.DataFrame(columns=columns)

        # Append new rows in a loop
        for state, value in data.items():
            new_row = {'state': state}
            for year, rain in value.items():
                new_row[year] = rain
            empty_df = empty_df.append(new_row, ignore_index=True)
        return empty_df.drop(columns=['1-12-2022'])


if __name__ == "__main__":
    p = Pipeline()
    p.execute_pipeline()