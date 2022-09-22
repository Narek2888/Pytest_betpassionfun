from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    def login_button(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(By.XPATH, xpath).click()

    def username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
    
    def login2(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()