from numpy import mean
from pandas import read_parquet, to_datetime, DataFrame
import data_loader as dl
import matplotlib.pyplot as plt

def get_avg_measurment(data: DataFrame) -> str:
    return f'avg: {"{:.2f}".format(mean(data["active_power"]))}'

def get_max_measurment(data: DataFrame) -> str:
    return f'max: {"{:.2f}".format(max(data["active_power"]))}'
def main():


    # data = dl.load_enertalk(R'data\enertalk\20161006\01_fridge.parquet.gzip')
    data = dl.load_enertalk(R'data\enertalk\20161006\00_total.parquet.gzip')
    # Extract the 'active_power' and 'hour' column data
    active_power = data['active_power']
    hour = data['time']

    # Create a plot using Matplotlib
    plt.plot(hour, active_power)
    plt.xlabel('Hour')
    plt.ylabel('Active Power')
    plt.title('Fridge usage')

    top_position = max(data['active_power'])
    print(get_avg_measurment(data))
    print(get_max_measurment(data))
    plt.show()



     # dl.plot(data)


if __name__ == '__main__':
    main()
