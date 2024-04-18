# MLOps. Практическое задание №4


### Выполнено практическое задание
    В рамках данного задания выполнены все основные операции с dvc. 
    Полученные теоретические знания, закрепленены, практическими действиями.

### Ссылки
- [Репозиторий с кодом](https://github.com/nocsland/urfu_mlops/tree/master/lab4)
- [README](https://github.com/nocsland/urfu_mlops/blob/master/lab4/README.md)
- [Функции для предобработки данных](https://github.com/nocsland/urfu_mlops/tree/master/lab4/src)
- [Облачное хранилище датасетов](https://drive.google.com/drive/folders/1kn2TH2myV6_gXmE1dFD76KoezClE1ygp?usp=sharing)
- [файл DVC для отслеживания версий данных](https://github.com/nocsland/urfu_mlops/blob/master/lab4/datasets.dvc)

### Коммиты
```
85987d6 (HEAD -> master, origin/master, origin/HEAD) Update titanic dataset: "Restore data for Passenger 1"
ad6e2da Update titanic dataset: "Add one-hot-encoding for sex field"
1120321 Add sex_one_hot.py
605bfe3 Update titanic dataset: nan values replace to mean
4263257 Add replace_nan_to_mean.py
876a1fd Update info Passenger 1. Change Pclass, Sex, Age
9f27fa0 Add loader for dataset titanic
739ce32 Add datasets titanic, remove irises
464575d Add datasets gitignore information
2040652 Add datasets gitignore information
bfa5086 Rename datasets folder
f2d0300 Add dvc
```
### Дополнения
Для переключения между версиями датасета использовал следующую конструкцию
```
git log --oneline
git checkout <commit_id>
dvc pull
```
Для возвращения к текущей актуальной версии датасета
```
git checkout master
dvc pull
```