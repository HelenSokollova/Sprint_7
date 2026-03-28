import pytest
import requests
import data
from urls import *
import allure

class TestLoginCourier:
    @allure.title('Проверка успешного логина зарегистрированного курьера')
    @allure.description('Проверяем, что код ответа 200, id курьера содержится в ответе')
    def test_login_success(self):
        login_pass = data.existing_courier
        with allure.step('Отправляем запрос на авторизацию зарегистрированного курьера'):
            response = requests.post(Urls.login_courier, json=login_pass)
        assert response.status_code == 200
        r = response.json()
        assert "id" in r

    @allure.title('Проверка неуспешного логина курьера без login или без пароля')
    @allure.description('Параметризованный тест, проверяет логин курьера без login или без пароля, код ответа 400, message ответа корректен')
    @pytest.mark.parametrize('payload', data.login_pass_uncorrect)
    def test_without_a_required_field(self, payload):
        with allure.step('Отправляем запрос на авторизацию курьера без логина/пароля'):
            response = requests.post(Urls.login_courier, json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == data.error_login

    @allure.title('Проверка неуспешного логина курьера с ошибкой в  login или пароле')
    @allure.description('Параметризованный тест, проверяет логин курьера c ошибкой логина(несуществующий пользователь) и пароля, код ответа 404, message ответа корректен')
    @pytest.mark.parametrize('payload', data.login_pass_with_error)
    def test_login_with_error_login_pass(self, payload):
        with allure.step('Отправляем запрос на авторизацию курьера с ошибкой в логине/пароле'):
            response = requests.post(Urls.login_courier, json=payload)
        assert response.status_code == 404
        assert response.json().get("message") == data.not_found_login
