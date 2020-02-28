from requests import request
from config import SERVER

URLS = {
    'API': f"http://{SERVER['host']}:{SERVER['port']}/character",
    'API_BY_ID': f"http://{SERVER['host']}:{SERVER['port']}/character/" + "{ID}"
}


def assert_all_character_properties(item):

    assert 'created' in item
    assert 'episode' in item
    assert 'gender' in item
    assert 'id' in item
    assert 'image' in item
    assert 'location' in item
    assert 'name' in item
    assert 'origin' in item
    assert 'species' in item
    assert 'status' in item
    assert 'type' in item


def get_character():

    response = request('GET', URLS['API']).json()

    assert len(response) > 0

    for item in response:
        assert_all_character_properties(item)


def get_character_by_id():
    characters = request('GET', URLS['API']).json()[:20]

    assert len(characters) > 0

    for item in characters:
        item_id = str(item['id'])
        character = request('GET', URLS['API_BY_ID'].format(ID=item_id)).json()

        assert_all_character_properties(character)


def test_answer():
    get_character()
    get_character_by_id()
