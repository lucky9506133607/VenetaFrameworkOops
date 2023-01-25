import selenium
from selenium import webdriver

def setup(request):
    if request == "chrome":
        driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
        ApplicationURL = "https://venetablinds.com.au/"
        driver.get(ApplicationURL)
        driver.maximize_window()
    else:
        print("Driver are not available")

  

