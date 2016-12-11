#!/usr/bin/python

import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os
import logging
from datetime import datetime
from datetime import date
from random import sample
LOG_FILENAME="Error.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
file_name=r"investorsForum.txt"

def openNewTab(driver,link):
    text_sum=""
    page=1
    driver.execute_script("window.open('"+link+"');")
    driver.switch_to_window(driver.window_handles[-1])
    try:
        page_max=int(driver.find_elements_by_xpath("//div[@class='pagesection']/div[@class='pagelinks floatleft']/a[@class='navPages']")[-1].text)
    except:
        page_max=1

    #for page in range(1,2):
    for page in range(1,page_max+1):
        sleep(0.05)
        for element2 in driver.find_elements_by_xpath("//div[@class='inner']"):#for every text block element  
            text_sum+=element2.text
        
        page_num_elements=driver.find_elements_by_xpath("//div[@class='pagelinks floatleft']/a[@class='navPages']")
        for page_num_element in page_num_elements:
            if int(page_num_element.text)>page:
                action = webdriver.common.action_chains.ActionChains(driver)
                action.move_to_element(page_num_element)
                action.click().perform()
                break
    driver.close() 
    driver.switch_to_window(driver.window_handles[0])
    with open(file_name,"a+") as f:
        f.write(text_sum.encode('gbk','replace').decode('utf-8','ignore'))

class Scrape():
    def test(self):
        test_instance1=ScrapeInvestor()
        test_instance1.setUp()
        test_instance1.testLinks()
        test_instance1.tearDown()

class ScrapeInvestor():
    def setUp(self):
        path=os.path.join(os.path.dirname(__file__),"webdriver","chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=path)
        self.url="http://forum.lendacademy.com/index.php/board,4.NUM.html"#NUM is 0,20,40,etc.

    def testLinks(self):
        driver = self.driver
        driver.get(self.url.replace("NUM","0"))
        for i in range(0,1640,20):
            link=self.url.replace("NUM",str(i))
            driver.execute_script("window.open('"+link+"');")
            driver.switch_to_window(driver.window_handles[-1])
            Link=lambda driver: driver.find_elements_by_xpath("//table[@class='table_grid']/tbody/tr/td/div/span/a")
            link_list=[i.get_attribute("href") for i in Link(driver)]
            for j in link_list:
                openNewTab(driver,j)
            driver.close() 
            driver.switch_to_window(driver.window_handles[0])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    a=Scrape()
    a.test()
    
