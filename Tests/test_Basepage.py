import allure
import time
from Main.Pages.BasePage import BasePage
from Main import config


basepage = BasePage(config.driver)


# adding the decorator
@allure.severity(allure.severity_level.NORMAL)
def test_open_mainpage():

    basepage.main_page()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/"
    time.sleep(1)


"""navigation bar elements"""


def test_tournament_button():

    basepage.tournament_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/tournament"
    time.sleep(1)


def test_guide_button():

    basepage.guide_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/guide"
    time.sleep(1)


def test_news_button():

    basepage.news_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/news"
    time.sleep(1)


def test_rules_button():

    basepage.rules_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/rules"
    time.sleep(1)


def test_home_button():

    basepage.home_betpassionfun().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/"
    time.sleep(1)


def test_login_button():

    basepage.login_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/login"
    time.sleep(1)


def test_register_button():

    basepage.register_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/register"
    time.sleep(1)


def test_suggest_1000pp_button():
    
    basepage.main_page()
    time.sleep(1)
    basepage.suggestion_1000pp_button().click()
    assert config.driver.current_url == 'https://betpassionfun.draft10.com/register'
    time.sleep(1)


"""social links"""


def test_facebook_button():

    basepage.main_page()
    time.sleep(1)
    basepage.facebook_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.facebook.com/NoiSiamoPassione"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


def test_insta_button():

    basepage.insta_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.instagram.com/betpassion.it/"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


def test_telegram_button():

    basepage.telegram_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://t.me/betpassionofficial"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


def test_youtube_button():

    basepage.youtube_button().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.youtube.com/results?search_query=betpassion.info"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])


# footer
"""legal aspects"""


def test_cookie_policy():

    basepage.cookie_policy().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.iubenda.com/privacy-policy/30380830/cookie-policy"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


def test_privacy_policy():

    basepage.privacy_policy().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.iubenda.com/privacy-policy/30380830"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


def test_terms_and_conditions():

    basepage.terms_and_conditions().click()
    config.driver.switch_to.window(config.driver.window_handles[1])
    assert config.driver.current_url == "https://www.iubenda.com/termini-e-condizioni/30380830"
    config.driver.close()
    config.driver.switch_to.window(config.driver.window_handles[0])
    time.sleep(1)


"""menu elements"""


def test_menu_tournament_button():

    basepage.menu_tournament_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/tournament"
    time.sleep(1)


def test_menu_guide_button():

    basepage.main_page()
    basepage.menu_guide_button().click()
    time.sleep(2)
    assert config.driver.current_url == "https://betpassionfun.draft10.com/guide"
    time.sleep(1)


def test_menu_news_button():

    basepage.main_page()
    time.sleep(1)
    basepage.menu_news_button().click()
    assert config.driver.current_url == "https://betpassionfun.draft10.com/news"
    time.sleep(1)


def test_menu_rules_button():

    basepage.main_page()
    basepage.menu_rules_button().click()
    time.sleep(2)
    assert config.driver.current_url == "https://betpassionfun.draft10.com/rules"
    config.driver.quit()
