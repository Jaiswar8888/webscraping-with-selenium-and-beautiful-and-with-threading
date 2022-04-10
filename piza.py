import pandas as pd 
import sqlalchemy

import pandas as pd
import pymysql
from sqlalchemy import create_engine
from time import sleep
from threading import *
from struct import pack
from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import  requests
from openpyxl import Workbook
import time
import pandas as pd 
from threading import *
from multiprocessing.pool import ThreadPool as Pool
import csv
from csv import writer

cnx = create_engine('mysql+pymysql://root:pj123@localhost/db')    
df = pd.read_sql('SELECT * FROM urldb', cnx)#read the entire table
product = df.values.tolist()
print(product)

class Hello(Thread):
    def run(self):
        for row in product:
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get(row[0])
            time.sleep(1)
            if row[0]:
                MJob_titles1=driver.find_elements(By.XPATH,'//*[@id="jobDetailHolder"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div[2]/h1')
                title=[]
                for Mjob1 in (MJob_titles1):  
                    title.append(Mjob1.text)
                   
                    print('The job title of monster.com is :-',title)
                    time.sleep(1)
                if row[0]:
                    MJob_loc1=driver.find_elements(By.XPATH,'//*[@id="jobDetailHolder"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/span/small[1]/a')
                    loc=[]
                    for Mjobloc1 in (MJob_loc1):  
                        loc.append(Mjobloc1.text)
                   
                        print('The loc of monster.com is :-',loc)
                        time.sleep(1)
                    if row[0]:
                        MJob_titles2=driver.find_elements(By.XPATH,'//*[@id="jobDetailHolder"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/h1')
                        title=[]
                        for Mjob2 in (MJob_titles2):  
                            title.append(Mjob2.text)
                   
                            print('The title of monster.com is :-',title)
                            time.sleep(1)
                        if row[0]:
                            MJob_loc2=driver.find_elements(By.XPATH,'//*[@id="jobDetailHolder"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/span/small[1]/a')
                            loc=[]
                            for Mjobloc2 in (MJob_loc2):  
                                loc.append(Mjobloc2.text)
                                print('The loc of monster.com is :-',loc)
                                time.sleep(1)
                            if row[0]:
                                MJob_Com=driver.find_elements(By.XPATH,'//*[@id="jobDetailHolder"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/span/a')
                                com=[]
                                for MjobCom in (MJob_Com):  
                                    com.append(MjobCom.text)
                                    print('The company name of monster.com is :-',com)
                                    time.sleep(1)
                                    
                                          
                                    with open('combined_file.csv', 'a', newline='') as outcsv:
                                        writer = csv.writer(outcsv)
                                        writer.writerow([title, loc,com])
                                                    
                               
                                
# Print the dataframe
print(df)
#         

t1=Hello()
t1.start()

time.sleep(2)
