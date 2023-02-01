import selenium
from selenium import webdriver

class Conftest:
    def setup(request):
        global driver
        if request == "chrome":
            driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
            ApplicationURL = "https://venetablinds.com.au/"
            driver.get(ApplicationURL)
            driver.maximize_window()
        else:
            print("Driver are not available")
    
      
    
    def updated_link(request):
        global driver
        if request == "chrome":
            driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
            ApplicationURL = "https://venetablinds.com.au/"
            driver.get(ApplicationURL)
            driver.maximize_window()
        else:
            print("Driver are not available")