import pytest
import requests
import data
import allure

class TestRegistrationNewCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверяем, что создан не пустой список, код ответа 201, структура ответа корректна')
    def test_register_new_courier(self, delete_courier_after_test):
        login_pass, status_code, response_json = delete_courier_after_test
        assert len(login_pass) == 3
        assert status_code == 201
        assert response_json == {"ok": True}

    @allure.title('Проверка неуспешного создания курьера с существующим логином')
    @allure.description('Проверяем, что при создании курьера с уже существующим логином код ответа 409, сообщение об ошибке корректно')
    def test_register_existing_courier(self):
        payload = data.existing_courier
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 409
        message = response.json().get("message")
        assert "Этот логин уже используется" in message

    @allure.title('Проверка неуспешного создания курьера без логина или без пароля')
    @allure.description('Параметризованный тест. Проверяем невозможность создания курьера без логина или без пароля, код ответа 400, структура ответа корректна')
    @pytest.mark.parametrize('payload', data.login_pass_uncorrect)
    def test_without_a_required_field(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"
    
 