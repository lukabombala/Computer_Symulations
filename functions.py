import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sms
import seaborn as sns
from scipy.special import erfinv

import logging

log = logging.getLogger("my-logger")


def wiener_plot(x, h, a, b, end):
    W = [x]
    T = [0]
    n = 0
    while n < end:
        k = rnd.normal()
        w = W[-1] + np.sqrt(h) * k
        n += 1
        W.append(w)
        T.append(T[-1] + h)
    return T, W


def wiener_times_out(x, h, a, b, end):
    W = x
    T = 0
    n = 0
    while n < end:
        if (W < a) or (W > b):
            break
        k = rnd.normal()
        W += np.sqrt(h) * k
        n += 1
        T += h
    return T


def run():
    output = []
    for i, x in enumerate(X):
        T = []
        for i in range(M):
            T.append(wiener_plot(x, h, a, b, end))
        output.append(np.mean(T))
        log.info(f"Computed run {i}/{N}")
    return output
