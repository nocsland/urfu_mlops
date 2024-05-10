import allure
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@allure.feature("Translation API")
class TestTranslation:

    @allure.story("Translate Russian to English")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_ru_en_404(self):
        with allure.step("Sending translation request from Russian to English"):
            response = client.post("/translate/ru-en/", json={"text": "привет"})
        with allure.step("Verifying response status code"):
            assert response.status_code == 404

    @allure.story("Translate Russian to English")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_ru_en_ok(self):
        with allure.step("Sending translation request from Russian to English"):
            response = client.post("/translate/ru-to-en/", json={"text": "привет"})
        with allure.step("Verifying response status code and translated text"):
            assert response.status_code == 200
            assert response.json() == {"translated_text": "Hey."}

    @allure.story("Translate Russian to English")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_ru_en_phrase_ok(self):
        with allure.step("Sending translation request with text phrase from Russian to English"):
            response = client.post("/translate/ru-to-en/", json={"text": "Пример текстовой фразы."})
        with allure.step("Verifying response status code and translated text"):
            assert response.status_code == 200
            assert response.json() == {"translated_text": "Example of a text phrase."}

    @allure.story("Translate Russian to English")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_ru_en_error(self):
        with allure.step("Sending translation request from Russian to English"):
            response = client.post("/translate/ru-to-en/", json={"text": "привет"})
        with allure.step("Verifying response status code and translation text"):
            assert response.status_code == 200
            assert not response.json() == {"translation_text": "Hi."}

    @allure.story("Translate Russian to English")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_ru_en_not_200(self):
        with allure.step("Sending translation request from Russian to English with incorrect data"):
            response = client.post("/translate/ru-to-en/", json={"message": "привет"})
        with allure.step("Verifying response status code"):
            assert response.status_code == 422

    @allure.story("Translate English to Russian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_en_ru_404(self):
        with allure.step("Sending translation request from English to Russian"):
            response = client.post("/translate/en-ru/", json={"text": "hello"})
        with allure.step("Verifying response status code"):
            assert response.status_code == 404

    @allure.story("Translate English to Russian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_en_ru_ok(self):
        with allure.step("Sending translation request from English to Russian"):
            response = client.post("/translate/en-to-ru/", json={"text": "hello"})
        with allure.step("Verifying response status code and translated text"):
            assert response.status_code == 200
            assert response.json() == {"translated_text": "Привет."}

    @allure.story("Translate English to Russian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_en_ru_phrase_ok(self):
        with allure.step("Sending translation request with text phrase from English to Russian"):
            response = client.post("/translate/en-to-ru/", json={"text": "Example of a text phrase."})
        with allure.step("Verifying response status code and translated text"):
            assert response.status_code == 200
            assert response.json() == {"translated_text": "Пример формулировки текста."}

    @allure.story("Translate English to Russian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_en_ru_error(self):
        with allure.step("Sending translation request from English to Russian"):
            response = client.post("/translate/en-to-ru/", json={"text": "hello"})
        with allure.step("Verifying response status code and translated text"):
            assert response.status_code == 200
            assert not response.json() == {"translated_text": "Не Привет."}

    @allure.story("Translate English to Russian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_translate_en_ru_error_not_200(self):
        with allure.step("Sending translation request from English to Russian with incorrect data"):
            response = client.post("/translate/en-to-ru/", json={"message": "hello"})
        with allure.step("Verifying response status code"):
            assert response.status_code == 422
