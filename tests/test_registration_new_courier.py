import pytest
import requests
import data
import random
import string
from urls import *
import allure

class TestRegistrationNewCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверяем, что курьер создан, код ответа 201, структура ответа корректна')
    def test_register_new_courier(self, delete_courier):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        with allure.step('Отправляем запрос на создание курьера'):
            response = requests.post(Urls.create_courier, json=payload)
        assert response.status_code == 201
        assert response.json() == data.ok_response
        delete_courier.append((login, password))


    @allure.title('Проверка неуспешного создания курьера с существующим логином')
    @allure.description('Проверяем, что при создании курьера с уже существующим логином код ответа 409, сообщение об ошибке корректно')
    def test_register_existing_courier(self):
        payload = data.existing_courier
        with allure.step('Отправляем запрос на создание курьера с существующим логином'):
            response = requests.post(Urls.create_courier, json=payload)
        assert response.status_code == 409
        message = response.json().get("message")
        assert data.login_used in message


    @allure.title('Проверка неуспешного создания курьера без логина или без пароля')
    @allure.description('Параметризованный тест. Проверяем невозможность создания курьера без логина или без пароля, код ответа 400, структура ответа корректна')
    @pytest.mark.parametrize('payload', data.login_pass_uncorrect)
    def test_without_a_required_field(self, payload):
        with allure.step('Отправляем запрос на создание курьера без логина/пароля'):
            response = requests.post(Urls.create_courier, json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == data.not_enough_data
    