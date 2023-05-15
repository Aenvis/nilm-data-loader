import csv
from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_parquet, to_datetime
from sklearn.preprocessing import MinMaxScaler


def load_enertalk(path: str) -> pd.DataFrame:
    data = read_parquet(path)

    # Convert timestamp to hour
    data['time'] = to_datetime(data['timestamp'], unit='ms').dt.hour
    return data

def filter_data(series: pd.Series, window_size: int) -> pd.Series:
    rolling_mean = series.rolling(window_size).mean()
    series = rolling_mean
    return series

def plot_enertalk(data: pd.DataFrame, device: str, date: str) -> None:
    path = 'data/enertalk/xx/00_total.parquet.gzip'
    path = path.replace('xx', date)

    aggregated_data = load_enertalk(path)
    aggregated_data['active_power'] = filter_data(aggregated_data['active_power'], 300)
    # aggregated_data = filter_data(data)
    aggregated_power = aggregated_data['active_power']
    aggregated_power = np.nan_to_num(aggregated_power, nan=0, posinf=0, neginf=0)
    aggregated_time = to_datetime(aggregated_data['timestamp'], unit='ms').dt.hour

    active_power = data['active_power']
    hour = data['time']

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)

    ax1.plot(hour, active_power)
    ax1.set_xlabel('Hour')
    ax1.set_ylabel('Active Power: ' + device)

    # Plotting the second subplot
    ax2.plot(aggregated_time, aggregated_power)
    ax2.set_xlabel('Hour')
    ax2.set_ylabel('Aggregated Power')

    # Setting the y-axis range of the second subplot
    ax1.set_ylim(0, max(aggregated_power))

    # Adjusting the spacing between subplots
    plt.subplots_adjust(hspace=0.4)
    plt.suptitle('Aggregated power and ' + device + ' power')
    print(get_avg_measurement_enertalk(data))
    print(get_max_measurement_enertalk(data))
    print(get_number_of_starts_enertalk(data))
    # Displaying the plot
    plt.show()

def get_avg_measurement_enertalk(data: pd.DataFrame) -> float:
    return np.mean(data["active_power"])

def get_max_measurement_enertalk(data: pd.DataFrame) -> float:
    return np.max(data["active_power"])

def get_number_of_starts_enertalk(data: pd.DataFrame) -> int:
    threshold = 100  # You need to set a proper threshold based on your specific appliance.
    data['start'] = ((data['active_power'] > threshold) & 
                     (data['active_power'].shift(1) < threshold)).astype(int)
    return data['start'].sum()
