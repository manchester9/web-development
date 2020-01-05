from pandas_datareader import data as pdr
import datetime
import numpy as np
import sklearn as sk 

start_date = datetime.datetime(2019, 9, 10)
end_date = datetime.datetime(2019, 10, 1)
tickers = ['GOOG', 'AAPL']

def extract_data(tickers, start_date, end_date):
    df = pdr.get_data_yahoo(tickers, start_date, end_date)
    return df  

extract_data(tickers, start_date, end_date)


