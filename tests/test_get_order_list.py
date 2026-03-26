import requests
import pytest
import data
from urls import *
import allure

class TestOrderList:
    @allure.title('Проверка получения списка заказов без id курьера')
    @allure.description('Параметризованный тест, проверяет получение списка заказов, получение 10 заказов для взятия курьером, список заказов по одной станции метро. Проверяем, что код ответа 200, заказы содержится в ответе')
    @pytest.mark.parametrize('url', data.url_list_order)
    def test_get_order_list(self, delete_order, url):
        with allure.step('Отправляем запрос на создание заказа'):
            response = requests.post(Urls.create_order, json=data.test_order)
            track = None
            if response.status_code == 201:
                track = response.json().get("track")
            if track:
                delete_order.append(track)
        with allure.step('Отправляем запрос на получение списка заказов'):
            response = requests.get(url)
        assert response.status_code == 200
        orders_data = response.json()
        assert "orders" in orders_data

    @allure.title('Проверка получения списка заказов по id курьера')
    @allure.description('Параметризованный тест, проверяет получение списка заказов курьера, список заказов курьера по станции метро. Проверяем, что код ответа 200, заказы содержится в ответе')
    @pytest.mark.parametrize('url', data.url_list_order_for_courier)
    def test_get_order_list_for_courier(self, finish_order, url):
        with allure.step('Отправляем запрос на создание заказа'):
            response = requests.post(Urls.create_order, json=data.test_order)
            track = None
            if response.status_code == 201:
                track = response.json().get("track")
            if track:
                finish_order.append(track)
        order_id = None
        if track:
            with allure.step('Отправляем запрос для получения id заказа по track'):
                track_response = requests.get(Urls.get_order_by_track(track))
        
            if track_response.status_code == 200:
                order_id = track_response.json()["order"]["id"]
        
        courier_id = data.existing_courier_id
        if order_id:
            with allure.step('Отправляем запрос на принятие заказа курьером'):
                requests.put(Urls.accept_order(order_id, courier_id))
        
        with allure.step('Отправляем запрос на получение списка заказов курьера'):
            url = url.format(courier_id=courier_id)
            response = requests.get(url)
        assert response.status_code == 200
        orders_data = response.json()
        assert "orders" in orders_data
