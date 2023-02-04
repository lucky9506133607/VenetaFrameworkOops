from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class DesignYourOwnPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.design_your_own_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopify-section-header']/header/div/div/div[2]/a")))
    
    def click(self):
        self.design_your_own_link.click()

class HoneycombBlindsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.honeycomb_li = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[1]/div[2]/ul[1]/li[1]")))
    
    def click(self):
        self.honeycomb_li.click()

class MaterialOptionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.continue_button = driver.find_element(By.XPATH,"//div[2]/div[2]/div[2]/div")
        self.sheer_options = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div")

    def click_continue_button(self):
        self.continue_button.click()
    
    def select_sheer_option(self):
        for option in self.sheer_options:
            if option.get_attribute("title") == "Sheer":
                option.click()
                break

if __name__ == "__main__":
    driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
    ApplicationURL = "https://venetablinds.com.au/"
    driver.get(ApplicationURL)
    driver.maximize_window()
    
    design_your_own_page = DesignYourOwnPage(driver)
    design_your_own_page.click()
    
    honeycomb_blinds_page = HoneycombBlindsPage(driver)
    honeycomb_blinds_page.click()
    
    material_option_page = MaterialOptionPage(driver)
    material_option_page.select_sheer_option()
    material_option_page.click_continue_button()
    
    driver.quit()
