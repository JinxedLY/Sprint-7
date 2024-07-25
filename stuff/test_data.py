from faker import Faker


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
    Insufficient_Data_Error = "Недостаточно данных для создания учетной записи"
    Courier_Login_Success = "id"
