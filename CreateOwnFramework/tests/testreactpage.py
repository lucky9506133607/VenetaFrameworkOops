import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from utilities.Baseclass import BaseClass
from PageObject.mainproduct_ReactPage import MainProduct_ReactPage
from PageObject.MainPage import MainPage


conftest.setup("chrome")

class TestReactPage(BaseClass):
    flag = 0
    def chooseProduct(self):
        BaseClass.verifyLinkPresence(self, "//*[@id='shopify-section-header']/header/div/div/div[2]/a")
        
        #----------------------------------------------- MainPage -----------------------------------------
        design_your_own = MainPage(self.driver)
        design_your_own.getMainProduct().click()

        #----------------------------------------------- MainProduct -----------------------------------------
        BaseClass.verifyLinkPresence(self, "//div[1]/div[2]/ul[1]/li[1]")
        mainproduct = MainProduct_ReactPage(self.driver)
        mainproduct.getMainProduct().click()
        BaseClass.scrollbar()
        
    #----------------------------------------------- MainProduct -----------------------------------------
    
    Honeycomb_product_count = driver.find_elements(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li")
    for i in range(1, len(Honeycomb_product_count)+1):
        choose_product = driver.find_element(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li["+str(i)+"]")
        copy_choose_product = choose_product
        choose_product.click()
        print(choose_product.get_attribute("data-target-list-handle"))
        _continue = driver.find_element(By.XPATH,"//div[2]/div[2]/div[2]/div")
        _continue.click() 
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]")))
        Material_options = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div")
        for i in range(1, len(Material_options)+1):
            get_Sheer_Option = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
            print("//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
            if get_Sheer_Option.get_attribute("title") == "Sheer":
                get_Sheer_Option.click()
                flag=1
                break
            else:
                pass
        if flag == 1:
            _next = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/button[2]")
            _next.click()
            # loop for sheer colors
            sheer_colors_count = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span")
            for i in range(1, len(sheer_colors_count)+1):
                select_color = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span["+str(i)+"]")
                print("color id ====== "+str(i))
                flag = 0
            
        else:
            print("Sheer not available")
        
        driver.get("https://venetablinds.com.au/pages/shop-now?step=1&current=bottom-up&pre=honeycomb-blinds")
    
    
    
    
    
#inheritance concept apply  
"""class TestReactPage(BaseClass):
    flag = 0
    def chooseProduct(self):
        BaseClass.verifyLinkPresence(self, "lucky")
        print("df")

TestReactPage().chooseProduct()"""
    
    
    
    