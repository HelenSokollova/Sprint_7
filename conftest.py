import pytest
import requests
import random
import string
import data


@pytest.fixture(scope='function')
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass, response.status_code, response.json()

@pytest.fixture(scope='function')
def delete_courier_after_test(register_new_courier_and_return_login_password):
    login_pass, status_code, response_json = register_new_courier_and_return_login_password
    if len(login_pass) == 3:
        login, password, first_name = login_pass
    else:
        login, password, first_name = None, None, None
    yield login_pass, status_code, response_json

    login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                  json={"login": login, "password": password})
    
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
            if delete_response.status_code == 200:
                print(f"Курьер с ID {courier_id} успешно удален")
            else:
                print(f"Ошибка при удалении курьера: {delete_response.status_code}")
    else:
        print("Не удалось получить ID курьера для удаления")

@pytest.fixture(scope='function')
def delete_order():
    tracks = []
    
    yield tracks
    
    for track in tracks:
        if track:
            response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel?track={track}')
            assert response.status_code == 200

@pytest.fixture(scope='function')
def create_and_delete_order():
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data.test_order)
        assert response.status_code == 201
        r = response.json()
        assert "track" in r

        track = r["track"]
                
        yield track
    
        if track:
            response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel?track={track}')
            assert response.status_code == 200

@pytest.fixture(scope='function')
def create_finish_and_delete_order():
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data.test_order)
        assert response.status_code == 201
        r = response.json()
        assert "track" in r
        track = r["track"]
        response_track = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
        assert response_track.status_code == 200
        track_data = response_track.json()
        order_id = track_data["order"]["id"]
        courier_id = 721912
        accept_response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        assert accept_response.status_code == 200
        yield order_id
    
        if order_id:

            finish_response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/finish/{order_id}')
            assert finish_response.status_code == 200

@pytest.fixture(scope='function')
def create_and_get_order():
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data.test_order)
    assert response.status_code == 201
    r = response.json()
    assert "track" in r
    track = r["track"]
    response_track = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
    assert response_track.status_code == 200
    track_data = response_track.json()
    order_id = track_data["order"]["id"]
    
    yield order_id
    
    if order_id:
        finish_response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/finish/{order_id}')
        assert finish_response.status_code == 200

@pytest.fixture(scope='function')
def create_and_get_id():
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data.test_order)
    assert response.status_code == 201
    r = response.json()
    assert "track" in r
    track = r["track"]
    response_track = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
    assert response_track.status_code == 200
    track_data = response_track.json()
    order_id = track_data["order"]["id"]
    
    yield order_id 
    
