#!/bin/bash

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    echo "Python не найден. Установите Python для продолжения."
    exit 1
fi

# Проверяем, запущен ли скрипт непосредственно из каталога scripts
if [[ "$(basename "$(pwd)")" != "scripts" ]]; then
  echo "Скрипт должен быть запущен из каталога, где он расположен (scripts)"
  exit 1
fi

# Проверяем наличие файла requirements.txt
if [ ! -f "../requirements.txt" ]; then
    echo "Файл requirements.txt не найден."
    exit 1
fi

# Проверка активации виртуального окружения
if [[ -z "${VIRTUAL_ENV}" ]]; then
   echo "Виртуальное окружение не активировано"

   # Создание виртуального окружения
   python3 -m venv ../../venv || { echo "Ошибка при создании виртуального окружения."; exit 1; }

   # Активация виртуального окружения
   source ../../venv/bin/activate || { echo "Ошибка при активации виртуального окружения."; exit 1; }

   echo "Устанавливаю зависимости"
   pip install -r ../requirements.txt || { echo "Ошибка при установке зависимостей."; exit 1; }
else
   echo "Виртуальное окружение активировано"
fi

cd ../src || { echo "Не удалось перейти в каталог src"; exit 1; }

echo "Запускаю пайплайн"

echo "Запуск создания данных"
python data_creation.py || { echo "Ошибка при выполнении data_creation.py"; exit 1; }

echo "Запуск предобработки данных"
python model_preprocessing.py || { echo "Ошибка при выполнении model_preprocessing.py"; exit 1; }

echo "Запуск подготовки и обучения модели"
python model_preparation.py || { echo "Ошибка при выполнении model_preparation.py"; exit 1; }

echo "Запуск тестирования модели"
python model_testing.py || { echo "Ошибка при выполнении model_testing.py"; exit 1; }
