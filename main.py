from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import string
import random
import time
from threading import Thread
import keyboard

stop = False
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


botCount = input("How many bots: ")
currentSentBots = 1
gamePin = input("Game pin: ")
namePrefix = input("Name Prefix: ")

def create_driver():
   chromeOptions = webdriver.ChromeOptions()
   chromeOptions.add_argument("--headless")
   chrome_options.add_experimental_option("detach", True)
   return webdriver.Chrome(options=chromeOptions) 

def sendBot(name, webdriver):
    global currentSentBots
    global stop
    webdriver.get("https://kahoot.it")

    while True:
      try:
        gameIdInputBox = webdriver.find_element(By.ID, 'game-input')
        break
      except:
        time.sleep(1)
    
    gameIdInputBox.send_keys(gamePin)

    submitId = webdriver.find_element(
        By.XPATH,
        '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button'
    )
    submitId.click()

    while True:
      try:
        nicknameBox = webdriver.find_element(By.NAME, 'nickname')
        break
      except:
        time.sleep(1)

    nicknameBox.send_keys(name)

    nicknameSubmit = webdriver.find_element(
        By.XPATH,
        '//*[@id="root"]/div[1]/div/div/div[1]/div[3]/div[2]/main/div/form/button'
    )

    nicknameSubmit.click()
    print("Sent bot number", currentSentBots)
    currentSentBots += 1
    while True:
        if stop == True:
            webdriver.quit()
            exit()
        time.sleep(1)



for bot in range(int(botCount)):
    name = namePrefix + '-'

    for letter in range(5):
        name += random.choice(string.ascii_letters)
    Thread(target = sendBot, args = [name, create_driver()]).start()

while True:
    if int(currentSentBots)-1 == int(botCount):
        break
    time.sleep(1)


print("Hold space to remove bots.")

while True:
    if keyboard.is_pressed("space"):
        stop = True
        break
    time.sleep(1)

