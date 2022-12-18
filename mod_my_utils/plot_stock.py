
import matplotlib.pyplot as plt

def plot_stock(stock, data, var_list):
    """
    Plotting of different stock prices
    Input: dataframe with open, close etc data
    Output": Plot of selected prices
    """
    print('cloumns selected for plotting', var_list)
    data[var_list].plot(title = stock)

    
def plot_signals(signals, symbol):
    fig = plt.figure(figsize=(20, 5))
    ax1 = fig.add_subplot(1,1,1)
    signals[['price']].plot(ax=ax1, title = symbol)
    ax1.plot(signals.loc[signals.buy_sell == 1].index, signals.price[signals.buy_sell == 1],"^", markersize = 12, color ='g')
    ax1.plot(signals.loc[signals.buy_sell == -1].index, signals.price[signals.buy_sell == -1],"v", markersize = 12, color ='m')

    plt.show()