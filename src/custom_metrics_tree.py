from treelib import Tree
import pandas as pd


def update_usage_data(t:Tree,node_id:str,usage:int=0) -> Tree:
    """Add the usage data for that custom metrtic to itself and walk through the ancestors adding to it"""
    t.get_node(node_id).data = usage
    # Initialize with the first ancestor ID and walk up the tree
    ancestor_id = t.ancestor(node_id)
    while ancestor_id is not None:
        t.get_node(ancestor_id).data += usage
        # Update the ancestor ID
        ancestor_id = t.ancestor(ancestor_id)
    return t


def add_metric_namespace_to_tree(metric_list:list, tree:Tree, data:int=0) -> Tree:
    parent="root"
    for element in metric_list:
        node_id = parent + "." + element
        # Check if the element exists in the parent's subtree
        # If it does skip, o.w. add to the tree
        if not tree.subtree(parent).get_node(node_id):
            # Initialize a new node with usage data = 0
            tree.create_node(element, node_id, parent=parent,data=0)
        # Update the parent ID
        parent = node_id
    # On the last node_id update the ancestor_id
    tree = update_usage_data(tree, node_id, data)
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
    df['metric_name'] = df['metric_name'].astype(pd.StringDtype())
    return df


def generate_cm_namespace_tree(cm_df:pd.DataFrame) -> Tree: 
    cm_tree = Tree()
    cm_tree.create_node("root","root",data=0)
    for iter, row in cm_df.iterrows():
        custom_metric = row.metric_name
        usage_data  = row.average_hourly_custom_metrics
        metric_namespace = custom_metric.split(".")
        cm_tree = add_metric_namespace_to_tree(metric_namespace,cm_tree, usage_data)
    return cm_tree