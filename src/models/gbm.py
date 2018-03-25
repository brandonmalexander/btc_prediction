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

def GBM(So, mu, sigma, W, N):    
    """Generates Geometric Brownian Motion.
    :param So:       starting price
    :param mu:       drift coefficient
    :param sigma:    diffusion coefficient
    :param W:        Brownian Motion
    :param N:        increments to predict
    :return S:       Geometric Brownian Motion (S(t))
    :return t:       all time-steps
    """
    t = np.linspace(0.,1.,N+1)
    S = []
    S.append(So)
    for i in range(1,int(N+1)):
        drift = (mu - 0.5 * sigma**2) * t[i]
        diffusion = sigma * W[i-1]
        S_temp = So*np.exp(drift + diffusion)
        S.append(S_temp)
    return S, t

def daily_returns(close, N):
    """Calculates daily returns, then drift and diffusion from those returns.
    :param close:       iterable of closing prices as [n, price]
    :param N:           increments to predict
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
    mu = np.mean(returns)*(N*1.) # drift
    sigma = np.std(returns)*np.sqrt(N*1.)#diffusion
    return mu, sigma

def modify_GBM(S, sentiment, alpha):
    """Modify GBM to account for sentiment. Used to tune alpha.
    
    """
    pass
