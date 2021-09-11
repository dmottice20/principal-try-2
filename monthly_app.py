from src.monthly.ingestor import Ingestor
from src.monthly.dnn import DeepNeuralNetwork
from tqdm import tqdm

# Necessary variables.
DATA_DIR = 'data'
raw_feature_file = 'newFred.csv'
raw_response_file = 'raw_returns.csv'
trans_feature_file = 'transformed_features.csv'
tran_response_file = 'transformed_responses.csv'

# Load raw feature datasets.
ing = Ingestor(trans_feature_file, tran_response_file, DATA_DIR, is_transformed=True)
ing.transform()
# ing.save_transformations()

# sw = D(feature_data=ing.feature_space_df, response_data=ing.response_df, size_of_train=12)
dnn = DeepNeuralNetwork(ing.feature_space_df, ing.response_df)
dnn.train()
