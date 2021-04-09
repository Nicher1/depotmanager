from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def lowInvMail(gmailId,passWord,modtager,vareNavn):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)

        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(gmailId)

        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)

        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()

        print('Login Successful...!!')
        # gmail send email attempt

    except:
        print('Login Failed')

    driver.implicitly_wait(150)
    try:
        new_email = driver.find_element_by_xpath('//*[@class ="T-I T-I-KE L3"]').click()
        driver.find_element_by_xpath("//textarea[@class='vO']").send_keys(modtager+Keys.ENTER)
        emne= driver.find_element_by_xpath("//input[@name='subjectbox']")
        emne.click()
        emne.send_keys("Der er lav mængde af "+vareNavn)
        textbox = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")
        textbox.click()
        textbox.send_keys("Yo bitch! Denne vare: "+vareNavn+ " er lav i beholdning.")
        print('input Successful...!!')
    except:
        ('Email Failed')

    try:
        send_knap = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
        send_knap.click()
        print('sending Successful...!!')
        time.sleep(2)
    except:
        ('Email not sent')

lowInvMail("arkivHTX@gmail.com","Belgisk/Vaffel55","simon.thomsen01@gmail.com","hjerneceller")
