from ast import literal_eval
import pandas as pd
import re
import allure
import pytest

DATASET_PATH = "data/datasets/dataset.csv"
test_data = pd.read_csv(filepath_or_buffer=DATASET_PATH)


@allure.feature("Data Quality Checks")
class TestDataQualityChecks:

    @allure.title("Check Existence of All Keys")
    @allure.description("Ensure all necessary keys are present in the dataset")
    def test_keys_existence(self):
        train = test_data["train"]
        for el in train:
            el_dict = dict(literal_eval(el))
            assert "id" in el_dict, "Key 'id' is missing"
            assert "translation" in el_dict, "Key 'translation' is missing"
            assert "en" in el_dict["translation"], "English translation is missing"
            assert "ru" in el_dict["translation"], "Russian translation is missing"

    @allure.title("Check Data Types")
    @allure.description("Ensure values for each key have the expected data type")
    def test_data_types(self):
        train = test_data["train"]
        for el in train:
            el_dict = dict(literal_eval(el))
            assert isinstance(el_dict["id"], str), "id should be a string"
            assert isinstance(el_dict["translation"], dict), "translation should be a dictionary"
            assert all(
                isinstance(value, str) for value in el_dict["translation"].values()
            ), "All translations should be strings"

    @allure.title("Check ID Format")
    @allure.description("Ensure the ID format is correct")
    def test_id_format(self):
        train = test_data["train"]
        for el in train:
            assert re.match(r'^\d+$', dict(literal_eval(el))["id"]), "ID format is incorrect"

    @allure.title("Check Translation Content")
    @allure.description("Ensure translation content is not empty or whitespace")
    def test_translation_content(self):
        train = test_data["train"]
        for el in train:
            for lang, text in dict(literal_eval(el))["translation"].items():
                assert text.strip(), f"Translation for {lang} is empty or whitespace"

    @allure.title("Check Unique IDs")
    @allure.description("Ensure IDs are unique")
    def test_unique_ids(self):
        ids = [dict(literal_eval(item))['id'] for item in test_data["train"]]
        assert len(ids) == len(set(ids)), "IDs are not unique"
