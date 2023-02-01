from selenium.webdriver.common.by import By
from selenium import webdriver

class colour_ReactPage:

    def __init__(self, driver):
        self.driver = driver

    count_materials = (By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div")
    

    def countColourOptions(self):
        return self.driver.find_elements(self.count_materials)
    
    def select_ColourOption(self, productid):
        return self.driver.find_element(By.XPATH, productid)
        
    
    def browser_console(self):
        return self.driver.execute_script("console.log('Hello, World!')")
    


