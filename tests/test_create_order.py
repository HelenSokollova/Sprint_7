import pytest
import requests
import data
import allure

class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Параметризованный тест, проверяет создание заказа черного или серого цвета, двух цветов, без выбора цвета самоката. Проверяем, что код ответа 201, track заказа содержится в ответе')
    @pytest.mark.parametrize('order_color', data.order_color)
    def test_create_order(self, order_color, delete_order):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_color)
        assert response.status_code == 201
        r = response.json()
        assert "track" in r
        delete_order.append(r["track"])

