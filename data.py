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

url_list_order = [
    'https://qa-scooter.praktikum-services.ru/api/v1/orders',
    'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0',
    'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0&nearestStation=["4"]'
]

url_list_order_for_courier = [
    'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=721912',
    'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=721912&nearestStation=["4", "2"]'
]
