from urls import *

existing_courier = {
    "login": "test12345asd",
    "password": "test12345",
    "firstName": "name"
}

login_pass_uncorrect = [
    {
    "login": "",
    "password": "test12345"
},
    {
    "login": "test",
    "password": ""
}
]

login_pass_with_error = [
    {
    "login": "test12345asd1",
    "password": "test12345"
},
    {
    "login": "test12345asd",
    "password": "test1234"
}
]

order_color = [{
    "firstName": "Masha",
    "lastName": "Ivanova",
    "address": "Ivanovo, Pavlovskaya str.",
    "metroStation": 4,
    "phone": "+7 920 000 00 01",
    "rentTime": 2,
    "deliveryDate": "2026-04-08",
    "comment": "Comment here",
    "color": [
        "BLACK"
    ]
},
{
    "firstName": "Masha",
    "lastName": "Ivanova",
    "address": "Ivanovo, Pavlovskaya str.",
    "metroStation": 4,
    "phone": "+7 920 000 00 01",
    "rentTime": 2,
    "deliveryDate": "2026-04-08",
    "comment": "Comment here",
    "color": [
        "BLACK"
    ]
},
{
    "firstName": "Masha",
    "lastName": "Ivanova",
    "address": "Ivanovo, Pavlovskaya str.",
    "metroStation": 4,
    "phone": "+7 920 000 00 01",
    "rentTime": 2,
    "deliveryDate": "2026-04-08",
    "comment": "Comment here",
    "color": [
        "BLACK",
        "GREY"
    ]
},
{
    "firstName": "Masha",
    "lastName": "Ivanova",
    "address": "Ivanovo, Pavlovskaya str.",
    "metroStation": 4,
    "phone": "+7 920 000 00 01",
    "rentTime": 2,
    "deliveryDate": "2026-04-08",
    "comment": "Comment here",
}]

test_order = {
    "firstName": "Masha",
    "lastName": "Ivanova",
    "address": "Ivanovo, Pavlovskaya str.",
    "metroStation": 4,
    "phone": "+7 920 000 00 01",
    "rentTime": 2,
    "deliveryDate": "2026-04-08",
    "comment": "Comment here",
    "color": [
        "BLACK"
    ]
}

url_list_order = order_list_urls

url_list_order_for_courier = order_list_urls_for_courier

existing_courier_id = 721912

not_existing_courier_id = 1

without_courier_id = ''

not_existing_order_id = 1

without_order_track = ''

not_existing_order_track = '001'

ok_response = {"ok": True}

not_existing_courier_id_response = "Курьера с таким id не существует"

without_courier_id_response = "Недостаточно данных для поиска"

not_existing_order_id_response = "Заказа с таким id не существует"

without_id_response = "Not Found."

not_existing_courier_delete = "Курьера с таким id нет."

without_order_track_response = "Недостаточно данных для поиска"

not_existing_order_track_response = "Заказ не найден"

error_login = "Недостаточно данных для входа"

not_found_login = "Учетная запись не найдена"

login_used = "Этот логин уже используется"

not_enough_data = "Недостаточно данных для создания учетной записи"
