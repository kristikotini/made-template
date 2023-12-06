from unittest.mock import patch

import pandas as pd
import pytest
from pandas._testing import assert_frame_equal

from dataframe_service import DataFrameService
from tests.test_data.test_data_dataframe_service import REPLACE_TEST_CASES, COLUMNS_TO_STR_TEST_CASES
from tests.utils import ParameterizationStruct


@pytest.mark.parametrize('test_case', REPLACE_TEST_CASES)
def test_replace(test_case: ParameterizationStruct):
    # Arrange
    service = DataFrameService()

    # Act
    df = test_case.input['df']
    DataFrameService.replace(**test_case.input)

    # Assert
    assert_frame_equal(df, test_case.output)


@pytest.mark.parametrize('test_case', COLUMNS_TO_STR_TEST_CASES)
def test_columns_to_str(test_case: ParameterizationStruct):
    # Arrange
    service = DataFrameService()

    # Act
    df = test_case.input['df']
    DataFrameService.columns_to_str(**test_case.input)

    # Assert
    assert_frame_equal(df, test_case.output)


@patch('dataframe_service.DataFrameService.df_to_pickle')
def test_df_to_pickle(mocked_to_pickle):
    # Arrange
    service = DataFrameService()

    # Act
    df = pd.DataFrame({
        'A': [1.0, 10.1, 2.0, 4.5, 0.0, -1.5, 0],
        'B': [1, 2, 3, 4, 5, 6, 7],
    })
    path = 'dummy/testpath/dummy_data.csv'
    DataFrameService.df_to_pickle(
        df=df, file_path=path
    )

    # Assert
    mocked_to_pickle.assert_called_once_with(df=df, file_path=path)
