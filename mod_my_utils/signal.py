import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_combined_signal(signal1, signal2):
    """
    Get signal combined with two different signals
    Input: signal1 and signal2 for the same date range
    Output: combined signal
    """
    combined_signal = pd.DataFrame(index=signal1.index)
    combined_signal['price'] = signal1['price'] 
    combined_signal['buy_sell'] = 0.0
    combined_signal['buy_sell'].loc[(signal1['buy_sell'] == 1.0) & (signal2['buy_sell'] == 1.0)] = 1.0
    combined_signal['buy_sell'].loc[(signal1['buy_sell'] == -1.0) & (signal2['buy_sell'] == -1.0)] = -1.0
    return combined_signal[['price', 'buy_sell']]


def plot_signals_buy_sell(signals, symbol):
    fig = plt.figure(figsize=(20, 5))
    ax1 = fig.add_subplot(1,1,1)
    signals[['price']].plot(ax=ax1, title = symbol)
    ax1.plot(signals.loc[signals.buy_sell == 1].index, signals.price[signals.buy_sell == 1],"^", markersize = 12, color ='g')
    ax1.plot(signals.loc[signals.buy_sell == -1].index, signals.price[signals.buy_sell == -1],"v", markersize = 12, color ='m')
    plt.show() 