from selenium.webdriver.common.by import By
from Main import config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return config.presence_of_element_located(By.ID, 'username')

    def password(self):
        return config.presence_of_element_located(By.ID, 'password')

    def show_password(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[2]/span')

    def forgot_password(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[3]/span')

    def login2(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[4]/button')

    def google_account(self):
        return config.element_to_be_clickable(By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-MJoBVe')

    def free_registration_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/button')

    def google_mail_field(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="identifierId"]')

    def google_nextbutton1(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="identifierNext"]/div/button/span')

    def google_password_field(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')

    def google_nextbutton2(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="passwordNext"]/div/button/span')

    def google_confirmbutton(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="confirm_yes"]/div[2]')
