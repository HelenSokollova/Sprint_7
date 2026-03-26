import requests
from urls import *
import data
import allure

class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    @allure.description('Проверяет удаление курьера, код ответа 200, структура ответа корректна')
    def test_delete_courier_success(self, login_courier):
        courier_id = login_courier
        with allure.step('Отправляем запрос на удаление курьера'):
            response = requests.delete(Urls.delete_courier(courier_id))
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == data.ok_response

    @allure.title('Проверка невозможности удаления курьера с несуществующим id')
    @allure.description('Проверяет невозможность удалить курьера с несуществующим id, код ответа 404, message ответа корректен')
    def test_delete_not_exist_courier(self):
        courier_id = data.not_existing_courier_id
        with allure.step('Отправляем запрос на удаление курьера с несуществующим id'):
            response = requests.delete(Urls.delete_courier(courier_id))
        assert response.status_code == 404
        assert response.json().get("message") == data.not_existing_courier_delete

    @allure.title('Проверка невозможности удаления курьера без id')
    @allure.description('Проверяет невозможность удалить курьера без id, код ответа 404, message ответа корректен')
    def test_delete_courier_without_id(self):
        courier_id = data.without_courier_id
        with allure.step('Отправляем запрос на удаление курьера без id'):
            response = requests.delete(Urls.delete_courier(courier_id))
        assert response.status_code == 404
        assert response.json().get("message") == data.without_id_response
    