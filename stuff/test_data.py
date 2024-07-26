from faker import Faker
import random


class FakeHuman:
    payload = {
        "login": "UniqueValue109",
        "password": "UniqueValue198"
    }


class RealHumans:
    @staticmethod
    def create_real_courier():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        return payload

    @staticmethod
    def create_real_order():
        fake = Faker()
        firstname = fake.first_name()
        lastname = fake.last_name()
        address = fake.address()
        metro = random.randint(1, 5)
        phone = fake.phone_number()
        rent = random.randint(1, 5)
        date = "2024-08-08"
        comment = fake.company()
        payload = {
            "firstName": firstname,
            "lastName": lastname,
            "address": address,
            "metroStation": metro,
            "phone": phone,
            "rentTime": rent,
            "deliveryDate": date,
            "comment": comment,
        }
        return payload


class APIResponses:
    Courier_Create_Success = "ok"
    Duplicate_Courier_Error = "Этот логин уже используется"
    Data_Courier_Create_Error = "Недостаточно данных для создания учетной записи"
    Courier_Login_Success = "id"
    Data_Courier_Login_Error = "Недостаточно данных для входа"
    Data_Courier_Login_Malformed = "Учетная запись не найдена"
    Order_Create_Success = "track"
