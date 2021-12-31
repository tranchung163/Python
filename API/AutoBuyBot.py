import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import pyttsx3
import os

pathname = os.path.abspath(os.getcwd())
pathname = pathname + '/chromedriver0'

link1 = 'https://www.amazon.com/dp/B08L8KC1J7?smid=ATVPDKIKX0DER&tag=avu-20&aod=1'
userID = input("Enter your ID: ")
password = input("Enter your password: ")

buyAvailable = False

driver = webdriver.Chrome(pathname)
driver.get(link1)

try:
    cookie = driver.find_element_by_id('sp-cc-accept')
    cookie.click()
except:
    print('no cookies')

while buyAvailable == False:
    try:
        buynow = driver.find_element_by_id('submit.buy-now')
        buynow.click()
        buyAvailable = True
        os.system('say "Peep Peep."')

    except:
        driver.refresh()
        time.sleep(4)

try:
    cancel = driver.find_element_by_id('signup_cancel')
    cancel.click()

except:
    email = driver.find_element_by_id('ap_email')
    email.send_keys(userID)

    cn = driver.find_element_by_id('continue')
    cn.click()

    passWard = driver.find_element_by_id('ap_password')
    passWard.send_keys(password)

    login = driver.find_element_by_id('signInSubmit')
    login.click()

    checkout = driver.find_element_by_name('placeYourOrder1')
    checkout.click()

    checkout1 = driver.find_element_by_name('forcePlaceOrder')
    checkout1.click()



'''if buyAvailable == True:
    engine = pyttsx3.init()
    engine.say("your order has been added to cart")
    engine.runAndWait()'''











