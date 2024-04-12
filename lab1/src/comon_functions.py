import os

import numpy as np


# Функция для загрузки данных из файлов в указанной директории
def load_data_from_directory(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                data.append(float(file.read()))
    return np.array(data)


# Загрузка данных из папок 'train' и 'test'
train_data_normal = load_data_from_directory('../data/train/_normal_temperature')
train_data_anomaly = load_data_from_directory('../data/train/_anomaly_temperature')
test_data_normal = load_data_from_directory('../data/test/_normal_temperature')
test_data_anomaly = load_data_from_directory('../data/test/_anomaly_temperature')
