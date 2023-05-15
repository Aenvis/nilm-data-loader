from numpy import mean
from pandas import read_parquet, to_datetime, DataFrame
import data_loader as dl
import matplotlib.pyplot as plt

def main():


    data = dl.load_enertalk(R'data\enertalk\20161002\01_fridge.parquet.gzip')
    # data = dl.load_enertalk(R'data\enertalk\20161006\00_total.parquet.gzip')
    dl.plot_enertalk(data, "Fridge", '20161002')


if __name__ == '__main__':
    main()
