import pandas as pd
import matplotlib.pyplot as plt

read_from = '/home/brandon/Desktop/2300 final project/btc_prediction/src/data/price_data_4-25.csv'
prices = pd.read_csv(filepath_or_buffer=read_from, infer_datetime_format=True)
prices = prices.set_index(prices.columns[0])
prices = prices.set_index(pd.DatetimeIndex(prices.index).to_pydatetime())

plt.figure(figsize=(20,10), dpi=80)
plt.plot(prices.index, prices.price)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Price (USD)', fontsize=20)
plt.title('Price of BTC, 2015-2018', fontsize=30)

plt.savefig('prices.png')

