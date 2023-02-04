from selenium import webdriver

class Conftest:
    def setup(self, lucky):
        global driver
        if lucky == "chrome":
            driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
            ApplicationURL = "https://venetablinds.com.au/"
            driver.get(ApplicationURL)
            driver.maximize_window()
        else:
            print("Driver are not available")
    
      
    
    def updated_link(self, newlink):
        driver.get(self.newlink)
        driver.maximize_window()
            
