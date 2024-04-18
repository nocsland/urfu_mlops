from catboost.datasets import titanic

# Загрузка датасета
data_df, _ = titanic()

# Сохранение в CSV
data_df.to_csv('../datasets/titanic/titanic_data.csv', index=False)
