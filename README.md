## Requirements
* python 3
* virtualenv
* chrome or phantomJS web driver

## Installation:
```
virtualenv env -p $(which python3) --no-wheel --no-setuptools
env/bin/pip install -r requirements.txt
```

Download and place binary from archive to bin folder - http://phantomjs.org/download.html

## Upgrade
After each `git pull` run command to update packages from requirements:   
`env/bin/pip install -r requirements.txt --upgrade`

## Usage
#### Feed liker 📃
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_my_feed.py
```
`--debug`  - use for getting debug information in console  
`--chrome` - for using Chrome webdriver instead of PhantomJS  
`--count 10` - for liking just 10 posts from feed  

Like posts until last liked.

#### User profile liker 👶
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_username.py
```
`--username wakecupbar` - indication what username profile to like **(required)**  
`--debug`  - use for getting debug information in console  
`--chrome` - for using Chrome webdriver instead of PhantomJS  
`--count 10` - for liking just 10 posts from profile  

Like posts from user profile.

#### Location liker 📍
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python like_location.py
```
`--location 212898659/kyiv-ukraine/` - indication what username profile to like **(required)**  
`--debug`  - use for getting debug information in console  
`--chrome` - for using Chrome webdriver instead of PhantomJS  
`--count 10` - for liking just 10 posts from profile  

Like posts from location.