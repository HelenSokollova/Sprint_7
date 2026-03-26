import pytest
import requests
import random
import string
import data
from urls import *


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
    response = requests.post(Urls.create_courier, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass, response.status_code, response.json()


@pytest.fixture(scope='function')
def login_courier(register_new_courier_and_return_login_password):
    login_pass = register_new_courier_and_return_login_password[0]
    if len(login_pass) == 3:
        login = login_pass[0]
        password = login_pass[1]
    else:
        login, password = None, None
    courier_id = None
    if login and password:
        login_response = requests.post(Urls.login_courier,
                                      json={"login": login, "password": password})
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
    yield courier_id


@pytest.fixture(scope='function')
def delete_courier():
    login_pass = []
    yield login_pass

    for login, password in login_pass:
        login_response = requests.post(Urls.login_courier,
                                      json={"login": login, "password": password})
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                requests.delete(Urls.delete_courier(courier_id))

@pytest.fixture(scope='function')
def delete_order():
    tracks = []
    
    yield tracks
    
    for track in tracks:
        if track:
            requests.put(Urls.cancel_order_by_track(track))


@pytest.fixture(scope='function')
def create_and_delete_order():
        response = requests.post(Urls.create_order, json=data.test_order)
        track = None
        if response.status_code == 201:
            r = response.json()
            if "track" in r:
                track = r["track"]
                
        yield track
    
        if track:
            requests.put(Urls.cancel_order_by_track(track))

#####################################################
@pytest.fixture(scope='function')
def finish_order():
    order_ids = []
    
    yield order_ids
    
    for order_id in order_ids:
        if order_id:
            requests.put(Urls.finish_order_by_id(order_id))
##############################################################

@pytest.fixture(scope='function')
def create_and_get_order():
    response = requests.post(Urls.create_order, json=data.test_order)
    track = None
    order_id = None
    if response.status_code == 201:
        r = response.json()
        if "track" in r:
            track = r["track"]
            response_track = requests.get(Urls.get_order_by_track(track))
            if response_track.status_code == 200:
                    track_data = response_track.json()
                    order_id = track_data["order"]["id"]
    
    yield order_id
    
    if order_id:
        requests.put(Urls.finish_order_by_id(order_id))


@pytest.fixture(scope='function')
def create_and_get_id():
    response = requests.post(Urls.create_order, json=data.test_order)
    track = None
    order_id = None
    if response.status_code == 201:
        r = response.json()
        if "track" in r:
            track = r["track"]
    response_track = requests.get(Urls.get_order_by_track(track))
    if response_track.status_code == 200:
                    track_data = response_track.json()
                    order_id = track_data["order"]["id"]
    
    yield order_id 
    
