from dataclasses import replace
from xmlrpc.client import boolean
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os, time
#login
#path = os.path.abspath('msedgedriver.exe')
browser = webdriver.Edge()
browser.get('https://servicosredessociais.com.br/')
usuario = browser.find_element(By.CSS_SELECTOR,'#username')
usuario.send_keys('usuario')
usuario = browser.find_element(By.CSS_SELECTOR,'#password') 
usuario.send_keys('senha')
usuario.submit()
#3572:13440:0205/144234.043:ERROR:chrome_browser_main_extra_parts_metrics.cc(251)
#search
j = 0
valor = 1
while(j < 11):
    browser.get('https://servicosredessociais.com.br/orders/all/' + str(j))
    
        #preparaSearch = '/html/body/div/div/div/div/table/tbody/tr[valor]/td[10]/div/a'
        #preparaSearch = preparaSearch.replace('valor', str(valor))
        
    target = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/table/thead/tr/th[13]/button")
    target.click();
    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = browser.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")
        
    time.sleep(30)
    j += 1

browser.quit()
