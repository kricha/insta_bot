# -*- coding: utf-8 -*-
import argparse
import os
from insta_browser import browser
import configure

parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--auto_follow', help='Enable auto following', action="store_true")
parser.add_argument('--count', help='if indicated, like posts by count', type=int, default=None)
parser.add_argument('--tag', help='if indicated, like posts by count', type=str, required=True)
args = parser.parse_args()
debug = args.debug
auto_follow = args.auto_follow
count = args.count
tag = args.tag


login = os.environ.get('insta_login')
password = os.environ.get('insta_password')

br = browser.Browser(
    debug=debug,
    cookie_path=configure.COOKIE_PATH,
    log_path=configure.LOG_PATH,
    exclude=configure.exclude,
    db_path=configure.DB_PATH,
    auto_follow=auto_follow
)
try:
    br.auth(login, password)
    br.process_tag(tag, count)
    print(br.get_summary())
finally:
    br.close_all()
