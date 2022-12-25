import pandas as pd
import pandas_datareader as web

def get_price_csv(folder_name, symbol, index_col):
    """ 
    Get 'Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split Ratio',
       'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume'
       
    Parameters
    --------------------------------
    Input Argument: 
    Folder name : Path of the folder where csv file is added
    symbol : name of the stock
    index_col: Column for indexing
    
    Output: 
    Stock data with date as index 
    """ 
    file_name = folder_name + "/" + symbol + ".csv" 
    data = pd.read_csv(file_name) 
    data[index_col] = pd.to_datetime(data[index_col]) 
    data = data.set_index(index_col)
    print("stock name: ", symbol) 
    return data

    

def get_price_yahoo(symbol, data_source, start_date = "1/1/2010", end_date = "1/1/2011"):
    """
    Get high low open close volume adj close data for a stock within the range
    
    Parameters
    ----------------------
    symbol : The name of the stock
    
    data_source :  Name of the data source
    
    start_date : start date for the date range
    
    end_date : end date for the date range
    """
    stock_name = symbol + '.NS'
    data = web.DataReader(name = stock_name, data_source = data_source, start = start_date, end = end_date)
    print('stock name', symbol)
    return data
    
