import pytest
import allure
import time
from Main.Pages.LoginPage import LoginPage
from Main.Pages.BasePage import BasePage
from Main.config import *
from Main.page_objects import HomePage as hp

basepage = BasePage(driver)

@allure.severity(allure.severity_level.NORMAL) #### adding the decorator
def test_open_mainpage():

    open_main_page = basepage.main_page()
    assert driver.current_url == hp.mainurl
    time.sleep(1)

"""navigation bar elements"""
def test_tournament_button():

    open_tournament_page = basepage.tournament_button().click()
    assert driver.current_url == hp.tournamentpage_url
    time.sleep(1)

def test_guide_button():

    open_guide_page = basepage.guide_button().click()
    assert driver.current_url == hp.guidepage_url
    time.sleep(1)

def test_news_button():

    open_news_page = basepage.news_button().click()
    assert driver.current_url == hp.newspage_url
    time.sleep(1)

def test_rules_button():

    open_rules_page = basepage.rules_button().click()
    assert driver.current_url == hp.rulespage_url
    time.sleep(1)

def test_home_button():

    open_home_page = basepage.home_betpassionfun().click()
    assert driver.current_url == hp.homepage_url
    time.sleep(1)

def test_login_button():

    open_login_page = basepage.login_button().click()
    assert driver.current_url == hp.loginpage_url
    time.sleep(1)

def test_register_button():

    open_register_page = basepage.register_button().click()
    assert driver.current_url == hp.registerpage_url
    time.sleep(1)


def test_suggest_1000pp_button():
    
    basepage.main_page()
    time.sleep(1)
    open_suggest_1000pp_page = basepage.suggestion_1000pp_button().click()
    assert driver.current_url == hp.registerpage_url
    time.sleep(1)
    
"""social links"""
def test_facebook_button():

    basepage.main_page()
    open_facebook_page = basepage.facebook_button().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.facebookpage_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

def test_insta_button():

    open_insta_page = basepage.insta_button().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.instapage_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

def test_telegram_button():

    open_telegram_page = basepage.telegram_button().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.telegrampage_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)


def test_youtube_button():

    open_youtube_page = basepage.youtube_button().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.youtubepage_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


### footer
"""legal aspects"""
def test_cookie_policy():

    open_cookie_policy = basepage.cookie_policy().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.cookie_policy_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

def test_privacy_policy():

    open_privacy_policy = basepage.privacy_policy().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.privacy_policy_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

def test_terms_and_conditions():

    open_terms_and_conditions = basepage.terms_and_conditions().click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == hp.terms_and_conditions_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)


"""menu elements"""
def test_menu_tournament_button():

    open_menu_tournament_page = basepage.menu_tournament_button().click()
    assert driver.current_url == hp.tournamentpage_url
    time.sleep(1)

def test_menu_guide_button():

    basepage.main_page()
    open_menu_guide_page = basepage.menu_guide_button().click()
    assert driver.current_url == hp.guidepage_url
    time.sleep(1)

def test_menu_news_button():

    basepage.main_page()
    time.sleep(1)
    open_menu_news_page = basepage.menu_news_button().click()
    assert driver.current_url == hp.newspage_url
    time.sleep(1)

def test_menu_rules_button():

    basepage.main_page()
    open_menu_rules_page = basepage.menu_rules_button().click()
    assert driver.current_url == hp.rulespage_url
    time.sleep(1)
    driver.quit()