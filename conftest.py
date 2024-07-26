import pytest
import requests
from stuff.pathways import Pathways
from stuff.test_data import RealHumans


@pytest.fixture
def courier_make():
    courier_payload = RealHumans.create_real_courier()
    yield courier_payload
    del courier_payload["first_name"]
    courier_login = requests.post(Pathways.courier_login, json=courier_payload)
    courier_id = courier_login.json()['id']
    requests.delete(Pathways.courier_delete + str(courier_id))
