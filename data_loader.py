from datetime import datetime
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, header=None, delimiter=';', names=['date', 'measurment1', 'measurment8'])
    #data['date'] = np.asarray(data['date'], dtype='datetime64[s]')
    return data

def plot(data: pd.DataFrame) -> None:
    #plt.xticks(data['date'], rotation=90)
    plt.plot(data['measurment8'])
    plt.show()