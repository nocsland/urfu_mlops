#!/bin/bash

# ВАЖНО! Данный скрипт настроен на запуск в сборке Jenkins.

# Получение пути к директории Jenkins Home
JENKINS_HOME="$JENKINS_HOME"

# Путь к каталогу сборки
BUILD_DIR="/build"

# Создание каталога build в корневом каталоге
mkdir -p "$BUILD_DIR" || { echo "Ошибка при создании каталога 'build'."; exit 1; }

# Проверка наличия каталога MLOps в директории Jenkins Home
if [ ! -d "$JENKINS_HOME/workspace/MLOps" ]; then
    echo "Каталог MLOps не найден в директории Jenkins Home."
    exit 1
fi

# Копирование всех файлов и каталогов из $JENKINS_HOME/workspace/MLOps в каталог build
cp -R "$JENKINS_HOME/workspace/MLOps/"* "$BUILD_DIR" || { echo "Ошибка при копировании содержимого MLOps."; exit 1; }

# Создание виртуального окружения
python3 -m venv "$BUILD_DIR/venv" || { echo "Ошибка при создании виртуального окружения."; exit 1; }

# Активация виртуального окружения
source "$BUILD_DIR/venv/bin/activate" || { echo "Ошибка при активации виртуального окружения."; exit 1; }

# Установка зависимостей
pip install -r "$BUILD_DIR/lab2/requirements.txt" || { echo "Ошибка при установке зависимостей."; exit 1; }

# Переход в каталог src
cd "$BUILD_DIR/lab2/src" || { echo "Не удалось перейти в каталог src"; exit 1; }

echo "Запуск создания данных"
python data_creation.py || { echo "Ошибка при выполнении data_creation.py"; exit 1; }

echo "Запуск предобработки данных"
python model_preprocessing.py || { echo "Ошибка при выполнении model_preprocessing.py"; exit 1; }

echo "Запуск подготовки и обучения модели"
python model_preparation.py || { echo "Ошибка при выполнении model_preparation.py"; exit 1; }

echo "Запуск тестирования модели"
python model_testing.py || { echo "Ошибка при выполнении model_testing.py"; exit 1; }