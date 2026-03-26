import requests
from urls import *
import data
import allure

class TestAcceptOrder:
    @allure.title('Проверка успешного принятия заказа курьером')
    @allure.description('Проверяет принятие заказа существующим курьером, код ответа 200, структура ответа корректна')
    def test_accept_order_success(self, create_and_get_order):
        order_id = create_and_get_order
        courier_id = data.existing_courier_id
        with allure.step('Отправляем запрос на принятие заказа существующим курьером'):
            response = requests.put(Urls.accept_order(order_id, courier_id))
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == data.ok_response

    @allure.title('Проверка неуспешного принятия заказа несуществующим курьером')
    @allure.description('Проверяет невозможность принятия заказа несуществующим курьером, код ответа 404, message ответа корректен')        
    def test_accept_order_not_exist_id_courier(self, create_and_get_id):
        order_id = create_and_get_id
        courier_id = data.not_existing_courier_id
        with allure.step('Отправляем запрос на принятие заказа несуществующим курьером'):
            response = requests.put(Urls.accept_order(order_id, courier_id))
        assert response.status_code == 404
        assert response.json().get("message") == data.not_existing_courier_id_response

    @allure.title('Проверка неуспешного принятия заказа при отсутсвии переданного id курьера')
    @allure.description('Проверяет невозможность принятия заказа курьером, если его id не передан, код ответа 400, message ответа корректен')
    def test_accept_order_without_id_courier(self, create_and_get_id):
        order_id = create_and_get_id
        courier_id = data.without_courier_id
        with allure.step('Отправляем запрос на принятие заказа без id курьера'):
            response = requests.put(Urls.accept_order(order_id, courier_id))
        assert response.status_code == 400
        assert response.json().get("message") == data.without_courier_id_response

    @allure.title('Проверка неуспешного принятия несуществующего заказа курьером')
    @allure.description('Проверяет невозможность принятия несуществующего заказа курьером, код ответа 404, message ответа корректен')
    def test_accept_order_not_exist_id_order(self):
        order_id = data.not_existing_order_id
        courier_id = data.existing_courier_id
        with allure.step('Отправляем запрос на принятие несуществующего заказа курьером'):
            response = requests.put(Urls.accept_order(order_id, courier_id))
        assert response.status_code == 404
        assert response.json().get("message") == data.not_existing_order_id_response

    @allure.title('Проверка неуспешного принятия заказа при отсутсвии переданного id заказа')
    @allure.description('Проверяет невозможность принятия заказа курьером, если id заказа не передан, код ответа 404, message ответа корректен')
    def test_accept_order_without_id_order(self):
        courier_id = data.existing_courier_id
        with allure.step('Отправляем запрос на принятие заказа без id курьером'):
            response = requests.put(Urls.accept_order_without_order_id(courier_id))
        assert response.status_code == 404
        assert response.json().get("message") == data.without_id_response
