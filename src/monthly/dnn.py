import pandas as pd
import tensorflow as tf
from tqdm import tqdm
from src.monthly.windows import SlidingWindow
from src.monthly.windows import RollingWindow


class DeepNeuralNetwork:
    """
    Class for a standard Deep Neural Network.
    """
    def __init__(self, feature_data, response_data):
        self.feature_df = feature_data
        self.response_df = response_data

    def train(self, type_of_window='sliding', step=12):
        # Instantiate whatever schedule desired...
        # sliding --> fixed train length and test length
        # rolling --> fixed test while train length grows over time
        if type_of_window == 'sliding':
            window = SlidingWindow(self.feature_df, self.response_df, set_sizes=[48, 24], step=step)
            window.create_schedule()
        else:
            window = RollingWindow()

        # Instantiate model.

        
        # Loop over each window where there is test data.
        for window_num, data in tqdm(window.schedule.keys(), desc="running models"):
            # Fit model.
