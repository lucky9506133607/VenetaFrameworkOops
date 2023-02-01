from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseClass:
    
    React_common_elements = {"continue":"//div[2]/div[2]/div[2]/div", "next":"//*[@id='root']/div/div/div/div[2]/div[2]/button[2]"}
    
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, text)))
        
    def scrollbar(self, element_name):
        self.driver.execute_script("window.scrollBy(0,265)")
        # 5. Scroll window by ('0','150')
        self.driver.execute_script("window.scrollBy(0,150)")
        # 6. Scroll window by ('0','9')
        self.driver.execute_script("window.scrollBy(0,9)")
        _button = self.driver.find_element(By.XPATH, self.React_common_elements[element_name])
        print(self.React_common_elements[element_name])
        _button.click()        
    

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

"""obj = BaseClass()
obj.scrollbar("next")"""




