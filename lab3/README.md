# MLOps. Практическое задание №3

### Выполнено практическое задание

    В рамках задания развернуто приложение в docker контейнере. Согласно ТЗ, это модель логистической регрессии на 
    датасете iris, принимающая запрос по API и возвращающая ответ.

### Запуск приложения
Запуск необходимо выполнять из каталога `lab3`
```
./pipeline.sh
```
Приложение будет развернуто по адресу 
```
http://localhost:8000/
```
Примеры запросов для классификации расположены в каталоге
```
/lab3/samples/
```

### Реализованные эндпоинты

Информационный эндпоинт
```
GET /
```
Эндпоинт для классификации ирисов
```
POST /predict
```

### Последовательность выполнения операций при создании образа и запуске контейнера
1. Загружаем базовый образ
2. Переключаем на root
3. Устанавливаем рабочую директорию
4. Копируем файлы приложения в контейнер
5. Устанавливаем зависимости
6. Запускаем приложение

### Действия выполняемые в приложении
- Определяем входные параметры модели
- Загружаем датасет
- Записываем датасет в CSV
- Выполняем предобработку данных
- Обучаем модель
- Записываем модель в файл
- Сопоставляем индексы с названиями классов
- Создаем эндпоинт для классификации ирисов
- Создаем эндпоинт возвращающий информационное сообщение

### Каталоги и файлы
Датасет и модель 
```
/lab3/data/
```
Приложение 
```
/lab3/src/app.py
```
Примеры запросов
```
/lab3/samples/
```








