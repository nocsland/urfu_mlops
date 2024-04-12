#!/bin/bash

# Проверяем, запущен ли скрипт непосредственно из каталога scripts
if [[ "$(basename "$(pwd)")" != "scripts" ]]; then
  echo "Скрипт должен быть запущен из каталога где он расположен (scripts)"
  exit 1
fi

# Проверка активации виртуального окружения
if [[ -z "${VIRTUAL_ENV}" ]]; then
   echo "Виртуальное окружение не активировано"

   # Создание виртуального окружения
   python3 -m venv ../../venv

   # Активация виртуального окружения
   source ../../venv/bin/activate
   echo "Проверяю и устанавливаю зависимости"
   pip install -r ../requirements.txt
else
   echo "Виртуальное окружение активировано"
fi

cd ../src || exit

echo "Запускаю пайплайн"

# Запуск создания данных
python data_creation.py

# Запуск предобработки данных
python model_preprocessing.py

# Запуск подготовки и обучения модели
python model_preparation.py

# Запуск тестирования модели
python model_testing.py
