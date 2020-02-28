#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Exemplo de entidade para manipulação de dados entre a aplicação 
    e o banco de dados
"""

DATA = [
    {'id': 1, 'name': 'Matheus Maciel'}
]


class Person:

    def __init__(self):
        self.data = DATA

    def append_person(self, person):
        self.data.appen(person)

    def get_person_by_name(self, name):
        return [person if person['name'] == name else None for person in self.data]
