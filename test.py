import pandas as pd

def get_data(folder_name, stock_name):
    file_name = folder_name + stock_name + '.csv'
    data = pd.read_csv(file_name)
    return data