from selenium.webdriver.common.by import By

class MainProduct_ReactPage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//div[1]/div[2]/ul[1]/li[1]")

    def getMainProduct(self):
        return self.driver.find_element(self.shop)
    
    





