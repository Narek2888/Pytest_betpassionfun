from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(By.ID, 'username')

    def password(self):
        return self.driver.find_element(By.ID, 'password')

    def show_password(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[2]/span')

    def forgot_password(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[3]/span')

    def login2(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/form/div[4]/button')

    def google_account(self):
        return self.driver.find_element(By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-MJoBVe')

    def free_registration_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/button')

    def google_mail_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')

    def google_nextbutton1(self):
        return self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')

    def google_password_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')

    def google_nextbutton2(self):
        return self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')

    def google_confirmbutton(self):
        return self.driver.find_element(By.XPATH, '//*[@id="confirm_yes"]/div[2]')
