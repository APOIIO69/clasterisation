import pandas as pd
import matplotlib
import matplotlib.pyplot as pl
from creating_datasets import return_lst_of_frames


def return_dataframe(frame):
    return pd.read_csv(f"data/datasets/data_{frame}.csv", sep=";", header=0, index_col=False, decimal=",")


def create_histogram():
    for frame, _ in return_lst_of_frames():
        df = return_dataframe(frame)
        df = df.astype(float)

        df.plot(x='Value', y=frame, kind='hist', bins=120)
        pl.savefig(f'data/histograms/hist_{frame}.png')
