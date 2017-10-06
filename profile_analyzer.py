# -*- coding: utf-8 -*-
import argparse
from insta_browser import InstaMeter

parser = argparse.ArgumentParser()
parser.add_argument('--username', help='set for indicating what profile we need to analyze', type=str, required=True)
args = parser.parse_args()
username = args.username


def callback(text):
    print(text)


im = InstaMeter(username=username, callback=callback)
res = im.analyze_profile()
im.print_account_statistic()
im.print_top_liked()
im.print_top_commented()
im.print_top_viewed()
