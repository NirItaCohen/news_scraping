from selenium.webdriver.common.by import By

from news_scraping.services.selenium_webdriver import Webdriver
from news_scraping.services.data_creation_methods import DataCreationMethods


class Ynet():
    def __init__(self):
        self.ynet_driver = Webdriver()
        self.data_methods = DataCreationMethods()
        self.ynet_sub_article_list = []

    def extract_ynet(self):
        self.ynet_driver.driver.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")

        try:
            main_title = self.ynet_driver.driver.find_element(By.CSS_SELECTOR, "div > a > .slotTitle  > span").text
            main_subtitle = self.ynet_driver.driver.find_element(By.CSS_SELECTOR,
                                                                 "div > a > .slotSubTitle  > span").text
            main_author = self.ynet_driver.driver.find_element(By.CSS_SELECTOR, "div > a > .author").text
        except:
            print("somthing went wrong")
        else:
            self.data_methods.add_list_to_csv(
                [{"title": main_title, "subTitle": main_subtitle, "author": main_author}])

        sub_articles_div = self.ynet_driver.driver.find_element(By.CLASS_NAME, "YnetMultiStripRowsComponenta")
        sub_articles_data = sub_articles_div.find_elements(By.CLASS_NAME, "slotView")

        for sub_article in sub_articles_data:
            self.ynet_sub_article_list.append(
                {
                    "title": sub_article.find_element(By.CLASS_NAME, "slotTitle").find_element(By.TAG_NAME,
                                                                                               "span").text,
                    "subTitle": sub_article.find_element(By.CLASS_NAME, "slotSubTitle").find_element(By.TAG_NAME,
                                                                                                     "span").text,
                    "author": sub_article.find_element(By.CLASS_NAME, "author").text
                })
        self.data_methods.add_list_to_csv(self.ynet_sub_article_list)

        self.ynet_driver.driver.quit()