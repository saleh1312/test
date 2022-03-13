from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import sys

# function to catch the elements
def ww(driver,xpath,exite=True,coll=False):
    try:
        if coll ==True:
            
            element = WebDriverWait(driver,20).until(
             EC.presence_of_all_elements_located((By.XPATH, xpath)))
        else:
            element = WebDriverWait(driver,20).until(
             EC.presence_of_element_located((By.XPATH, xpath)))
            
        
        return element
        
    except:
        if exite==True:
            print("not found")
            sys.exit()
        else:
            return None
        
        
driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")
driver.get("https://cov-lineages.org/?fbclid=IwAR0s1FxNAtWP7iqbY6tQ1OJskxiUZGwnW4Wp0-OVADR034V5Ma_IswolKj4https://twitter.com/")  
button=ww(driver,"//*[@id='main_nav']/li[3]/a")
button.click()

########## get the parent table
table_xpath="//table[@id='myTable' and @class='table']/tbody/tr"
table=ww(driver,table_xpath,coll=True)
rows=len(table)

######### loop over all the elemnts in the parent table
links={}
for row in range(1,rows+1):
    
    ### get the link in every row in parent table
    xpath_ele=f"{table_xpath}[ position()={row} ]/td[position()=1]/a"
    link=ww(driver,xpath_ele)
    link_name=link.text
    link.click()
    
    
    ### get the child table
    tablec=ww(driver,"//table[@id='myTable' and @class='table']/tr",coll=True)
    
    ### loop over all rows in the child table
    childs=[]
    for rowc in tablec:
        linkc=rowc.find_element_by_xpath("./td[position()=1]/a")
        childs.append(linkc.text)
        
    links[link_name]=childs
    driver.back()

        
driver.quit()
        
