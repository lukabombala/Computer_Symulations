import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import config
import functions
import logging

log = logging.getLogger("plots")
if config.LOGGING:
    logging.basicConfig(level=logging.INFO)


def ex_plot(filename):
    data = pd.read_csv(f"{config.SAVE_DIR}{filename}")

    plt.plot(data['x'],data['time'])

    outname = functions.create_save_name(config.PLOTS_DIR,
                                        "ex_plot",
                                         config.PLOT_EXT)
    plt.savefig(outname)
    log.info(f\n"Saved to file {outname}")


filename = "ex_output20220626-174642.csv"
ex_plot(filename)