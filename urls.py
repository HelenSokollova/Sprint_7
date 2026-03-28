import data

class Urls:
    base_url = 'https://qa-scooter.praktikum-services.ru'

    create_order = f'{base_url}/api/v1/orders'
    login_courier = f'{base_url}/api/v1/courier/login'
    get_orders = f'{base_url}/api/v1/orders'
    create_courier = f'{base_url}/api/v1/courier'

    @staticmethod
    def accept_order(order_id, courier_id):
        return f'{Urls.base_url}/api/v1/orders/accept/{order_id}?courierId={courier_id}'
    
    @staticmethod
    def accept_order_without_order_id(courier_id):
        return f'{Urls.base_url}/api/v1/orders/accept/?courierId={courier_id}'

    @staticmethod
    def delete_courier(courier_id):
        return f'{Urls.base_url}/api/v1/courier/{courier_id}'
    
    @staticmethod
    def get_orders_with_limit_and_page(limit=10, page=0):
        return f'{Urls.base_url}/api/v1/orders?limit={limit}&page={page}'
    
    @staticmethod
    def get_orders_with_limit_page_and_station(limit=10, page=0, station="4"):
        return f'{Urls.base_url}/api/v1/orders?limit={limit}&page={page}&nearestStation=["{station}"]'

    @staticmethod
    def get_order_for_courier(courier_id):
        return f'{Urls.base_url}/api/v1/orders?courierId={courier_id}'
    
    @staticmethod
    def get_order_for_courier_with_station(courier_id):
        return f'{Urls.base_url}/api/v1/orders?courierId={courier_id}&nearestStation=["4", "2"]'
    
    @staticmethod
    def get_order_by_track(track):
        return f'{Urls.base_url}/api/v1/orders/track?t={track}'
    
    @staticmethod
    def cancel_order_by_track(track):
        return f'{Urls.base_url}/api/v1/orders/cancel?track={track}'
    
    @staticmethod
    def finish_order_by_id(order_id):
        return f'{Urls.base_url}/api/v1/orders/finish/{order_id}'
    
order_list_urls = [
    Urls.get_orders,
    Urls.get_orders_with_limit_and_page(),
    Urls.get_orders_with_limit_page_and_station()
]   
   
order_list_urls_for_courier = [
    f'{Urls.base_url}/api/v1/orders?courierId={{courier_id}}',
    f'{Urls.base_url}/api/v1/orders?courierId={{courier_id}}&nearestStation=["4", "2"]'
]
