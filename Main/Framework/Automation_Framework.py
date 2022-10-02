from Main.Pages.LoginPage import LoginPage
from Main.Pages.BasePage import BasePage
from Main import data 
from Main.config import driver
import time

bp = BasePage(driver)
lp = LoginPage(driver)


class Login:

    def correct_login(self):

        bp.main_page()
        bp.login_button().click()
        lp.username().send_keys(data.username2)
        lp.password().send_keys(data.password2)
        lp.login2().click()
    
    def incorrect_login(self):

        bp.main_page()
        bp.login_button().click()
        lp.username().send_keys(data.invalid_username)
        lp.password().send_keys(data.invalid_password)
        lp.login2().click()

    def google_account_login(self):

        bp.main_page()
        time.sleep(1)
        bp.login_button().click()
        time.sleep(5)
        lp.google_account().click()
        driver.switch_to.window(driver.window_handles[1])
        lp.google_mail_field().send_keys(data.google_account_mail)
        lp.google_nextbutton1().click()
        lp.google_password_field().send_keys(data.google_account_password)
        lp.google_nextbutton2().click()
