import pandas as pd


# Instantiate MonthlyDataLoader Class.
class Ingestor:
    def __init__(self, feature_filename, response_filename, data_dir, is_transformed):
        if not is_transformed:
            self.feature_space_df = None
            self.response_df = None
            self.raw_feature_space_df = pd.read_csv('{}/{}'.format(data_dir, feature_filename))
            self.raw_response_df = pd.read_csv('{}/{}'.format(data_dir, response_filename))
        else:
            self.raw_feature_space_df = pd.read_csv('{}/{}'.format(data_dir, feature_filename))
            self.raw_response_df = pd.read_csv('{}/{}'.format(data_dir, response_filename))

    def transform(self):
        """
        Fx that transforms the data.
        :return: feature_space_df, response_df
        """
        raw_features_df = self.raw_feature_space_df

        # Convert date column from type str to datetime & set as index.
        raw_features_df.DATE = pd.to_datetime(raw_features_df.DATE)
        raw_features_df.set_index('DATE', drop=True, inplace=True)

        # Find first row's index for each column to start running models,
        # this is because most columns are empty until a more recent date.
        # Start at the maximum of these indices.
        first_non_nan = [raw_features_df[col].first_valid_index() for col in raw_features_df.columns]
        print(raw_features_df.shape)
        raw_features_df = raw_features_df.loc[max(first_non_nan):, :]
        print(raw_features_df.shape)
