import numpy as np

def Brownian(seed, N):
    """Generates Brownian Motion.
    :param seed:   random seed to use
    :param N:      increments
    :return W:     brownian motion
    :return b:     brownian increments
    """
    np.random.seed(seed)                         
    dt = 1./N
    b = np.random.normal(0., 1., int(N))*np.sqrt(dt)
    W = np.cumsum(b)
    return W, b

def modified_GBM(So, mu, sigma, W, N):    
    """Generates Geometric Brownian Motion.
    :param So:       starting price
    :param mu:       drift coefficient
    :param sigma:    diffusion coefficient
    :param W:        Brownian Motion
    :param N:        increments
    :return S:       Geometric Brownian Motion (S(t))
    :return t:       all time-steps
    """
    t = np.linspace(0.,1.,N+1)
    S = []
    S.append(So)
    for i in range(1,int(N+1)):
        drift = (mu - 0.5 * sigma**2) * t[i]
        diffusion = sigma * W[i-1]
        # effect of sentiment = some weight * sentiment
        S_temp = So*np.exp(drift + diffusion)# + ^^ )
        S.append(S_temp)
    return S, t

def daily_returns(close, timefactor):
    """Calculates daily returns, drift, and diffusion
    :param close:       iterable of closing prices
    :param timefactor:  ex, scale from 1 to 252 (trade days)
    :return returns:    daily returns
    :return mu:         drift
    :return sigma:      diffusion
    """
    returns = []
    for i in range(0, len(close)-1):
        today = close[i+1]
        yesterday = close[i]
        r = (today - yesterday) / yesterday
        returns.append(r)
    mu = np.mean(returns)*(timefactor*1.) # drift
    sigma = np.std(returns)*np.sqrt(timefactor*1.)#diffusion
    return mu, sigma


"""
So = 55.25 # also close[0]
timefactor = 252
seed = 22

N = 2.**6
W = Brownian(seed, N)[0]

mu = .15 #daily_returns(close, timefactor)[1]
sigma = .4 #daily_returns(close, timefactor)[2]

S, xs = modified_GBM(So, mu, sigma, W, N)
plt.plot(xs, S)
plt.show()
"""
