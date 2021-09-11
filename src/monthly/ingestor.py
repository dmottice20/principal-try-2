import pandas as pd
import os


# Instantiate MonthlyDataLoader Class.
class Ingestor:
    def __init__(self, feature_filename, response_filename, data_dir, is_transformed):
        self.is_transformed = is_transformed
        if not self.is_transformed:
            self.feature_space_df = None
            self.response_df = None
            self.raw_feature_space_df = pd.read_csv('{}/{}'.format(data_dir, feature_filename))
            self.raw_response_df = pd.read_csv('{}/{}'.format(data_dir, response_filename))
        else:
            self.feature_space_df = pd.read_csv('{}/{}/{}'.format(data_dir, 'transformed', feature_filename))
            self.response_df = pd.read_csv('{}/{}/{}'.format(data_dir, 'transformed', response_filename))

            # Convert date columns to datetime indices and set as index.
            self.feature_space_df.DATE = pd.to_datetime(self.feature_space_df.DATE)
            self.feature_space_df.set_index('DATE', drop=True, inplace=True)
            self.response_df.Date = pd.to_datetime(self.response_df.Date)
            self.response_df.set_index('Date', drop=True, inplace=True)

    def transform(self):
        """
        Fx that transforms the data.
        :return: feature_space_df, response_df
        """
        if not self.is_transformed:
            raw_features_df = self.raw_feature_space_df
            raw_responses_df = self.raw_response_df

            # Convert date column from type str to datetime & set as index.
            raw_features_df.DATE = pd.to_datetime(raw_features_df.DATE)
            raw_features_df.set_index('DATE', drop=True, inplace=True)

            # Find first row's index for each column to start running models,
            # this is because most columns are empty until a more recent date.
            # Start at the maximum of these indices.
            first_non_nan = [raw_features_df[col].first_valid_index() for col in raw_features_df.columns]
            raw_features_df = raw_features_df.loc[max(first_non_nan):, :]

            # TARGET TRANSFORMATIONS
            # Convert date column from type str to datetime
            raw_responses_df.Date = pd.to_datetime(raw_responses_df.Date)

            # Transform EOM date to BOM w/ the assumption that the closing price of the month
            # before is the opening price of the month currently. The returns data starts back
            # at March 1887 and goes until July 2021.
            new_index = pd.date_range(start=pd.to_datetime('3/01/87'),
                                      end=pd.to_datetime('7/01/21'), freq=pd.offsets.MonthBegin(1))
            raw_responses_df['Date'] = new_index
            raw_responses_df.set_index('Date', drop=True, inplace=True)
            raw_responses_df = raw_responses_df.loc[max(first_non_nan):, :]

            # Convert all columns in raw_responses_df from type str to floats.
            def convert_string_pct_to_float(x):
                return float(x.split('%')[0])
            # 1) Loop over all columns.
            for col in raw_responses_df.columns:
                # 2) apply above transformation.
                raw_responses_df[col] = raw_responses_df[col].apply(convert_string_pct_to_float)

            # Update class attributes.
            self.feature_space_df = raw_features_df
            self.response_df = raw_responses_df
        else:
            print("DATA IS ALREADY TRANSFORMED!")

    def save_transformations(self):
        """
        Fx that saves transformed dataframes to .csv files
        :return:
        """
        os.system('mkdir data/transformed/')
        self.feature_space_df.to_csv('data/transformed/transformed_features.csv')
        self.response_df.to_csv('data/transformed/transformed_responses.csv')
