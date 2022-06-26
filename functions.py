from datetime import datetime
import config
import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.special import erfinv
import pandas as pd
import time


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


def run(M, N, X, h, a, b, end, log, save=False):
    log.info(f"Starting")
    output = []
    for i, x in enumerate(X):
        T = []
        for _ in range(M):
            T.append(wiener_plot(x, h, a, b, end))
        output.append(np.mean(T))
        log.info(f"Computed run {i + 1}/{N} ( {100 * (i + 1) / N}% )")
    log.info(f"Done")

    if save:
        to_csv(data=output,
               index=X,
               cols=["time"])
    return output


def to_csv(index, data, cols):
    df = pd.DataFrame(data,
                      index=index,
                      columns=cols)
    filename = config.SAVE_DIR + "output" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    df.to_csv(filename)
