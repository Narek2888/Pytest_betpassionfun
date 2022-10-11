from email import parser
from pytest import Parser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse


browser = "Chrome"

if browser == "Chrome":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
elif browser == "Firefox":
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
elif browser == "Safari":
    driver = webdriver.Safari()
else:
    print("choose correct browser name")


def element_to_be_clickable(locator, value):

    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((locator, value)))


def url_to_be(url):

    return WebDriverWait(driver, 10).until(EC.url_to_be(url))


def presence_of_element_located(locator, value):

    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((locator, value)))