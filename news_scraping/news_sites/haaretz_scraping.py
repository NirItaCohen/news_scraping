from selenium.webdriver.common.by import By

from news_scraping.services.selenium_webdriver import Webdriver
from news_scraping.services.data_creation_methods import DataCreationMethods


class Haaretz():

    def __init__(self):
        self.haaretz_driver = Webdriver()
        self.data_methods = DataCreationMethods()
        self.haaretz_sub_article_list = []

    def extract_haaretz(self):
        pass