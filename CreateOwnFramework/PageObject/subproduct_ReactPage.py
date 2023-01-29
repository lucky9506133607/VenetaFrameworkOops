from selenium.webdriver.common.by import By

class subproduct_ReactPage:

    def __init__(self, driver):
        self.driver = driver

    count_subproducts = (By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li")
    

    def countSubProducts(self):
        return self.driver.find_elements(self.count_subproducts)
    
    def get_SubProduct(self, productid):
        return self.driver.find_element(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li["+str(productid)+"]")            
    
    def get_SubProductName(self, productid):
        return self.driver.find_element(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li["+str(productid)+"]")                
        


