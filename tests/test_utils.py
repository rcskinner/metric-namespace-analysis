# Small Utility file holding the test data
import pandas as pd

def raw_test_data():
    # Create the test data suite
    metric_namespaces = [
        "mongo.cache.performance.max",
        "mongo.cache.performance.min",
        "request.route1.latency",
        "request.route2.latency"
    ]
    metric_avg_data = [10,10,10,10]
    metric_max_data = [20,20,20,20]
    data_dict = {
        "Metric Name": metric_namespaces,
        "Average Custom Metrics / Hour": metric_avg_data,
        "Max Custom Metrics / Hour": metric_max_data
                 }
    raw_test_df = pd.DataFrame.from_dict(data_dict)
    return raw_test_df


def processes_test_data():
        # Create the test data suite
    metric_namespaces = [
        "mongo.cache.performance.max",
        "mongo.cache.performance.min",
        "request.route1.latency",
        "request.route2.latency"
    ]
    metric_avg_data = [10,10,10,10]
    metric_max_data = [20,20,20,20]
    data_dict = {
        "metric_name": metric_namespaces,
        "average_hourly_custom_metrics": metric_avg_data,
        "max_hourly_custom_metrics": metric_max_data
                 }
    processed_test_df = pd.DataFrame.from_dict(data_dict)
    return processed_test_df