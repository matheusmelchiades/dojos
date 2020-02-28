#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Exemplo de model aplicar a regra de negocio necessaria, manipulando os dados externos
    e integrando a camada de acesso ao banco de dados
"""

import dao as dao_users
import dao as dao_posts


def get_users(conditionals):

    if (conditionals):

        return dao_users.get_users()

    return []


def get_posts_by_users():

    allUsers = dao_users.getUsers()

    for user in allUsers:
        user['posts'] = dao_posts.get_posts_by_user(user)

    return allUsers
