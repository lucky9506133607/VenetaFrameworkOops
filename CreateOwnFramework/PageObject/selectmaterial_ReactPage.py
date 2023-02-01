from selenium.webdriver.common.by import By
from selenium import webdriver

class selectmaterial_ReactPage:

    def __init__(self, driver):
        self.driver = driver

    count_colours = (By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span")

    def countColourOptions(self):
        return self.driver.find_elements(self.count_colours)
    
    def get_MaterialName(self, productid):
        return self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(productid)+"]")            

    def browser_console(self):
        return self.driver.execute_script("console.log('Hello, World!')")
    


