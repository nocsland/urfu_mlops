from fastapi.testclient import TestClient

from translator.src.app import app


client = TestClient(app)


def test_translate_ru_en_404():
    response = client.post(
        "/translate/ru-en/",
        json={"text": "привет"},
    )
    assert response.status_code == 404


def test_translate_ru_en_ok():
    response = client.post(
        "/translate/ru-to-en/",
        json={"text": "привет"},
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Hey."}


def test_translate_ru_en_phrase_ok():
    response = client.post(
        "/translate/ru-to-en/",
        json={"text": "Пример текстовой фразы."},
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Example of a text phrase."}


def test_translate_ru_en_error():
    response = client.post(
        "/translate/ru-to-en/",
        json={"text": "привет"},
    )
    assert response.status_code == 200
    assert not response.json() == {"translation_text": "Hi."}


def test_translate_ru_en_not_200():
    response = client.post(
        "/translate/ru-to-en/",
        json={"message": "привет"}
    )
    assert response.status_code == 422


def test_translate_en_ru_404():
    response = client.post(
        "/translate/en-ru/",
        json={"text": "привет"},
    )
    assert response.status_code == 404


def test_translate_en_ru_ok():
    response = client.post(
        "/translate/en-to-ru/",
        json={"text": "hello"},
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Привет."}


def test_translate_en_ru_phrase_ok():
    response = client.post(
        "/translate/en-to-ru/",
        json={"text": "Example of a text phrase."},
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Пример формулировки текста."}


def test_translate_en_ru_error():
    response = client.post(
        "/translate/en-to-ru/",
        json={"text": "hello"},
    )
    assert response.status_code == 200
    assert not response.json() == {"translated_text": "Не Привет."}


def test_translate_en_ru_error_not_200():
    response = client.post(
        "/translate/en-to-ru/",
        json={"message": "hello"}
    )
    assert response.status_code == 422
