import pandas as pd

# Read in data.
DATA_DIR = 'final'
data = pd.read_excel('{}/list_eval_partition.xlsx'.format(DATA_DIR), header=None)
data.columns = ['img', 'type']
print(data.shape)
print(data.columns)

# Seperate into 
