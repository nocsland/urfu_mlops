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
    @pytest.mark.parametrize("el", test_data["train"])
    def test_keys_existence(self, el):
        with allure.step("Convert string to dictionary"):
            el_dict = dict(literal_eval(el))
        with allure.step("Check 'id' key existence"):
            assert "id" in el_dict, "Key 'id' is missing"
        with allure.step("Check 'translation' key existence"):
            assert "translation" in el_dict, "Key 'translation' is missing"
        with allure.step("Check 'en' translation existence"):
            assert "en" in el_dict["translation"], "English translation is missing"
        with allure.step("Check 'ru' translation existence"):
            assert "ru" in el_dict["translation"], "Russian translation is missing"

    @allure.title("Check Data Types")
    @allure.description("Ensure values for each key have the expected data type")
    @pytest.mark.parametrize("el", test_data["train"])
    def test_data_types(self, el):
        with allure.step("Convert string to dictionary"):
            el_dict = dict(literal_eval(el))
        with allure.step("Check 'id' data type"):
            assert isinstance(el_dict["id"], str), "id should be a string"
        with allure.step("Check 'translation' data type"):
            assert isinstance(el_dict["translation"], dict), "translation should be a dictionary"
        with allure.step("Check translation values data type"):
            assert all(isinstance(value, str) for value in
                       el_dict["translation"].values()), "All translations should be strings"

    @allure.title("Check ID Format")
    @allure.description("Ensure the ID format is correct")
    @pytest.mark.parametrize("el", test_data["train"])
    def test_id_format(self, el):
        with allure.step("Convert string to dictionary"):
            el_dict = dict(literal_eval(el))
        with allure.step("Check ID format"):
            assert re.match(r'^\d+$', el_dict["id"]), "ID format is incorrect"

    @allure.title("Check Translation Content")
    @allure.description("Ensure translation content is not empty or whitespace")
    @pytest.mark.parametrize("el", test_data["train"])
    def test_translation_content(self, el):
        with allure.step("Convert string to dictionary"):
            el_dict = dict(literal_eval(el))
        with allure.step("Check translation content"):
            for lang, text in el_dict["translation"].items():
                assert text.strip(), f"Translation for {lang} is empty or whitespace"

    @allure.title("Check Unique IDs")
    @allure.description("Ensure IDs are unique")
    def test_unique_ids(self):
        with allure.step("Extract IDs from dataset"):
            ids = [dict(literal_eval(item))['id'] for item in test_data["train"]]
        with allure.step("Check ID uniqueness"):
            assert len(ids) == len(set(ids)), "IDs are not unique"
