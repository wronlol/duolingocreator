# -*- coding: UTF-8 -*-
import hashlib
import platform
import random
import string
import time
import requests
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait





def createaccount():
    try:
        Bot()
    except Exception as E:
        open("log.txt", "a+").write(str(E)+"\n")
        print(E)




def Bot():

    try:
        config = open("config.txt", "r+").readlines()
        ref = config[0]
    except:
        ref = "temp"
        pass
    
    driver = webdriver.Firefox(executable_path=geckopath)

    driver.get(
        ref)






    time.sleep(2)
    register_button = driver.find_element_by_xpath("/html/body/div/div/div/span/div/div/div/ul/a[1]/div/div[2]")
    register_button.click()

    # Page 1

    reason = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/ul/label[1]/img"))
    )

    reason.click()

    #first_name.send_keys(first)

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[1]/div/button").click()
    time.sleep(2)

    #age
    first = "23"
    age = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div[1]/div/label[1]/div/input"))
    )
    age.send_keys(first)

#randommail
    random = randint(0,99999999)
    second = str(random) + "first@pepeg.com"
    mail = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div[1]/div/label[3]/div/input"))
    )
    mail.send_keys(second)


#pwd
    third = "pepeg123"
    pwd = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div[1]/div/label[4]/div/input"))
    )
    pwd.send_keys(third)


#click register

    lastbtn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/form/div[1]/button")
    lastbtn.click()


    #driver.quit()
    left = int(accounts)-int(generated)-1
    print("\n\nYour duolingo account has been created .\n\n")
    print("\n\nThere is " + str(left) + " left to make.\n\n")








if platform.system() == "Windows":  # checking OS
    geckopath = "./geckodriver.exe"
else:
    geckopath = "./geckodriver"


accounts = int(input("How many refs do u want?\n"))
print("Creating!\n")




generated = 0


while accounts > generated:
   createaccount()
   generated = generated + 1

