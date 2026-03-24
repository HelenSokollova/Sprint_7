import requests
import pytest
import data
import allure

class TestOrderList:
    @allure.title('Проверка получения списка заказов без id курьера')
    @allure.description('Параметризованный тест, проверяет получение списка заказов, получение 10 заказов для взятия курьером, список заказов по одной станции метро. Проверяем, что код ответа 200, заказы содержится в ответе')
    @pytest.mark.parametrize('url', data.url_list_order)
    def test_get_order_list(self, create_and_delete_order, url):
        track = create_and_delete_order
        assert track is not None
        response = requests.get(url)
        assert response.status_code == 200
        orders_data = response.json()
        assert "orders" in orders_data

    @allure.title('Проверка получения списка заказов по id курьера')
    @allure.description('Параметризованный тест, проверяет получение списка заказов курьера, список заказов курьера по станции метро. Проверяем, что код ответа 200, заказы содержится в ответе')
    @pytest.mark.parametrize('url', data.url_list_order_for_courier)
    def test_get_order_list_for_courier(self, create_finish_and_delete_order, url):
        order_id = create_finish_and_delete_order
        assert order_id is not None
        response = requests.get(url)
        assert response.status_code == 200
        orders_data = response.json()
        assert "orders" in orders_data
