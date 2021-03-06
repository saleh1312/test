from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import sys
import math


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
        
        
        
#to make the code work for all elements in the website change the value to math.inf like that---> limit = math.inf   
limit=2


driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")
driver.get("https://cov-lineages.org/?fbclid=IwAR0s1FxNAtWP7iqbY6tQ1OJskxiUZGwnW4Wp0-OVADR034V5Ma_IswolKj4https://twitter.com/")  
button=ww(driver,"//*[@id='main_nav']/li[3]/a")
button.click()

########## get the parent table
table_xpath="//table[@id='myTable' and @class='table']/tbody/tr"
table=ww(driver,table_xpath,coll=True)
rows=len(table)

links={}

x=1
for row in range(1,rows+1):
    
    xpath_ele=f"{table_xpath}[ position()={row} ]/td[position()=1]/a"
    link=ww(driver,xpath_ele)
    link_name=link.text
    link.click()
    
    tablec=ww(driver,"//table[@id='myTable' and @class='table']/tr",coll=True)
    
    childs=[]
    
    y=1
    for rowc in tablec[1:]:
        linkc=rowc.find_element_by_xpath("./td[position()=1]/a").text
        most_commen=rowc.find_element_by_xpath("./td[position()=2]").text
        earlies_date=rowc.find_element_by_xpath("./td[position()=3]").text
        disign_date=rowc.find_element_by_xpath("./td[position()=4]").text
        assign=rowc.find_element_by_xpath("./td[position()=5]").text
        desciption=rowc.find_element_by_xpath("./td[position()=6]").text
        who_name=rowc.find_element_by_xpath("./td[position()=7]").text
        
        childs.append([linkc,most_commen,earlies_date,disign_date,assign,desciption,who_name])

        
        if y==limit:
            break
        y+=1
        
    links[link_name]=childs
    driver.back()
    
    
    
    if x==limit:
        break
    x+=1

        
driver.quit()
        

for key , value in links.items():
    print('#################')
    print('parent: ',key)
    print('childs:')
    for child in value:
        print('    ',child)
        print('')
        
        
        
