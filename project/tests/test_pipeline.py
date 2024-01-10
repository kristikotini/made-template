from unittest.mock import patch

import numpy as np

from project.pipeline import Pipeline
from project.tests.utils import validate_column_choices, PLACE_NAMES, STATE_NAMES, SEVERITY_NAMES


@patch('project.dataframe_service.DataFrameService.df_to_pickle')
def test_pipeline_run_successfully(mocked_to_pickle):
    # Arrange
    pipeline = Pipeline()
    # Act
    pipeline.execute_pipeline()
    # Assert
    assert mocked_to_pickle.call_count == 2


def test_create_traffic_accident_df():
    # Arrange
    pipeline = Pipeline()
    # Act
    df = pipeline.create_traffic_accident_df()
    # Assert
    assert len(df.columns) == 26

    assert validate_column_choices(df, 'state', STATE_NAMES)
    assert validate_column_choices(df, 'place', PLACE_NAMES)
    assert validate_column_choices(df, 'severity', SEVERITY_NAMES)

    # all traffic values for each year are of type int
    column_types = df.iloc[:, 3:-2].dtypes
    assert all(np.issubdtype(dtype, np.integer) for dtype in column_types)


def test_create_weather_df():
    # Arrange
    pipeline = Pipeline()
    # Act
    df = pipeline.create_weather_df()
    # Assert
    assert len(df.columns) == 25
    assert validate_column_choices(df, 'state', STATE_NAMES)

    # all traffic values for each year are of type int
    column_types = df.iloc[:, 1:].dtypes
    assert all(np.issubdtype(dtype, np.floating) for dtype in column_types)
