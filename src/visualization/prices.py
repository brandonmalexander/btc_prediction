import pandas as pd
import matplotlib.pyplot as plt

read_from = '/home/brandon/Northeastern/1b_Spring18/EECE_2300/3_15_2lmao/btc_prediction/src/data/price_data.csv'
prices = pd.read_csv(filepath_or_buffer=read_from, infer_datetime_format=True)
prices = prices.set_index(prices.columns[0])
prices = prices.set_index(pd.DatetimeIndex(prices.index).to_pydatetime())

plt.figure(figsize=(20,10), dpi=80)
plt.plot(prices.index, prices.price)
plt.xlabel('date')
plt.ylabel('price (USD)')

plt.savefig('prices.png')

