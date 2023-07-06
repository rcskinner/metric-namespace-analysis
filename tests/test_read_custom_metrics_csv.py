import pytest
import pandas as pd


from src.custom_metrics_tree import read_custom_metrics_csv

data_path = "tests/test_data.csv"

def test_dataframe_type(): 
    test_df = read_custom_metrics_csv(data_path)
    assert type(test_df) == pd.DataFrame

def test_column_names():
    test_df = read_custom_metrics_csv(data_path)
    expected_colnames = ["metric_name","average_hourly_custom_metrics","max_hourly_custom_metrics"]
    assert list(test_df.columns) == expected_colnames

# TODO: Add a Type test