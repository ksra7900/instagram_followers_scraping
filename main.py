import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

from Enter_Data import Instagram_ID, username, password

PATH = 'driver/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.instagram.com/'+Instagram_ID+'/')

def LogIn(username, password):
    try:
        cookie_accept = driver.find_element_by_xpath('//button[text()="Accept All"]')
        cookie_accept.click()
        time.sleep(3)
    except:
        pass

    user = driver.find_element_by_name('username')
    pas = driver.find_element_by_name('password')

    user.click()
    user.send_keys(username)

    pas.click()
    pas.send_keys(password)

    log_in = driver.find_element_by_xpath('//div[text()="Log In"]')
    log_in.click()
    time.sleep(5)

    try:
        info = driver.find_element_by_xpath('//button[text()="Not Now"]')
        info.click()
        time.sleep(3)
    except:
        pass
    

    try:
        notif = driver.find_element_by_xpath('//button[text()="Not Now"]')
        notif.click()
        time.sleep(3)
    except:
        pass

def scrolling():
    counter = 0
    while True:
        scroll = driver.find_element_by_xpath('//div[@class="isgrP"]')
        driver.implicitly_wait(10)
        # Scroll down to bottom
        scroll.click()
        ActionChains(driver).move_to_element(scroll).send_keys(Keys.END).perform()

        height = driver.execute_script('return document.getElementsByClassName("isgrP")[0].scrollHeight;')
        
        # Calculate new scroll height and compare with last scroll height
        if height == counter:   
            break
        counter = height

        # wait to load page
        time.sleep(2)

def fetch_comments(insta_ID):
    user_names = []

    # show followers
    show_followers = driver.find_element_by_xpath('//a[@href="/'+insta_ID+'/followers/"]')
    show_followers.click()
    time.sleep(3)

    scrolling()

    followers = driver.find_elements_by_xpath('//div[@class="PZuss"]/li')
    for f in followers:
        Uname = f.find_elements_by_xpath('//span[@class="Jv7Aj mArmR MqpiF  "]/a')
        
    for u in Uname:
        print(u.text)
        user_names.append(str(u.text))

    dict = {'username' : user_names}
    df = pd.DataFrame(dict)
    df.to_csv('followers.csv')


    


if __name__ == '__main__':
    LogIn(username, password)
    fetch_comments(Instagram_ID)