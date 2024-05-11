from ast import literal_eval
import pandas as pd
import re

DATASET_PATH = "../data/datasets/dataset.csv"
test_data = pd.read_csv(filepath_or_buffer=DATASET_PATH)


# Проверка наличия всех необходимых ключей
def test_keys_existence():
    train = test_data["train"]
    for el in train:
        el_dict = dict(literal_eval(el))
        assert "id" in el_dict, "Key 'id' is missing"
        assert "translation" in el_dict, "Key 'translation' is missing"
        assert "en" in el_dict["translation"], "English translation is missing"
        assert "ru" in el_dict["translation"], "Russian translation is missing"


# Проверка типов данных: значения для каждого ключа имеют ожидаемый тип
def test_data_types():
    train = test_data["train"]
    for el in train:
        el_dict = dict(literal_eval(el))
        assert isinstance(el_dict["id"], str), "id should be a string"
        assert isinstance(el_dict["translation"], dict), (
            "translation should be a dictionary"
        )
        assert all(
            isinstance(value, str) for value in el_dict["translation"].values()
        ), "All translations should be strings"


# Проверка формата ID
def test_id_format():
    train = test_data["train"]
    for el in train:
        assert re.match(r'^\d+$', dict(literal_eval(el))["id"]), \
            "ID format is incorrect"


# Проверка содержимого перевода
def test_translation_content():
    train = test_data["train"]
    for el in train:
        for lang, text in dict(literal_eval(el))["translation"].items():
            assert text.strip(), f"Translation for {lang} is empty or whitespace"


# Проверка уникальности ID
def test_unique_ids():
    ids = [dict(literal_eval(item))['id'] for item in test_data["train"]]
    assert len(ids) == len(set(ids)), "IDs are not unique"
