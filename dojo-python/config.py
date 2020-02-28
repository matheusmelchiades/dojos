#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Matheus Maciel Melchiades
Email: matheusmacielmelchiades@hotmail.com
Description: Config file.
"""
import os

os.environ['FLASK_ENV'] = 'development'

SERVER = {
    'host': 'localhost',
    'port': 5000,
    'debug': True
}
