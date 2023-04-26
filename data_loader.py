import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, header=None, delimiter=';', names=['date', 'measurement1', 'measurement8'])
    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y %H:%M:%S')
    data['time'] = data['date'].dt.time
    return data

def plot(data: pd.DataFrame) -> None:
    # Set the index to the 'date' column
    data = data.set_index('date')
    # Plot the 'measurement8' column
    plt.plot(data['measurement1'])
    # Set the x-axis tick marks to every 2 hours
    x_ticks = pd.date_range(start=data.index.max() - pd.Timedelta(hours=23), end=data.index.max(), freq='2H')
    plt.xticks(x_ticks, x_ticks.strftime('%H:%M:%S'), rotation=45, ha='right', fontsize=8)
    # Set the x-axis label
    plt.xlabel('Time')
    # Set the y-axis label
    plt.ylabel('Measurement 1')

    last_measurement = data['measurement1'].iloc[-1]
    top_position = np.max(data['measurement1'])
    plt.text(data.index[len(data['time'])/2], top_position, get_avg_measurment(data))

    # Show the plot
    plt.show()

def get_avg_measurment(data: pd.DataFrame) -> str:
    return f'avg: {"{:.2f}".format(np.mean(data["measurement1"]))}'