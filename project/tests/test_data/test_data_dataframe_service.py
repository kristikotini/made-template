import numpy as np
import pandas as pd

import os

# Get and print the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

from project.dataframe_service import ALL_COLUMNS
from project.tests.utils import ParameterizationStruct

REPLACE_TEST_CASES: list[ParameterizationStruct] = [
    ParameterizationStruct(
        description="Case 0: Normal behavior",
        input={
            'df': pd.DataFrame({
                'A': [100, 200, np.nan, '', None],
                'B': [100, 200, 0, 0, 0],
                'C': ['foo', 'foo', 'foo', 'foo', 'foo'],
            }),
            'fields': [
                {
                    'column_name': 'A',
                    'values': {np.nan: 0, None: 0, '': 0}
                },
                {
                    'column_name': ALL_COLUMNS,
                    'values': {0: 123}
                },
                {
                    'column_name': 'C',
                    'values': {'foo': 'bar'}
                }
            ],
        },
        output=pd.DataFrame(
            {
                'A': [100, 200, 123, 123, 123],
                'B': [100, 200, 123, 123, 123],
                'C': ['bar', 'bar', 'bar', 'bar', 'bar'],
            })
    ),
]

COLUMNS_TO_STR_TEST_CASES: list[ParameterizationStruct] = [
    ParameterizationStruct(
        description="Case 0: Normal behavior",
        input={
            'df': pd.DataFrame({
                'A': [1.0, 10.1, 2.0, 4.5, 0.0, -1.5, 0],
                'B': [1, 2, 3, 4, 5, 6, 7],
            }),
            'column_names': ['A'],
        },
        output=pd.DataFrame(
            {
                'A': ['1.0', '10.1', '2.0', '4.5', '0.0', '-1.5', '0.0'],
                'B': [1, 2, 3, 4, 5, 6, 7],
            })
    )
]
