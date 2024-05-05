from selenium.webdriver.common.by import By

from news_scraping.services.selenium_webdriver import Webdriver
from news_scraping.services.data_creation_methods import DataCreationMethods


class Israelhayom():

    def __init__(self):
        self.israelhayom_driver = Webdriver()
        self.data_methods = DataCreationMethods()
        self.israelhayom_sub_article_list = []

    def extract_israelhayom(self):
        self.israelhayom_driver.driver.get("https://www.israelhayom.co.il/")

        try:
            main_title = self.israelhayom_driver.driver.find_element(By.CSS_SELECTOR,
                                                                     ".posts-octet__post-1> .post-content > hgroup  > "
                                                                     "h3 > a > span").text
            main_author = self.israelhayom_driver.driver.find_element(By.CSS_SELECTOR,
                                                                      ".posts-octet__post-1> .post-content > .post-meta").find_elements(
                By.TAG_NAME, "a").te
        except:
            print("somthing went wrong")
        else:
            self.data_methods.add_list_to_csv(
                [{"title": main_title, "subTitle": main_subtitle, "author": main_author}])
