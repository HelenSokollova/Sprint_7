import requests
import allure

class TestAcceptOrder:
    @allure.title('Проверка успешного принятия заказа курьером')
    @allure.description('Проверяет принятие заказа существующим курьером, код ответа 200, структура ответа корректна')
    def test_accept_order_success(self, create_and_get_order):
        order_id = create_and_get_order
        courier_id = 721912
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert response_json == {"ok": True}

    @allure.title('Проверка неуспешного принятия заказа несуществующим курьером')
    @allure.description('Проверяет невозможность принятия заказа несуществующим курьером, код ответа 404, message ответа корректен')        
    def test_accept_order_not_exist_id_courier(self, create_and_get_id):
        order_id = create_and_get_id
        courier_id = 1
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        assert response.status_code == 404
        assert response.json().get("message") == "Курьера с таким id не существует"

    @allure.title('Проверка неуспешного принятия заказа при отсутсвии переданного id курьера')
    @allure.description('Проверяет невозможность принятия заказа курьером, если его id не передан, код ответа 400, message ответа корректен')
    def test_accept_order_without_id_courier(self, create_and_get_id):
        order_id = create_and_get_id
        courier_id = ''
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    @allure.title('Проверка неуспешного принятия несуществующего заказа курьером')
    @allure.description('Проверяет невозможность принятия несуществующего заказа курьером, код ответа 404, message ответа корректен')
    def test_accept_order_not_exist_id_order(self):
        order_id = 1
        courier_id = 721912
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        assert response.status_code == 404
        assert response.json().get("message") == "Заказа с таким id не существует"

    @allure.title('Проверка неуспешного принятия заказа при отсутсвии переданного id заказа')
    @allure.description('Проверяет невозможность принятия заказа курьером, если id заказа не передан, код ответа 404, message ответа корректен')
    def test_accept_order_without_id_order(self):
        courier_id = 721912
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/?courierId={courier_id}')
        assert response.status_code == 404
        assert response.json().get("message") == "Not Found."
