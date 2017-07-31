# -*- coding: utf-8 -*-
import os

script_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(script_path, 'var')
COOKIE_PATH = os.path.join(var_path, 'cookie')
LOG_PATH = os.path.join(var_path, 'log')
DB_PATH = os.path.join(var_path, 'db')

exclude = open(os.path.join(var_path,  'exclude_accounts.txt')).read().split(',')