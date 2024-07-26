import allure
import pytest
from stuff.methods import CourierMethods
from stuff.test_data import RealHumans, APIResponses


class TestCourierCreateAPI:
    @allure.title("Проверка успешного создания курьера с рандомным набором данных")
    @allure.description("Тест создает нового курьера, используя рандомный набор данных, проверяет успешность операции и удаляет курьера пост-фактум")
    def test_create_new_courier_random_data_success(self, courier_make):
        courier = CourierMethods.courier_create(courier_make)
        assert courier.status_code == 201 and APIResponses.Courier_Create_Success in courier.json()

    @allure.title("Проверка невозможности создания второго курьера используя данные существующего курьера")
    @allure.description("Тест создает нового курьера, используя рандомный набор данных. Повторяет этот же запрос с идентичным набором данных, проверяет отсутствие создания курьера на второй запросе и удаляет курьера пост-фактум")
    def test_create_duplicate_courier_duplicate_data_failure(self, courier_make):
        CourierMethods.courier_create(courier_make)
        courier = CourierMethods.courier_create(courier_make)
        assert courier.status_code == 409 and courier.json()['message'] == APIResponses.Duplicate_Courier_Error

    @pytest.mark.parametrize("missing_field", ["password", "login", "first_name"])
    @allure.title("Проверка невозможности создания курьера без передачи обязательного поля")
    @allure.description("Пытаемся создать курьера, но не передаем одно из обязательных полей")
    def test_create_courier_without_password_failure(self, missing_field):
        payload = RealHumans.create_real_courier()
        del payload[missing_field]
        courier = CourierMethods.courier_create(payload)
        assert courier.status_code == 400 and courier.json()['message'] == APIResponses.Insufficient_Data_Error
