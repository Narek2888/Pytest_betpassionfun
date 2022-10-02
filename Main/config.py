from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def element_to_be_clickable(locator, value):

    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((locator, value)))


def url_to_be(url):

    return WebDriverWait(driver, 10).until(EC.url_to_be(url))


def presence_of_element_located(locator, value):

    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((locator, value)))