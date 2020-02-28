from requests import request
from config import SERVER

URL_SERVER = f"http://{SERVER['host']}:{SERVER['port']}"


def main_home():

    response = request('GET', URL_SERVER).json()

    assert 'status' in response
    assert response['status'] == 'RUNNNING'

def test_answer():
    main_home()
