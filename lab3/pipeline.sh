#!/bin/bash

# Проверяем, запущен ли скрипт непосредственно из каталога lab3
if [[ "$(basename "$(pwd)")" != "lab3" ]]; then
  echo "Скрипт должен быть запущен из каталога 'lab3'"
  exit 1
fi


# создаем образ
docker build -t iris-api-image .

# создаем и запускаем контейнер
docker run -d --restart always  --name iris-api-container -p 8000:8000 iris-api-image