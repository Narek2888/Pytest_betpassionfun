from Main.page_objects import HomePage as h
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium.webdriver.chrome.options import Options
from Main.config import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """open main page"""
    def main_page(self):
        return self.driver.get(h.mainurl)

    """open tournament page"""
    def tournament_button(self):
        return self.driver.find_element(By.XPATH, h.tournamentbutton_xpath)
   
    """open guide page"""
    def guide_button(self):
        return self.driver.find_element(By.XPATH, h.guidebutton_xpath)

    """open news page"""
    def news_button(self):
        return self.driver.find_element(By.XPATH, h.newsbutton_xpath)

    """open rules page"""
    def rules_button(self):
        return self.driver.find_element(By.XPATH, h.rulesbutton_xpath)

    """click the homepage logo"""
    def home_betpassionfun(self):
        return self.driver.find_element(By.XPATH, h.homelogo_xpath)
    
    """open login page"""
    def login_button(self):
        return self.driver.find_element(By.XPATH, h.loginbutton_xpath)
    
    """open register page"""
    def register_button(self):
        return self.driver.find_element(By.XPATH, h.registerbutton_xpath)        
    
    """click 1000pp suggestion button"""
    def suggestion_1000pp_button(self):
        return self.driver.find_element(By.XPATH, h.suggest1000pp_xpath)


    ### social links
    """click facebook icon"""
    def facebook_button(self):
        return self.driver.find_element(By.XPATH, h.facebookicon_xpath)

    """click instagram icon"""
    def insta_button(self):
        return self.driver.find_element(By.XPATH, h.instaicon_xpath)

    """click telegram icon"""
    def telegram_button(self):
        return self.driver.find_element(By.XPATH, h.telegramicon_xpath)

    """click youtube icon"""
    def youtube_button(self):
        return self.driver.find_element(By.XPATH, h.youtubeicon_xpath)

    
    ### footer legal aspects
    """click cookie policy button"""
    def cookie_policy(self):
        return self.driver.find_element(By.XPATH, h.cookie_policy_xpath)

    """click privacy policy button"""
    def privacy_policy(self):
        return self.driver.find_element(By.XPATH, h.privacy_policy_xpath)

    """click terms and conditions button"""
    def terms_and_conditions(self):
        return self.driver.find_element(By.XPATH, h.terms_and_conditions_xpath)


    ### footer menu list
    """open tournament page"""
    def menu_tournament_button(self):
        return self.driver.find_element(By.XPATH, h.menu_tournamentbutton_xpath)
   
    """open guide page"""
    def menu_guide_button(self):
        return self.driver.find_element(By.XPATH, h.menu_guidebutton_xpath)

    """open news page"""
    def menu_news_button(self):
        return self.driver.find_element(By.XPATH, h.menu_newsbutton_xpath)

    """open rules page"""
    def menu_rules_button(self):
        return self.driver.find_element(By.XPATH, h.menu_rulesbutton_xpath)