import pandas as pd

# Загрузка датасета
df = pd.read_csv('../datasets/titanic/titanic_data.csv')

# Применение one-hot-encoding для признака "Sex"
sex_one_hot = pd.get_dummies(df['Sex'], prefix='Sex')

# Добавление новых признаков в исходный DataFrame
df = pd.concat([df, sex_one_hot], axis=1)

# Сохранение новой версии датасета
df.to_csv('../datasets/titanic/titanic_data.csv', index=False)
