#!/bin/python3

from requests import request
import json
from os import path, mkdir

CHARACTER_URL = 'https://rickandmortyapi.com/api/character'
LOCATIONS_URL = 'https://rickandmortyapi.com/api/location'
EPSODIES_URL = 'https://rickandmortyapi.com/api/episode'


def getFullData(url, results=[]):

    response = request('GET', url).json()

    results = results + response['results']

    print(f"GET DATA {len(results)} OF {response['info']['count']}")

    if response['info']['next']:

        return getFullData(response['info']['next'], results)
    else:

        print('############')
        print(url)
        print('GET ALL DATA WITH SUCCESS')
        print('############')

        return results


def formatData(items=[]):

    for item in items:

        if 'characters' in item:
            item['characters'] = getIds(item['characters'])

        if 'residents' in item:
            item['residents'] = getIds(item['residents'])

        if 'episode' in item and type(item['episode']) is list:
            item['episode'] = getIds(item['episode'])

        if 'location' in item and type(item['location']) is dict:
            string_id = item['location']['url'].split('/')[-1]
            item['location'] = int(string_id) if len(string_id) > 0 else None

        if 'origin' in item and type(item['origin']) is dict:
            string_id = item['origin']['url'].split('/')[-1]
            item['origin'] = int(string_id) if len(string_id) > 0 else None

        del item['url']

    return items


def getIds(items):
    return list(map(lambda x: int(x.split('/')[-1]), items))


def saveData(name, data):

    if not path.exists('./data'):
        mkdir('./data')

    with open(f'./data/{name}.json', 'w+', encoding='utf-8') as file:
        json.dump(data, file, sort_keys=True, indent=4)


if __name__ == "__main__":
    characters = getFullData(CHARACTER_URL)
    characters = formatData(characters)
    saveData('characters', characters)

    locations = getFullData(LOCATIONS_URL)
    locations = formatData(locations)
    saveData('locations', locations)

    epsodies = getFullData(EPSODIES_URL)
    epsodies = formatData(epsodies)
    saveData('episodies', epsodies)
