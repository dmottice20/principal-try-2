from tqdm import tqdm


# Instantiate a SlidingWindow Class...
class SlidingWindow:
    """
    Window class to be used the various models in the time series model
    and use for a train / test / validation split.
    """
    def __init__(self, feature_data, response_data, set_sizes=None, step=12):
        """
        Initialized sliding window class to be used by the
        :param feature_data: data frame of transformed features.
        :param response_data: dataframe of transformed responses
        :param set_sizes: # of months for [train,  test] sets.
        :param step: # of months to move forward between each window.
        """
        if set_sizes is None:
            # Default to training on 48 months, testing on 24, where
            # the validation split will be 0.5 --> 12 for test, 12 for val.
            self.set_sizes = [48, 24]
        else:
            self.set_sizes = set_sizes

        # Create an index tracker to make easy work of converting b/w different structures.
        dates = list(response_data.index.values)
        self.indices_by_date = {}
        for i, date in enumerate(dates):
            self.indices_by_date[i] = date

        self.feature_df = feature_data
        self.response_df = response_data
        self.step = step
        self.schedule = {}

    def create_schedule(self):
        i = 0
        window_location = 0

        # Loop over all entries in data, stepping forward by the step size.
        for window_start in tqdm(range(0, len(self.response_df), self.step), desc='Creating sliding window...'):
            # Split into X_train, X_test, y_train, y_test
            idx = window_start + self.set_sizes[0]
            X_train, X_test = self.feature_df.iloc[window_start:idx], self.feature_df.iloc[idx:idx+self.set_sizes[1]]
            y_train, y_test = self.response_df.iloc[window_start:idx], self.response_df.iloc[idx:idx+self.set_sizes[1]]
            
            # Update schedule w/ these values.
            self.schedule[i] = {
                "X_train": X_train,
                "X_test": X_test,
                "y_train": y_train,
                "y_test": y_test
            }
            
            i += 1

        return self.schedule

    def analyze_schedule(self):
        print("THERE ARE {} WINDOW!".format(len(self.schedule.keys())))
        for k, v in self.schedule.items():
            print("For Window {}".format(k))
            print("X_train is...", v["X_train"].shape)
            print("X_test is...", v["X_test"].shape)
            print("y_train is...", v["y_train"].shape)
            print("y_test is...", v["y_test"].shape)

class RollingWindow:
    """
    Class for rolling windows, where the training set grows over time.
    """
    def __init__(self):
        print("Rolling Window")