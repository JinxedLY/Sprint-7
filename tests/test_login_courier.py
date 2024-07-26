import allure
import pytest
from stuff.methods import CourierMethods
from stuff.test_data import FakeHuman, RealHumans, APIResponses

class TestCourierLoginAPI:
    @allure.title("Проверки возможности логина с валидными данными")
    @allure.description("Создаем курьера, логинимся под этим курьером")
    def test_courier_login_valid_data_success(self, courier_make):
        CourierMethods.courier_create(courier_make)
        courier_login = CourierMethods.courier_login(courier_make)
        assert courier_login.status_code == 200 and APIResponses.Courier_Login_Success in courier_login.json()

    @pytest.mark.parametrize("missing_field", ["password", "login"])
    @allure.title("Проверка невозможности логина при отсутствующем обязательном поле")
    @allure.description("Создаем курьера, дропаем логин или пасс из запроса, пробуем логин")
    def test_courier_login_missing_value_failure(self, missing_field, courier_make):
        incomplete_payload = courier_make.copy()
        incomplete_payload.pop(missing_field, None)
        courier_login = CourierMethods.courier_login(incomplete_payload)
        assert courier_login.status_code == 400 and courier_login.json()['message'] == APIResponses.Data_Courier_Login_Error

    @pytest.mark.parametrize("altered_field", ["password", "login"])
    @allure.title("Проверка невозможности логина при некорректно переданном значении пароля либо логина")
    @allure.description("Создаем курьера, подменяем логин или пасс на другое значение, пробуем логин")
    def test_courier_login_malformed_data_failure(self, altered_field, courier_make):
        altered_payload = courier_make.copy()
        existing_value = altered_payload[altered_field]
        new_value = existing_value + "12"
        altered_payload[altered_field] = new_value
        courier_login = CourierMethods.courier_login(altered_payload)
        assert courier_login.status_code == 404 and courier_login.json()['message'] == APIResponses.Data_Courier_Login_Malformed

    @allure.title("Проверка невозможности логина при передаче в принципе несуществующей пары данных логин-пароль")
    @allure.description("Передаем юзера, которого нет. Ожидаем фейл")
    def test_courier_login_nonexistant_courier_failure(self):
        courier_login = CourierMethods.courier_login(FakeHuman.payload)
        assert courier_login.status_code == 404 and courier_login.json()['message'] == APIResponses.Data_Courier_Login_Malformed
