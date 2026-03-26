import requests
from urls import *
import data
import allure

class TestGetOrderTrack:
    @allure.title('Проверка успешного получения информации о заказе по треку')
    @allure.description('Проверяет получение информации о заказе по треку, код ответа 200, структура ответа корректна')
    def test_get_order(self, create_and_delete_order):
        track = create_and_delete_order
        with allure.step('Отправляем запрос на получение информации о заказе по треку'):
            response = requests.get(Urls.get_order_by_track(track))
        assert response.status_code == 200
        r = response.json()
        assert "order" in r

    @allure.title('Проверка невозможности получения информации о заказе без трека')
    @allure.description('Проверяет отсутствие получения информации о заказе,если не передан его трек, код ответа 400, message ответа корректен')
    def test_get_order_without_track(self):
        track = data.without_order_track
        with allure.step('Отправляем запрос на получение информации о заказе без трека'):
            response = requests.get(Urls.get_order_by_track(track))
        assert response.status_code == 400
        assert response.json().get("message") == data.without_order_track_response

    @allure.title('Проверка невозможности получения информации о заказе с несуществующим треком')
    @allure.description('Проверяет отсутствие получения информации о заказе,если передан несуществующий трек, код ответа 404, message ответа корректен')
    def test_get_order_not_exist_track(self):
        track = data.not_existing_order_track
        with allure.step('Отправляем запрос на получение информации о заказе по несуществующему треку'):
            response = requests.get(Urls.get_order_by_track(track))
        assert response.status_code == 404
        assert response.json().get("message") == data.not_existing_order_track_response
