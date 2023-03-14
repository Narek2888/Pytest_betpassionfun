from distutils.command.config import config
from Main.Pages.LoginPage import LoginPage
from Main.Pages.BasePage import BasePage
from Main import data 
from Main.config import *
import time
from selenium.webdriver.common.by import By

bp = BasePage(driver)
lp = LoginPage(driver)


class Login:

    def correct_login(self):

        bp.main_page()
        bp.login_button().click()
        lp.username().send_keys(data.username2)
        lp.password().send_keys(data.password2)
        lp.login2().click()

        try:
            element_to_be_clickable(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/div/button').click()
        except:
            element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/div/i').click()
    
    def incorrect_login(self):

        bp.main_page()
        bp.login_button().click()
        lp.username().send_keys(data.invalid_username)
        lp.password().send_keys(data.invalid_password)
        lp.login2().click()

    def google_account_login(self):

        bp.main_page()
        bp.login_button().click()
        lp.google_account().click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        lp.google_mail_field().send_keys(data.google_account_mail)
        time.sleep(2)
        lp.google_nextbutton1().click()
        time.sleep(2)
        lp.google_password_field().send_keys(data.google_account_password)
        time.sleep(2)
        lp.google_nextbutton2().click()
