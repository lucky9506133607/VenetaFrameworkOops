from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseClass:
    
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, text)))
        
    def scrollbar(self):
        self.driver.execute_script("window.scrollBy(0,265)")
        # 5. Scroll window by ('0','150')
        self.driver.execute_script("window.scrollBy(0,150)")
        # 6. Scroll window by ('0','9')
        self.driver.execute_script("window.scrollBy(0,9)")
        _continue = self.driver.find_element(By.XPATH,"//div[2]/div[2]/div[2]/div")
        _continue.click()        
    

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
