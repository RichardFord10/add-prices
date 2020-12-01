import openpyxl
import selenium
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import pandas as pd
import sys
import csv
import os

# configure webdriver & headless chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options = chrome_options, executable_path=r'C:/Users/rford/Desktop/chromedriver/chromedriver.exe')

# current day format
currentDate = datetime.today().strftime('%Y-%m-%d')




def login(user, pword = str):
    driver.get("www.#######.com")
    Username = driver.find_element_by_id("bvuser")
    Password = driver.find_element_by_id("bvpass")
    Login = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/input')
    Username.send_keys(user)
    Password.send_keys(pword)
    Login.click()
    print("Logging In...")


def add_prices():
    prices = []
    driver.get('https://www.#########.com/manager/sale-pricing.php?sale={}'.format(sale_id))
    qb_names = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr/td[3]')
    prices_df = pd.read_csv(r'C:\Users\rford\Desktop\add_prices.csv', usecols=['Name', "Price"])
    qb_names_csv = prices_df['Name'].tolist()
    prices_list = prices_df['Price'].tolist()
    prices.append(prices_list)
    check_boxes = driver.find_elements_by_class_name('sale_checked')
    input_boxes = driver.find_elements_by_xpath('//*[contains(@id, "price_")]')
    # while True:
    #     try:
    #         sale_id = int(input('Please Enter Sale ID: '))
    #     except ValueError:
    #         print("Please enter a valid Sale ID: ")
    #         continue
    #     else: 
    #         break
    #get prices from add_prices.csv 

    for check_box in check_boxes:
        check_box.click()

    for input_box in input_boxes:
        input_boxes.clear()


            


login(input("Enter Username: "), getpass("Enter Password: "))
add_prices()