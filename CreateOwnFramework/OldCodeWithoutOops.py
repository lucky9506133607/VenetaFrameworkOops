import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe")
ApplicationURL = "https://venetablinds.com.au/"
driver.get(ApplicationURL)
driver.maximize_window()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopify-section-header']/header/div/div/div[2]/a")))
finally:
    design_your_own = driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/header/div/div/div[2]/a")
    design_your_own.click()
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[1]/div[2]/ul[1]/li[1]")))
finally:
    li = driver.find_element(By.XPATH,"//div[1]/div[2]/ul[1]/li[1]")
    li.click()
driver.execute_script("window.scrollBy(0,265)")
# 5. Scroll window by ('0','150')
driver.execute_script("window.scrollBy(0,150)")
# 6. Scroll window by ('0','9')
driver.execute_script("window.scrollBy(0,9)")
_continue = driver.find_element(By.XPATH,"//div[2]/div[2]/div[2]/div")
_continue.click()
flag = 0

# 8. Scroll window by ('0','-318')

#driver.execute_script("window.scrollBy(0,-318)")
#li1 = driver.find_element(By.XPATH,"//ul[2]/li[1]")  ######################## Remove line #######################
#li1.click()



Honeycomb_product_count = driver.find_elements(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li")
for i in range(1, len(Honeycomb_product_count)+1):
    choose_product = driver.find_element(By.XPATH, "//*[@id='shopify-section-template--15942692896941__shop-now-page']/div/div[2]/div[1]/div[2]/ul[2]/li["+str(i)+"]")
    copy_choose_product = choose_product
    choose_product.click()
    print(choose_product.get_attribute("data-target-list-handle"))
    _continue = driver.find_element(By.XPATH,"//div[2]/div[2]/div[2]/div")
    _continue.click() 
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]")))
    Material_options = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div")
    for i in range(1, len(Material_options)+1):
        get_Sheer_Option = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
        print("//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div["+str(i)+"]")
        if get_Sheer_Option.get_attribute("title") == "Sheer":
            get_Sheer_Option.click()
            flag=1
            break
        else:
            pass
    if flag == 1:
        _next = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/button[2]")
        _next.click()
        # loop for sheer colors
        sheer_colors_count = driver.find_elements(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span")
        for i in range(1, len(sheer_colors_count)+1):
            select_color = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]/div[4]/div/div[3]/span["+str(i)+"]")
            
            #Add Screenshot code if needed
            
            print("color id ====== "+str(i))
            flag = 0
        
    else:
        print("Sheer not available")
        
    driver.get("https://venetablinds.com.au/pages/shop-now?step=1&current=bottom-up&pre=honeycomb-blinds")
    
    
    
    
    
    
    
    
    
    
    