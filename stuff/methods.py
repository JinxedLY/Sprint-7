import allure
import requests
from stuff.pathways import Pathways


class CourierMethods:
    @staticmethod
    @allure.step("Создать курьера")
    def courier_create(payload):
        response = requests.post(Pathways.courier_create, json=payload)
        return response

    @staticmethod
    @allure.step("Удалить курьера")
    def courier_delete(payload):
        try:
            fetch_id = requests.post(Pathways.courier_login, json=payload)
            fetch_id.raise_for_status()
            courier_id = fetch_id.json().get('id')
            if courier_id:
                requests.delete(f"{Pathways.courier_delete}{courier_id}")
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Не смог удалить курьера: {e}")

    @staticmethod
    @allure.step("Залогиниться под курьером")
    def courier_login(payload):
        response = requests.post(Pathways.courier_login, json=payload)
        return response
