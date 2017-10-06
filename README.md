# Instagram bot 😎
![phantom](https://user-images.githubusercontent.com/4619899/27839319-0384f6a2-60f9-11e7-84f8-98b078e58855.gif)

## NEED TO KNOW:
Always use latest version of **[insta_browser](https://github.com/aLkRicha/insta_browser)** [![PyPI](https://img.shields.io/pypi/v/insta_browser.svg)](https://pypi.python.org/pypi/insta_browser) package

## Requirements
* python 2.7/3
* virtualenv
* ChromeDriver (‼️) intsa_browser package removed phantomjs support 🆘

## Installation:
```
virtualenv env -p $(which python3) --no-wheel --no-setuptools
env/bin/pip install -r requirements.txt
```

## Upgrade
After each `git pull` run command to update packages from requirements:   
`env/bin/pip install -r requirements.txt --upgrade`

## Usage
#### Feed liker 📃
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_my_feed.py
```
`--debug`  - use for getting debug information in console
`--count 10` - for liking just 10 posts from feed  

Like posts until last liked.

#### User profile liker 👶
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_username.py
```
`--username wakecupbar` - indication what username profile to like **(required)**  
`--debug`  - use for getting debug information in console
`--count 10` - for liking just 10 posts from profile  

Like posts from user profile.

#### Location liker 📍
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_location.py
```
`--location 212898659/kyiv-ukraine/` - indication what username profile to like **(required)**  
`--debug`  - use for getting debug information in console
`--count 10` - for liking just 10 posts from profile  

Like posts from location.

#### Tag liker #️⃣
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_tag.py
```
`--tag python` - indication what tag to like **(required)**  
`--debug`  - use for getting debug information in console
`--count 10` - for liking just 10 posts from profile  

Like posts from tag.
