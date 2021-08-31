import pandas as pd


# Instantiate MonthlyDataLoader Class.
class MonthlyDataLoader:
    def __init__(self, feature_filename, response_filename, data_dir):
        self.feature_space_df = pd.read_csv('{}/{}'.format(data_dir, feature_filename))
        self.response_df = pd.read_csv('{}/{}'.format(data_dir, response_filename))
