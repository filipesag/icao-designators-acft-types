import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# ICAO URL 
url = "https://www.icao.int/publications/DOC8643/Pages/SpecialDesignators.aspx"

#Selenium config
option = Options()

#In order to see browser opening set True, otherwise set False
option.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

#Access icao website
driver.get(url)
driver.implicitly_wait(10) 

#Get table html content
element = driver.find_element(By.XPATH, "//div[@class='ms-rtestate-field']//table")
html_content = element.get_attribute('outerHTML')

#Parse html content 
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#Structuring html content to DF
df = pd.read_html( str(table) )[0]

#Saving as CSV
df.to_csv('special_designators_type.csv',index=False)

#Close session
driver.quit()