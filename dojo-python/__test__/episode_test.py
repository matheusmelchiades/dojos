from requests import request
from config import SERVER
import __test__.character_test as characterTest

URLS = {
    'API': f"http://{SERVER['host']}:{SERVER['port']}/episode",
    'API_BY_ID': f"http://{SERVER['host']}:{SERVER['port']}/episode/" + "{ID}",
    'API_BY_NAME': f"http://{SERVER['host']}:{SERVER['port']}/episode?name=" + "{NAME}",
    'API_BY_SEASON': f"http://{SERVER['host']}:{SERVER['port']}/episode/season/" + "{SEASON}",
    'API_BY_ID_WITH_CHARACTERS': f"http://{SERVER['host']}:{SERVER['port']}/episode/" + "{ID}/character"
}


def assert_all_episode_properties(item):

    assert 'air_date' in item
    assert 'characters' in item
    assert 'created' in item
    assert 'episode' in item
    assert 'id' in item
    assert 'name' in item


def get_episode():

    response = request('GET', URLS['API']).json()

    assert len(response) > 0

    for item in response:
        assert_all_episode_properties(item)


def get_episode_by_id():

    episodies = request('GET', URLS['API']).json()[:20]

    assert len(episodies) > 0

    for item in episodies:

        assert_all_episode_properties(item)

        item_id = str(item['id'])
        episodie = request('GET', URLS['API_BY_ID'].format(ID=item_id)).json()

        assert_all_episode_properties(episodie)


def get_episode_by_id_with_characters():

    episodies = request('GET', URLS['API']).json()[:20]

    assert len(episodies) > 0

    for item in episodies:
        assert_all_episode_properties(item)

        item_id = str(item['id'])

        episodie = request(
            'GET', URLS['API_BY_ID_WITH_CHARACTERS'].format(ID=item_id)).json()

        for character in episodie['characters']:
            characterTest.assert_all_character_properties(character)


def get_episode_by_name():
    episodies = request('GET', URLS['API']).json()[:20]

    assert len(episodies) > 0

    for item in episodies:

        assert_all_episode_properties(item)

        item_name = item['name'].split

        episodies_search = request(
            'GET', URLS['API_BY_NAME'].format(NAME=item_name)).json()

        for episodie in episodies_search:

            assert_all_episode_properties(episodie)

            assert item['id'] == episodie['id']
            assert item['name'] == episodie['name']
            assert item['created'] == episodie['created']
            assert len(item['characters']) == len(['characters'])


def get_episode_by_season():
    episodies = request('GET', URLS['API']).json()

    seasons = []

    for ep in episodies:

        assert_all_episode_properties(ep)

        season = ep['episode'].split('E')[1:]
        season = list(map(lambda x: int(x), season))[-1]

        episodies_by_season = request(
            'GET', URLS['API_BY_SEASON'].format(SEASON=season)).json()

        for ep_season in episodies_by_season:

            assert_all_episode_properties(ep_season)


def test_answer():

    get_episode()
    get_episode_by_id()
    get_episode_by_name()
    get_episode_by_season()
    get_episode_by_id_with_characters()
