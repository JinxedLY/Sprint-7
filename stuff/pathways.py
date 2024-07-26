class Pathways:
    base_path = "https://qa-scooter.praktikum-services.ru/"  # головняк
    courier_create = base_path + "api/v1/courier"  # создание курьера
    courier_login = base_path + "api/v1/courier/login"  # логин из-под курьера
    courier_delete = base_path + "api/v1/courier/"  # удаление курьера
    order_create = base_path + "api/v1/orders"  # создание заказа
    order_fetch = base_path + "api/v1/orders"  # получение списка заказов
