from requests import request
from config import SERVER

URLS = {
    'API': f"http://{SERVER['host']}:{SERVER['port']}/location",
    'API_BY_ID': f"http://{SERVER['host']}:{SERVER['port']}/location/" + "{ID}"
}


def assert_all_location_properties(item):

    assert 'created' in item
    assert 'dimension' in item
    assert 'id' in item
    assert 'name' in item
    assert 'residents' in item
    assert 'type' in item


def get_location():

    response = request('GET', URLS['API']).json()

    assert len(response) > 0

    for item in response:
        assert_all_location_properties(item)


def get_location_by_id():
    locations = request('GET', URLS['API']).json()[:20]

    assert len(locations) > 0

    for item in locations:
        item_id = str(item['id'])
        location = request('GET', URLS['API_BY_ID'].format(ID=item_id)).json()

        assert_all_location_properties(location)


def test_answer():
    get_location()
    get_location_by_id()
