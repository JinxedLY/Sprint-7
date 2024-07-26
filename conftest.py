import pytest
import requests
from stuff.pathways import Pathways
from stuff.test_data import RealHumans


@pytest.fixture
def courier_make():
    courier_payload = RealHumans.create_real_courier()
    yield courier_payload
    try:
        courier_login = requests.post(Pathways.courier_login, json=courier_payload)
        courier_login.raise_for_status()
        courier_id = courier_login.json().get('id')
        if courier_id:
            requests.delete(f"{Pathways.courier_delete}{courier_id}")
    except requests.exceptions.RequestException as e:
        print(f"Не смог удалить курьера: {e}")
