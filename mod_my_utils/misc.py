import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from mod_my_utils.read_write_data import get_price_yahoo


# singal stock functionality
def summary(data):
    """
    This method provide summary of data frame
    with columns, index, first few rows, basic statistics and plot for all numerical columns
    """
    print('Columns of data frame \n', data.columns)
    print('Row information \n',  data.index)
    print('First few rows \n', data.head(3))
    print('Summary Statistics\n', data.describe())
    data.plot()
    plt.show()
    
# Multiple stocks functionality
def stocks_dataframe(stocks_names, start_date, end_date, data_source):
    """
    Input: stocks_names is a list of stock, start date, end date, data source
    Output: Data frame with date as index, different columns has different adjusted closing price
    """
    count = 1
    for stock in stocks_names:
    #     print(stock)
        symbol = stock
        print(stock)
        data = get_price_yahoo(symbol= symbol, data_source= data_source, start_date= start_date, end_date= end_date)
    #     print(data.head())
        if count == 1:
            df = data[['Adj Close']]
            df.columns = [stock]
        elif count > 1:
            df[stock] = data[['Adj Close']]
    #     print(df.head())
        count = count + 1
    #     print(count)
#     print(df.head())
    return df

# Multiple stocks functionality
def stocks_summary(stocks_names, start_date, end_date, data_source):
    """
    Input: Folder path, stocks_names is a list of stock
    Output: Columns name, index, summary statistics, plot for each stock
    """
    stocks_df = stocks_dataframe(stocks_names, start_date, end_date, data_source)
    print("Stocks Name: ", stocks_df.columns)
    print("Dates: ", stocks_df.index)
    print("Summary of stocks price: \n", stocks_df.describe())
    print("Graphs of stocks price:")
    stocks_df.plot()
    plt.show()