from dataclasses import replace
from xmlrpc.client import boolean
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os, time
#login
path = os.path.abspath('msedgedriver.exe')
browser = webdriver.Edge(path)
browser.get('https://servicosredessociais.com.br/')
usuario = browser.find_element_by_css_selector('#username')
usuario.send_keys('usuario')
usuario = browser.find_element_by_css_selector('#password') 
usuario.send_keys('senha')
usuario.submit()
#3572:13440:0205/144234.043:ERROR:chrome_browser_main_extra_parts_metrics.cc(251)
#search
j = 0
valor = 1
while(j < 11):
    time.sleep(30)
    browser.get('https://servicosredessociais.com.br/orders/all/' + str(j))
    
        #preparaSearch = '/html/body/div/div/div/div/table/tbody/tr[valor]/td[10]/div/a'
        #preparaSearch = preparaSearch.replace('valor', str(valor))
        
    target = browser.find_elements_by_partial_link_text("Reposição")
    for x in range(0,len(target)):
                if target[x].is_displayed():
                    target[x].click()
        
    j += 1

browser.quit()
