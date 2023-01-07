import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_macd_signal_line(data, short_window = 20, long_window = 50, signal_window = 12):
    """
    Get SMA, LMA, MACD, signal_line
    
    parameters
    -----------------------------
    short_window: short moving average size
    long_window: long moving average size
    signal_window: moving average size for signal line
    Output:
    Data frame with price, SMA, LMA, MACD, signal_line
    SMA: short moving average
    LMA: long moving average
    MACD: SMA - LMA
    signal_line: moving average of MACD
    """
    macd_data = data.copy()
    # Create the set of short and long simple moving average, MACD, signal line over the 
    # respective periods
    macd_data["SMA"] = macd_data['price'].rolling(window = short_window, center=False).mean()
    macd_data["LMA"] = macd_data['price'].rolling(window = long_window, center=False).mean()
    macd_data["MACD"] = macd_data['SMA'] - macd_data['LMA']
    macd_data['signal_line'] = macd_data['MACD'].rolling(window = signal_window).mean()
    return macd_data

def get_signal_macd_crossover(macd_signal_line, long_window):
    """
    Get signal from macd crossover
    
    parameters
    -------------------------
    Input: 
    SMA, LMA, MACD, signal_line
    output: Trading signal from cross over of long and short moving average
    Buy Signal = 1, Sell Signal = -1, Do nothing = 0
    """
    signals = pd.DataFrame(index = macd_signal_line.index)
    signals['price'] = macd_signal_line['price']
    signals['buy_sell'] = 0.0
    signals['buy_sell'][long_window:] = np.where((macd_signal_line.MACD)[long_window:] 
                                            > 0, 1.0, 0.0)  
    signals['buy_sell'] = signals['buy_sell'].diff()
    # return buy and sell signal
    return signals

def get_signal_macd_signalline(macd_signal_line, long_window):
    """
    Get trading signals from macd and signal line
    
    Parameters
    -------------------------------
    Input: data frame with macd values and macd signal line
    output: Trading signal from cross over of macd and macd signal line
    Buy Signal = 1, Sell Signal = -1, Do nothing = 0
    """
    signals = pd.DataFrame(index=macd_signal_line.index)
    signals['price'] = macd_signal_line['price']
    signals['buy_sell'] = 0.0
    signals['buy_sell'][long_window:] = np.where((macd_signal_line.MACD)[long_window:] 
                                            > macd_signal_line.signal_line[long_window:], 1.0, 0.0)  
    signals['buy_sell'] = signals['buy_sell'].diff()
    # return buy and sell signal
    return signals

def plot_macd_buy_sell(macd_signal_line, signals, symbol = 'HDFC'):
    """
    Get plot for macd price, shortma, longma, buy signal, sell signal
    Input: data frame with all above information
    Output: None
    """
    # putting all above together
    fig = plt.figure(figsize=(12,8))
    plt.title(symbol)
    #fig1
    ax1 = fig.add_subplot(411, ylabel='Price in $')
    macd_signal_line['price'].plot(ax=ax1, color = 'r', lw = 2.)
    macd_signal_line[['SMA', 'LMA']].plot(ax = ax1, lw=2.)
    #fig2
    ax2 = fig.add_subplot(412, ylabel = 'buy signal')
    signals['price'].plot(ax=ax2, color = 'r', lw = 2.)
    ax2.plot(signals.loc[signals.buy_sell == 1.0].index, signals.price[signals.buy_sell == 1.0], '^', markersize=10, color = 'm')
    #fig3
    ax3 = fig.add_subplot(413, ylabel = 'sell signal')
    signals['price'].plot(ax=ax3, color = 'r', lw = 2.)
    ax3.plot(signals.loc[signals.buy_sell == -1.0].index, signals.price[signals.buy_sell == -1.0], 'v', markersize=10, color='k')
    #fig4
    ax4 = fig.add_subplot(414, ylabel='buy sell signal')
    signals['price'].plot(ax=ax4, color = 'r', lw = 2.)
    # add buy sell
    ax4.plot(signals.loc[signals.buy_sell == 1.0].index, signals.price[signals.buy_sell == 1.0], '^', markersize=10, color = 'g')
    ax4.plot(signals.loc[signals.buy_sell == -1.0].index, signals.price[signals.buy_sell == -1.0], 'v', markersize=10, color='k')
    #
    plt.show()
    
    
    
    
if __name__ == '__main__':
    pass
    
    import seaborn as sn
    
    # get stock data
    # macd_values = 
    # macd_signal =
    # plot graph
    