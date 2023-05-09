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

    # Plot the 'measurement1' column
    plt.plot(data['measurement1'])
    
    # Set the x-axis tick marks to every 2 hours
    x_ticks = pd.date_range(start=data.index.max() - pd.Timedelta(hours=23), end=data.index.max(), freq='2H')
    plt.xticks(x_ticks, x_ticks.strftime('%H:%M:%S'), rotation=45, ha='right', fontsize=8)

    plt.xlabel('Time')
    plt.ylabel('Measurement 1')

    top_position = np.max(data['measurement1'])
    plt.text(data.index[len(data['time']) // 2],   top_position,      f'avg: {"{:.2f}".format(get_avg_measurment(data))}')
    plt.text(data.index[len(data['time']) // 2],   top_position - 50, f'max: {"{:.2f}".format(get_max_measurment(data))}')
    plt.text(data.index[len(data['time']) // 2],   top_position - 60, f'num of triggers: {get_number_of_starts(data)}')
    # Show the plot
    plt.show()

def get_avg_measurment(data: pd.DataFrame) -> float:
    return np.mean(data["measurement1"])

def get_max_measurment(data: pd.DataFrame) -> float:
    return np.max(data["measurement1"])

def get_number_of_starts(data: pd.DataFrame) -> int:
    avg = get_avg_measurment(data)
    print(avg)
    numberOfStarts = 0
    isWorking = 0
    timeWorking = 0
    for dt in data["measurement1"]:
        if dt > avg:
            isWorking = 1
            timeWorking += 1
        elif dt < avg and isWorking and timeWorking > 10:
            isWorking = 0
            timeWorking = 0
            numberOfStarts += 1
    return numberOfStarts