import functions
from functions import *
import logging
import config

log = logging.getLogger("run")
if config.LOGGING:
    logging.basicConfig(level=logging.INFO)

h = 0.05
M = 80  # runs for each argument
a = 25
b = 75
N = 100 # domain length
X = np.linspace(a, b, N)
end = 50000

run(M, N, X, h, a, b, end, log, save=True)

#run_prob(M, N, X, h, a, b, end, log, save=True)
