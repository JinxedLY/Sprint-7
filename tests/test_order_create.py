import allure
import pytest
from stuff.methods import OrderMethods
from stuff.test_data import RealHumans, APIResponses


class TestOrderCreateAPI:
    @pytest.mark.parametrize("colour_value", ["[GREY]", "[BLACK]", "[GREY], [BLACK]", ""])
    @allure.title("Проверка возможности создания заказа с наборами опицонального поля 'Цвет'")
    @allure.description("Создаем заказ, перебираем все возможные варианты поля для передачи цвета. Ожидаем успех")
    def test_order_create_parametized_colour_success(self, colour_value):
        order = RealHumans.create_real_order()
        order["color"] = [colour_value]
        order_response = OrderMethods.order_create(order)
        assert order_response.status_code == 201 and APIResponses.Order_Create_Success in order_response.json()
