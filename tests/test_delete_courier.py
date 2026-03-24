import requests
import allure

class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    @allure.description('Проверяет удаление курьера, код ответа 200, структура ответа корректна')
    def test_delete_courier_success(self, register_new_courier_and_return_login_password):
        login_pass = register_new_courier_and_return_login_password[0]
        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                  json = {"login": login_pass[0], "password": login_pass[1]})
        assert login_response.status_code == 200
        courier_id = login_response.json().get("id")
        delete_response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
        assert delete_response.status_code == 200
        response_json = delete_response.json()
        assert response_json == {"ok": True}

    @allure.title('Проверка невозможности удаления курьера с несуществующим id')
    @allure.description('Проверяет невозможность удалить курьера с несуществующим id, код ответа 404, message ответа корректен')
    def test_delete_not_exist_courier(self):
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/1')
        assert response.status_code == 404
        assert response.json().get("message") == "Курьера с таким id нет."

    @allure.title('Проверка невозможности удаления курьера без id')
    @allure.description('Проверяет невозможность удалить курьера без id, код ответа 404, message ответа корректен')
    def test_delete_courier_without_id(self):
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/')
        assert response.status_code == 404
        assert response.json().get("message") == "Not Found."
    