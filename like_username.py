# -*- coding: utf-8 -*-
import argparse
import os
from insta_browser import browser

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
COOKIE_PATH = '{}/var/cookie'.format(SCRIPT_PATH)
SCREEN_SHOT_PATH = '{}/var/screenshot'.format(SCRIPT_PATH)
LOGGER_FILE = '{}/var/log/insta_browser.txt'.format(SCRIPT_PATH)

parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--chrome', help='using Chrome webdriver instead of PhantomJS', action="store_true")
parser.add_argument('--count', help='if indicated, like posts by count', type=int, default=None)
parser.add_argument('--username', help='if indicated, like posts by count', type=str, required=True)
args = parser.parse_args()
debug = args.debug
chrome = args.chrome
count = args.count
username = args.username


login = os.environ.get('insta_login')
password = os.environ.get('insta_password')

br = browser.Browser(debug, chrome, COOKIE_PATH, SCREEN_SHOT_PATH, LOGGER_FILE)
try:
    br.auth(login, password)
    br.process_user(username, count)
finally:
    print(br.get_summary())
    br.close_all()
