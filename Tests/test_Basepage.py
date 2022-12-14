from lib2to3.pgen2 import driver
import allure
from Main.Pages.BasePage import BasePage
from Main import config
import pytest


basepage = BasePage(config.driver)


# adding the decorator
@allure.severity(allure.severity_level.NORMAL)
# @pytest.mark.usefixtures("driver_init")
def test_open_mainpage():

    basepage.main_page()
    assert config.url_to_be("https://betpassionfun.draft10.com/")


"""navigation bar elements"""

def test_tournament_button():

    basepage.main_page()
    basepage.tournament_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/tournament")


def test_guide_button():

    basepage.main_page()
    basepage.guide_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/guide")


def test_news_button():

    basepage.main_page()
    basepage.news_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/news")


def test_rules_button():

    basepage.main_page()
    basepage.rules_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/rules")


def test_home_button():

    basepage.main_page()
    basepage.home_betpassionfun().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/")


def test_login_button():

    basepage.main_page()
    basepage.login_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/login")


def test_register_button():

    basepage.main_page()
    basepage.register_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/register")


def test_suggest_1000pp_button():
    
    basepage.main_page()
    basepage.suggestion_1000pp_button().click()
    assert config.url_to_be('https://betpassionfun.draft10.com/register')


"""social links"""


def test_facebook_button():

    basepage.main_page()
    basepage.facebook_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.facebook.com/NoiSiamoPassione")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


def test_insta_button():

    basepage.main_page()
    basepage.insta_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.instagram.com/betpassion.it/")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


def test_telegram_button():

    basepage.main_page()
    basepage.telegram_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://t.me/betpassionofficial")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


def test_youtube_button():

    basepage.main_page()
    basepage.youtube_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.youtube.com/results?search_query=betpassion.info")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


# footer
"""legal aspects"""


def test_cookie_policy():

    basepage.main_page()
    basepage.cookie_policy().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.iubenda.com/privacy-policy/30380830/cookie-policy")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


def test_privacy_policy():

    basepage.main_page()
    basepage.privacy_policy().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.iubenda.com/privacy-policy/30380830")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


def test_terms_and_conditions():

    basepage.main_page()
    basepage.terms_and_conditions().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.url_to_be("https://www.iubenda.com/termini-e-condizioni/30380830")
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


"""menu elements"""


def test_menu_tournament_button():

    basepage.main_page()
    basepage.menu_tournament_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/tournament")


def test_menu_guide_button():

    basepage.main_page()
    basepage.menu_guide_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/guide")


def test_menu_news_button():

    basepage.main_page()
    basepage.menu_news_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/news")


def test_menu_rules_button():

    basepage.main_page()
    basepage.menu_rules_button().click()
    assert config.url_to_be("https://betpassionfun.draft10.com/rules")
