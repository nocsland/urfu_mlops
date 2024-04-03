import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Загрузка предобработанных данных
data = pd.read_csv('../data/train/train_data_preprocessed.csv')
X = data[['day']]
y = data['temperature']

# Разделение данных на обучающую и валидационную выборки
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=1, random_state=42)

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, '../data/model/model.pkl')
