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
        fetch_id = requests.post(Pathways.courier_login, json=payload)
        courier_id = fetch_id.json()['id']
        requests.delete(Pathways.courier_delete + str(courier_id))

    @staticmethod
    @allure.step("Залогиниться под курьером")
    def courier_login(payload):
        response = requests.post(Pathways.courier_login, json=payload)
        return response
