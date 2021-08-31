from src.monthly.ingestor import MonthlyDataLoader
from tqdm import tqdm

# Necessary variables.
DATA_DIR = 'data'
feature_file = 'merged_data_eom.csv'
response_file = 'excess_return_data_eom.csv'

# Feature datasets.
data = MonthlyDataLoader(feature_file, response_file, DATA_DIR)
X = data.feature_space_df
y = data.response_df

print(X.shape, y.shape)

for row in tqdm(range(100000)):
    ...
