import allure
from stuff.methods import OrderMethods
from stuff.test_data import APIResponses


class TestOrderFetchAPI:
    @allure.title("Проверяем запрос на список заказов, ожидается возвращение массива объектов на запрос")
    @allure.description("Дергаем ручку, ждем что в ответ вернутся заказы")
    def test_order_fetch_success(self):
        order_list = OrderMethods.order_fetch()
        assert order_list.status_code == 200 and APIResponses.Order_Fetch in order_list.json()
