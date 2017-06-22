# -*- coding: utf-8 -*-
import argparse
import os
from insta_browser import browser


parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--chrome', help='using Chrome webdriver instead of PhantomJS', action="store_true")
args = parser.parse_args()
debug = args.debug
chrome = args.chrome

login = os.environ.get('insta_login')
password = os.environ.get('insta_password')

br = browser.Browser(debug, chrome, 'var/cookies')
try:
    br.auth(login, password)
    br.scroll_feed_to_last_not_liked()
    br.like_found_posts()
finally:
    print(br.get_summary())
    br.close_all()