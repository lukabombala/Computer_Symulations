from datetime import datetime
import config
import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt
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

def wiener_prob_b(x, h, a, b, end,log):
    W = x
    n = 0
    output = None
    while n < end:
        if (W < a):
            output = False
            break
        elif (W > b):
            output = True
            break
        k = rnd.normal()
        W += np.sqrt(h) * k
        n += 1
    if output is None:
        log.warning("Reached loop end\n")
    return output

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
               name="ex_output",
               log=log)
    return np.array(output)


def run_prob(M, N, X, h, a, b, end, log, save=False):
    log.info(f"Starting")
    output = []
    for i, x in enumerate(X):
        P=[]
        for _ in range(M):
            P.append(wiener_prob_b(x, h, a, b, end,log))
        output.append(sum(P)/M)
        log.info(f"Computed run {i + 1}/{N} ( {100 * (i + 1) / N}% )")
    log.info(f"Done")

    if save:
        to_csv(data=output,
               index=X,
               name="prob_output",
               log=log)
    return np.array(output)

    
def to_csv(index, data, log, name):
    d = {"x": index, "time": data}
    df = pd.DataFrame(d)
    filename = create_save_name(config.SAVE_DIR, 
                                name, 
                                ".csv")
    df.to_csv(filename)
    log.info(f"Saving...")
    log.info(f"Saved to file {filename}")

def create_save_name(predir, name, ext, timestamp=True):
    temp = predir + name
    if timestamp:
        temp += datetime.now().strftime("%Y%m%d-%H%M%S")
    return temp + ext