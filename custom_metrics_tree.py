from treelib import Tree
import pandas as pd


def add_metric_namespace_to_tree(metric_list:list, tree:Tree) -> Tree:
    """Given a split list of a metrics namespace, add the """
    parent="root"
    for element in metric_list:
        node_id = parent + "." + element
        # Check if the element exists in the parent's subtree
        # If it does skip, o.w. add to the tree
        if not tree.subtree(parent).get_node(node_id):
            tree.create_node(element, node_id, parent=parent)
        parent = node_id
    return tree


def read_custom_metrics_csv(fn:str) -> pd.DataFrame():
    """
    Purpose: Read in the custom metrics .csv file and make 
    small transformations to it. 
    
    Input Args: 
        - fn(str): The filepath to the .csv
    Output: 
        - pd.DataFrame: Transformed custom metrics data
    """
    df = pd.read_csv(fn)
    df = df.rename(columns={
        "Metric Name":"metric_name",
        "Average Custom Metrics / Hour": "average_hourly_custom_metrics",
        "Max Custom Metrics / Hour": "max_hourly_custom_metrics"
        })
    return df


def generate_cm_namespace_tree(cm_df:pd.DataFrame) -> Tree: 
    cm_tree = Tree()
    cm_tree.create_node("root","root")
    for iter, row in cm_df.iterrows():
        custom_metric = row.metric_name
        metric_namespace = custom_metric.split(".")
        cm_tree = add_metric_namespace_to_tree(metric_namespace,cm_tree)
    return cm_tree