# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import argparse
import pickle
import pprint
import os

parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--chrome', help='using Chrome webdriver instead of PhantomJS', action="store_true")
args = parser.parse_args()
debug = args.debug
chrome = args.chrome

class browser:
    """docstring for browser."""

    def __init__(self, debug = False, chrome = False ):
        if chrome:
            self.chrome = chrome
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.PhantomJS()
            self.browser.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
            self.resourceRequestedLogic()
        self.mouse = ActionChains(self.browser)
        self.debug = debug


    def clearDriverCache(self):
        self.browser.execute('executePhantomScript', {'script': '''
            var page = this;
            page.clearMemoryCache();
        ''', 'args': []})

    def resourceRequestedLogic(self):
        self.browser.execute('executePhantomScript', {'script': '''
            var page = this;
            page.onResourceRequested = function(request, networkRequest) {
                if (/\.(jpg|jpeg|png|mp3|css|mp4)/i.test(request.url))
                {
                    //console.log('Final with css! Suppressing image: ' + request.url);
                    networkRequest.abort();
                    return;
                }
            }
        ''', 'args': []})

    def auth(self, login, password):
        br = self.browser
        self.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        try:
            self.log('try to auth with cookies')
            cookies = pickle.load(open('var/cookies/{}.pkl'.format(login), "rb"))
            for cookie in cookies:
                br.add_cookie(cookie)

        except:
            self.log('regular login')
            login_field = br.find_element_by_name("username")
            login_field.clear()
            self.log(u'Login fill')
            login_field.send_keys(login)
            password_field = br.find_element_by_name("password")
            password_field.clear()
            self.log(u'Password fill')
            password_field.send_keys(password)
            submit = br.find_element_by_css_selector("form button")
            self.log(u'Form submit')
            submit.submit()
            time.sleep(3)
            pickle.dump([br.get_cookie('sessionid')], open('var/cookies/{}.pkl'.format(login), "wb"))
            self.log('auth complete')
        br.refresh()

    def get(self, url):
        self.browser.get(url)
        self.log(u'Open ' + self.browser.current_url)

    def closeAll(self):
        self.browser.close()
        self.browser.quit()
        self.log(u'Browser process was ended')
        self.log(u'')

    def scrollToLastUnliked(self):
        while not len(self.browser.find_elements_by_css_selector('.coreSpriteLikeHeartFull')):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # pprint.pprint(len(self.browser.find_elements_by_css_selector('.coreSpriteLikeHeartFull')))
            self.log('scroll down')

    def likeFoundPosts(self):
        br = self.browser
        articles = br.find_elements_by_tag_name('article')
        for post in articles:
            self.mouse.move_to_element(post).perform()
            time.sleep(1)
            heart = post.find_element_by_css_selector('div:nth-child(3) section a:first-child')
            if 'coreSpriteLikeHeartOpen' in heart.find_element_by_css_selector('span').get_attribute("class"):
                self.log('need to be liked ♥️')
                self.mouse.move_to_element(heart).perform()
                heart.click()
            else:
                self.log('no need to be liked 🍔')

    def log(self, text):
        if self.debug:
            print(text)


login = os.environ.get('insta_login')
password = os.environ.get('insta_password')


br = browser(debug, chrome)
try:
    br.auth(login, password)
    br.scrollToLastUnliked()
    br.likeFoundPosts()
finally:
    br.closeAll()
