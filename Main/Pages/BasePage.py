from selenium.webdriver.common.by import By
from Main import config


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """open main page"""
    def main_page(self):
        return self.driver.get("https://betpassionfun.draft10.com/")

    """open tournament page"""
    def tournament_button(self):
        # return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/ul/li[1]/a')))
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/ul/li[1]/a')

    """open guide page"""
    def guide_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/ul/li[2]/a')

    """open news page"""
    def news_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/ul/li[3]/a')

    """open rules page"""
    def rules_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/ul/li[4]/a')

    """click the homepage logo"""
    def home_betpassionfun(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/img')

    """open login page"""
    def login_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[1]')

    """open register page"""
    def register_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[2]')        

    """click 1000pp suggestion button"""
    def suggestion_1000pp_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/button')

    # social links
    """click facebook icon"""
    def facebook_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]')

    """click instagram icon"""
    def insta_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[2]')

    """click telegram icon"""
    def telegram_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[3]')

    """click youtube icon"""
    def youtube_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[4]')

    # footer legal aspects
    """click cookie policy button"""
    def cookie_policy(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]/a')

    """click privacy policy button"""
    def privacy_policy(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[2]/a')

    """click terms and conditions button"""
    def terms_and_conditions(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span[3]/a')

    # footer menu list
    """open tournament page"""
    def menu_tournament_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]/span')

    """open guide page"""
    def menu_guide_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[2]/span')

    """open news page"""
    def menu_news_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[3]/span')

    """open rules page"""
    def menu_rules_button(self):
        return config.element_to_be_clickable(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a[4]/span')
