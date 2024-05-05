from selenium.webdriver.common.by import By

from news_scraping.services.selenium_webdriver import Webdriver
from news_scraping.services.data_creation_methods import DataCreationMethods


class Walla():

    def __init__(self):
        self.walla_driver = Webdriver()
        self.data_methods = DataCreationMethods()
        self.walla_sub_article_list = []

    def extract_walla(self):
        pass
