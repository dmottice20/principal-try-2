import pandas as pd
import requests
import csv

# Necessary variables.
DATA_DIR = 'data'
fred_file = 'newFred.csv'

# Read in FRED_data.csv file and look at first & last.
fred = pd.read_csv('{}/{}'.format(DATA_DIR, fred_file))
print('------FIRST ROW-------')
print(fred.head(1))

print('------SECOND ROW-------')
print(fred.head(2))

print('------LAST ROW-------')
print(fred.tail(1))

print('------COLUMN NAMES-------')
print(fred.columns)

print('------SHAPE OF DATA-------')
print(fred.shape)

# Look @ the alphaVantage API and test.
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo'
