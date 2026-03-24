import requests
import allure

class TestGetOrderTrack:
    @allure.title('Проверка успешного получения информации о заказе по треку')
    @allure.description('Проверяет получение информации о заказе по треку, код ответа 200, структура ответа корректна')
    def test_get_order(self, create_and_delete_order):
        track = create_and_delete_order
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
        assert response.status_code == 200
        r = response.json()
        assert "order" in r

    @allure.title('Проверка невозможности получения информации о заказе без трека')
    @allure.description('Проверяет отсутствие получения информации о заказе,если не передан его трек, код ответа 400, message ответа корректен')
    def test_get_order_without_track(self):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=')
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    @allure.title('Проверка невозможности получения информации о заказе с несуществующим треком')
    @allure.description('Проверяет отсутствие получения информации о заказе,если передан несуществующий трек, код ответа 404, message ответа корректен')
    def test_get_order_not_exist_track(self):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=001')
        assert response.status_code == 404
        assert response.json().get("message") == "Заказ не найден"

