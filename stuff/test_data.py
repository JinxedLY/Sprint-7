from faker import Faker


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


class APIResponses:
    Courier_Create_Success = "ok"
    Duplicate_Courier_Error = "Этот логин уже используется"
    Data_Courier_Create_Error = "Недостаточно данных для создания учетной записи"
    Courier_Login_Success = "id"
    Data_Courier_Login_Error = "Недостаточно данных для входа"
    Data_Courier_Login_Malformed = "Учетная запись не найдена"
