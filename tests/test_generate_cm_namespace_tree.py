import pytest 

from src.custom_metrics_tree import (
    generate_cm_namespace_tree, 
    read_custom_metrics_csv
)

data_file = "tests/test_data.csv"


def test_average_hourly_generation():
    """Testing generating a tree with the default
    column (average_hourly_custom_metrics) and to check if
    the weights are updating appropriately"""
    cm_df = read_custom_metrics_csv(data_file)
    cm_tree = generate_cm_namespace_tree(cm_df)
    n = cm_tree.get_node("root")
    assert n.data == 40

def test_max_hourly_generation():
    """Testing generating the custom metrics tree
    with the second provided column (max_hourly_custom_metrics)
    and to check if the weights are updating appropriately"""
    cm_df = read_custom_metrics_csv(data_file)
    cm_tree = generate_cm_namespace_tree(cm_df,"max_hourly_custom_metrics")
    n = cm_tree.get_node("root")
    assert n.data == 80

