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
    """Test the associated tag when a single node is added"""
    # Create a blank tree
    t = rooted_tree()
    # Add a single node to the tree 
    t = add_metric_namespace_to_tree(["A"],t)
    n = t.get_node("root.A")
    assert n.tag == "A"


def test_single_node_id():
    """Test the identifiers are created correctly for a node."""
    t = rooted_tree()
    t = add_metric_namespace_to_tree(["A"],t)
    n = t.get_node("root.A")
    assert n.identifier == "root.A"


def test_single_parent():
    t = rooted_tree()
    t = add_metric_namespace_to_tree(["A"],t)
    assert t.parent("root.A").tag == "root"


def test_single_child(): 
    """Testing tree creation works with one ID provided"""
    t = rooted_tree()
    t = add_metric_namespace_to_tree(["A"], t) 
    # Check that the first child's id is "root.A"
    assert t.children("root")[0].identifier == "root.A"


def test_two_root_children(): 
    """Testing multiple children can point to the root"""
    t = rooted_tree() 
    t = add_metric_namespace_to_tree(["A"], t)
    t = add_metric_namespace_to_tree(["B"], t) 

    assert t.children("root")[0].identifier == "root.A"
    assert t.children("root")[1].identifier == "root.B"


def test_nested_identifier():
    """Testing nested identifier creation"""
    t = rooted_tree() 
    t = add_metric_namespace_to_tree(["A","B"], t)
    
    assert t.get_node("root.A.B").identifier == "root.A.B"


def test_nesting_child_identifier():
    """Test that a nested child inherits the parent ID"""
    t = rooted_tree()
    t = add_metric_namespace_to_tree(["A","B"],t)

    # Check that B is a child of A
    assert t.children("root.A")[0].identifier == "root.A.B"


def test_nested_children():
    """Checking that nodes will nest correctly, passing in an A --> B 
    and A --> sequence."""
    t = rooted_tree()
    t = add_metric_namespace_to_tree(["A","B"],t)
    t = add_metric_namespace_to_tree(["A","C"],t)

    assert len(t.children("root.A")) == 2 
    assert t.children("root.A")[0].identifier == "root.A.B"
    assert t.children("root.A")[1].identifier == "root.A.C"


def test_unique_id_multiple_tags():
    """Testing that multiple tags will show up correctly without an ID conflict.
    Testing to see if """
    t = rooted_tree()

    # Create the first sequenc
    t = add_metric_namespace_to_tree(["request1","latency"],t)
    t = add_metric_namespace_to_tree(["request2","latency"],t)

    assert t.get_node("root.request1.latency").tag == "latency"
    assert t.get_node("root.request2.latency").tag == "latency"

def test_add_order_insensitivity(): 
    """Checking that the function isn't sensitive to add order. i.e. adding the following:
        1. root --> request1 --> latency
        2. root --> mongo --> hits
        2. root --> request1 --> errors
        
        doesn't cause a problem.
        """
    t = rooted_tree()

    t = add_metric_namespace_to_tree(["request1","latency"],t)
    t = add_metric_namespace_to_tree(["mongo","hits"])
    t = add_metric_namespace_to_tree(["request1","errors"])

    children = t.children("root.request1")

    assert [node.tag for node in children] == ["latency","errors"]
