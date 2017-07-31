# -*- coding: utf-8 -*-
import argparse
import os
from insta_browser import browser
import configure

parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--chrome', help='using Chrome webdriver instead of PhantomJS', action="store_true")
parser.add_argument('--count', help='if indicated, like posts by count', type=int, default=0)
args = parser.parse_args()
debug = args.debug
chrome = args.chrome
count = args.count

login = os.environ.get('insta_login')
password = os.environ.get('insta_password')

br = browser.Browser(
    debug=debug,
    chrome=chrome,
    cookie_path=configure.COOKIE_PATH,
    log_path=configure.LOG_PATH,
    exclude=configure.exclude,
    db_path=configure.DB_PATH,
)
try:
    br.auth(login, password)
    br.process_feed(count)
    print(br.get_summary())
finally:
    br.close_all()
