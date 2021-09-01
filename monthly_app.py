from src.monthly.ingestor import Ingestor
from tqdm import tqdm

# Necessary variables.
DATA_DIR = 'data'
raw_feature_file = 'newFred.csv'
raw_response_file = 'excess_return_data_eom.csv'

# Load raw feature datasets.
ing = Ingestor(raw_feature_file, raw_response_file, DATA_DIR, is_transformed=False)
ing.transform()
