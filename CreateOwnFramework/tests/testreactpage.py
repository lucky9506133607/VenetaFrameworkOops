import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import Conftest
from utilities.Baseclass import BaseClass
from PageObject.mainproduct_ReactPage import MainProduct_ReactPage
from PageObject.MainPage import MainPage
from PageObject.subproduct_ReactPage import subproduct_ReactPage
from PageObject.selectmaterial_ReactPage import selectmaterial_ReactPage
from PageObject.colour_ReactPage import colour_ReactPage


obj = Conftest
obj.setup("chrome")

class TestReactPage(BaseClass):
    flag = 0

    def chooseProduct(self):
        BaseClass.verifyLinkPresence("//*[@id='shopify-section-header']/header/div/div/div[2]/a")
        
        #----------------------------------------------- MainPage -----------------------------------------
        design_your_own = MainPage(self.driver)
        design_your_own.getMainProduct().click()

        #----------------------------------------------- MainProduct -----------------------------------------
        BaseClass.verifyLinkPresence("//div[1]/div[2]/ul[1]/li[1]")
        mainproduct_obj = MainProduct_ReactPage(self.driver)
        mainproduct_obj.getMainProduct().click()
        BaseClass.scrollbar("continue")
        
        
    #----------------------------------------------- subproducts -----------------------------------------
    
        subproduct_ReactPage_obj = subproduct_ReactPage()
        Honeycomb_product_count = subproduct_ReactPage_obj.countSubProducts()
    
        for i in range(1, len(Honeycomb_product_count)+1):
            choose_product = subproduct_ReactPage_obj.get_SubProduct(i)
            copy_choose_product = choose_product
            choose_product.click()
            print(subproduct_ReactPage_obj.get_SubProductName(i))
            BaseClass.scrollbar("continue")
            
            #------------------------------------------- Material -------------------------------------------
            
            BaseClass.verifyLinkPresence("//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]")
            
            #Material_options = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div")
            selectmaterial_ReactPage_obj = selectmaterial_ReactPage(self.driver)
            Material_options = selectmaterial_ReactPage_obj.countMaterialOptions()
            
            
            for i in range(1, len(Material_options)+1):
                #get_Sheer_Option = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
                get_Sheer_Option = selectmaterial_ReactPage_obj.get_MaterialName(i)
                print("//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
                
                if get_Sheer_Option.get_attribute("title") == "Sheer":
                    get_Sheer_Option.click()
                    self.flag=1
                    break
                else:
                    pass
            if self.flag == 1:
                #_next = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/button[2]")
                BaseClass.scrollbar("next")
                
                #---------------------------------------  loop for sheer colors ----------------------------
                
                #sheer_colors_count = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span")
                colour_ReactPage_obj = colour_ReactPage(self.driver)
                sheer_colors_count = colour_ReactPage_obj.countColourOptions()
                for i in range(1, len(sheer_colors_count)+1):
                    select_color = colour_ReactPage_obj.select_ColourOption(i)
                    print("color id ====== "+str(i))
                    flag = 0
                
            else:
                print("Sheer not available")
            
            #driver.get("https://venetablinds.com.au/pages/shop-now?step=1&current=bottom-up&pre=honeycomb-blinds")
            
            conftest.updated_link("chrome")
                
    
    
#inheritance concept apply  
"""class TestReactPage(BaseClass):
    flag = 0
    def chooseProduct(self):
        BaseClass.verifyLinkPresence(self, "lucky")
        print("df")

TestReactPage().chooseProduct()"""
    
    
    
    