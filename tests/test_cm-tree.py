import pytest
from treelib import Tree
from src.custom_metrics_tree import add_metric_namespace_to_tree

from .test_utils import raw_test_data

def rooted_tree():
    # Utility function to create a rooted tree
    t = Tree()
    t.create_node("root","root")
    return t


def test_single_node_tag(): 
    """Test the base tree generation function."""
    # Create a blank tree
    t = Tree()
    t.create_node("root","root")

    # Add a single node to the tree 
    t = add_metric_namespace_to_tree(["A"],t)
    assert t.tag == "A"

    