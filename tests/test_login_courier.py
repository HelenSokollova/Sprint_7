import pytest
import requests
import data
import allure

class TestLoginCourier:
    @allure.title('Проверка успешного логина зарегистрированного курьера')
    @allure.description('Проверяем, что код ответа 200, id курьера содержится в ответе')
    def test_login_success(self):
        login_pass = data.existing_courier
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_pass)
        assert response.status_code == 200
        r = response.json()
        assert "id" in r

    @allure.title('Проверка неуспешного логина курьера без login или без пароля')
    @allure.description('Параметризованный тест, проверяет логин курьера без login или без пароля, код ответа 400, message ответа корректен')
    @pytest.mark.parametrize('payload', data.login_pass_uncorrect)
    def test_without_a_required_field(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"

    @allure.title('Проверка неуспешного логина курьера с ошибкой в  login или пароле')
    @allure.description('Параметризованный тест, проверяет логин курьера c ошибкой логина(несуществующий пользователь) и пароля, код ответа 404, message ответа корректен')
    @pytest.mark.parametrize('payload', data.login_pass_with_error)
    def test_login_with_error_login_pass(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

