#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#
import time


def test_petfriends(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open PetFriends base page:
    selenium.get("https://petfriends1.herokuapp.com/")

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()
    
    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element_by_id("email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("isaid.zx@gmail.com")

    field_pass = selenium.find_element_by_id("pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("qwerty1234")
    
    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()


  #  time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:


    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result_petfriends.png')

def save_cookie(selenium, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(selenium.get_cookies(), filehandler)
