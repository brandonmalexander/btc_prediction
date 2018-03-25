import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gbm

seed = 5
N = 2**6

W = gbm.Brownian(seed, N)[0]



prices = pd.read_csv('data/price_data.csv', infer_datetime_format=True)
p = prices['price']
timefactor = 1109

mu, sigma = gbm.daily_returns(p, timefactor)



S, xs = gbm.GBM(p[0], mu, sigma, W, N)

plt.plot(xs, S)
plt.show()
