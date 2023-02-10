import pandas as pd
import matplotlib.pyplot as pl
from creating_datasets import return_lst_of_frames


# функция возврата готового DataFrame объекта
def return_dataframe(frame):
    return pd.read_csv(f"data/datasets/data_{frame}.csv", sep=";", header=0, index_col=False, decimal=",")


# функция для создания гистограмм
def create_histogram():
    for frame, _ in return_lst_of_frames():
        df = return_dataframe(frame)
        df = df.astype(float)

        df.plot(x='Value', y=frame, kind='hist', bins=120)
        pl.savefig(f'data/histograms/hist_{frame}.png')
