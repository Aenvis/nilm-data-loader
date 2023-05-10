import csv
from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, header=None, delimiter=';', names=['date', 'measurement1', 'measurement8'])
    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y %H:%M:%S')
    data['time'] = data['date'].dt.time
    return data

def sum_power_values(csv_files, output_file):
    data_column = []
    power_sums = []

    for file_index, file in enumerate(csv_files):
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            file_power_sum = [0, 0]  # Suma wartości mocy dla aktualnego pliku
            for row_index, row in enumerate(reader):
                if file_index == 0:
                    data_column.append(row[0])

                # Sprawdzenie rozmiaru listy power_sums
                if row_index >= len(power_sums):
                    power_sums.append([0, 0])

                # Dodawanie sumy wartości w drugiej i trzeciej kolumnie dla danego wiersza
                power_sums[row_index][0] += int(row[1])
                power_sums[row_index][1] += int(row[2])

    # Zapisywanie danych do nowego pliku CSV
    with open(output_file, 'w', newline='') as csv_output:
        writer = csv.writer(csv_output, delimiter=';')
        for i, date in enumerate(data_column):
            writer.writerow([date, power_sums[i][0], power_sums[i][1]])

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
    plt.text(data.index[len(data['time']) // 2], top_position,      f'avg: {"{:.2f}".format(get_avg_measurement(data))}')
    plt.text(data.index[len(data['time']) // 2],   top_position - 50, f'max: {"{:.2f}".format(get_max_measurment(data))}')
    plt.text(data.index[len(data['time']) // 2],   top_position - 120, f'num of triggers: {get_number_of_starts(data)}')
    # Show the plot
    plt.show()

def get_avg_measurement(data: pd.DataFrame) -> float:
    return np.mean(data["measurement1"])

def get_max_measurment(data: pd.DataFrame) -> float:
    return np.max(data["measurement1"])



# def get_number_of_starts(data: pd.DataFrame) -> int:
#     avg = get_avg_measurement(data)
#     print(avg)
#     numberOfStarts = 0
#     isWorking = False
#     timeWorking = 0
#     for dt in data["measurement1"]:
#         if dt > avg:
#             isWorking = True
#             timeWorking += 1
#         elif dt < avg and isWorking and timeWorking > 10:
#             isWorking = False
#             timeWorking = 0
#             numberOfStarts += 1
#     return numberOfStarts
def get_number_of_starts(data: pd.DataFrame) -> int:
    avg = get_avg_measurement(data)
    print(avg)

    # Create a column indicating whether the measurement is above the average or not
    data['is_above_avg'] = data['measurement1'] > avg

    # Initialize variables
    is_working = False
    starts = 0
    consecutive_count = 0

    for above_avg in data['is_above_avg']:
        if above_avg:
            consecutive_count += 1
            if not is_working and consecutive_count >= 10:
                is_working = True
                starts += 1
        else:
            consecutive_count = 0
            is_working = False

    return starts