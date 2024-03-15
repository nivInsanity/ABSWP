from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

def loginIntoAcc():

    driver.get('https://account.protonmail.com/login')
    #waiting only for login here, because when login is loaded - password will be loaded too :)
    time.sleep(1)
    nLoginElement = driver.find_element_by_xpath('//*[@id="username"]')
    nLoginElement.send_keys('hornySasquatch1234@protonmail.com')
    PassElem = driver.find_element_by_xpath('//*[@id="password"]')
    PassElem.send_keys('twujStaryNigdyNieJestTrzezwy123)(*&^%$#@!')
    loginClickButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/form/button')
    loginClickButton.click()
    time.sleep(8)

def messageWriteFunc():

    i = 0
    while i == 0:
        emailRecipient = input('Write an e-mail recipient: \n')
        print('Is that adress "' + emailRecipient + '" correct?\n0-No 1-Yes')
        check = input()
        if check == '0':
            print('So write again.')
            continue
        elif check == '1':
            break
        else:
            print('Incorrect data! Try again.')
    while i == 0:
        emailTopic = input('Write topic: \n')
        print('Is that topic "' + emailTopic + '" correct?\n0-No 1-Yes')
        check = input()
        if check == '0':
            print('So write again.')
            continue
        elif check == '1':
            break
        else:
            print('Incorrect data! Try again.')

    while i == 0:
        message = input('Write a message: \n')
    #TODO: multi line message from a command line
        print('Is that message "' + message + '" correct?\n0-No 1-Yes')
        check = input()
        if check == '0':
            print('So write again.')
            continue
        elif check == '1':
            break
        else:
            print('Incorrect data! Try again.')

    nMessButtonFind = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div[2]/button')
    nMessButtonFind.click()
    time.sleep(1)
    emAddressWrite = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/input')
    emAddressWrite.send_keys(emailRecipient)
    topicWrite = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div/div[3]/input')
    topicWrite.send_keys(emailTopic)
    changeMessType = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/section/div/div/div[2]/button[14]')
    changeMessType.click()
    changeMessTypeDropMenu = driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[5]/button')
    changeMessTypeDropMenu.click()
    writeMessage = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/section/div/div/div[1]/textarea')
    #below code explanation - protonmail has shitty watermark-like thing and that simple combination surpass this paywall crap :)
    writeMessage.send_keys(Keys.CONTROL, 'a')
    writeMessage.send_keys(message)
    messSendButton = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/footer/div[1]/button')
    messSendButton.click()
    print('Message was sent successfully.')
    time.sleep(3)

def logoutAndExit():
    logoutDropButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/header/div[2]/ul/li[6]/button/span[2]')
    logoutDropButton.click()
    logoutButton = driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[8]/div/button')
    logoutButton.click()
    driver.close()

loginIntoAcc()
messageWriteFunc()
logoutAndExit()