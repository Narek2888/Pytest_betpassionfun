import allure
from Main.Pages.LoginPage import LoginPage
from Main.Pages.BasePage import BasePage
from Main import config
from Main.data import *
from Main.Framework.Automation_Framework import Login
import requests
from selenium.webdriver.common.by import By
import pytest


basepage = BasePage(config.driver)
loginpage = LoginPage(config.driver)


@allure.severity(allure.severity_level.NORMAL) #### adding the decorator
def test_correct_login():


    Login().correct_login()

    auth_url = r'https://stagingapi.pokerplaza.com/api_v2/authenticatePlayer'
    params = {
        'username': username2, 
        'password': password2, 
        'skinId': 569450, 
        'parentId': 569450,
    }

    authenticate_request = requests.post(auth_url, params)
    data = authenticate_request.json()

    assert data['result']['wallets'][5]['balance'] == int(config.presence_of_element_located(By.CLASS_NAME, 'fpp__amount').text)
    