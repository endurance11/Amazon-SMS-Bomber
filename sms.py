from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By

  
browser = webdriver.Chrome() 
  
frequency = 2
 
mobile_number = "9129291918"
 
for i in range(frequency): 
    browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    number = browser.find_element_by_id("ap_email")  

    number.send_keys(mobile_number) 
    
    cont= browser.find_element_by_id("continue")
    cont.click()
      
    forgot = browser.find_element_by_id("auth-fpp-link-bottom") 
      

    forgot.click() 
    
    cont1 = browser.find_element_by_id("a-autoid-0")
    cont1.click()

    time.sleep(3)
    	
browser.quit() 
