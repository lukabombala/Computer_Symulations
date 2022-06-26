import functions
from functions import *
import logging
import config

log = logging.getLogger("run")
if config.LOGGING:
    logging.basicConfig(level=logging.INFO)

h = 0.05
M = 20
a = 25
b = 75
N = 50
X = np.linspace(a, b, N)
end = 10000

T = run(M, N, X, h, a, b, end, log, save=True)
