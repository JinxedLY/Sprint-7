import allure
import pytest
from stuff.methods import CourierMethods
from stuff.test_data import RealHumans, APIResponses

class TestCourierLoginAPI:
    @allure.title("Проверки возможности логина с валидными данными")
    @allure.description("Создаем курьера, логинимся под этим курьером")
    def test_courier_login_valid_data_success(self):
        payload = RealHumans.create_real_courier()
        CourierMethods.courier_create(payload)
        del payload["first_name"]
        courier_login = CourierMethods.courier_login(payload)
        CourierMethods.courier_delete(payload)
        assert courier_login.status_code == 200 and APIResponses.Courier_Login_Success in courier_login.json()

    @pytest.mark.parametrize("missing_field", ["password", "login"])
    @allure.title("Проверка невозможности логина при отсутствующем обязательном поле")
    @allure.description("Создаем курьера, дропаем логин или пасс из запроса, пробуем логин")
    def test_courier_login_missing_value_failure(self, missing_field):
        payload = RealHumans.create_real_courier()
        CourierMethods.courier_create(payload)
        del payload["first_name"]
        del payload[missing_field]
        courier_login = CourierMethods.courier_login(payload)
        CourierMethods.courier_delete(payload)