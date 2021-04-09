# import smtplib
# x = 5
# vareid = 53243
# varenavn = "Tusch"
#
# server=smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=120)
# server.login("arkivHTX@gmail.com","Belgisk/Vaffel55")
# server.sendmail("arkivHTX@gmail.com",
#                 "arkivHTX@googlemail.com", "Maybe?")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('Indtast gmail, password, modtager e-mail og varenavn')
gmailId, passWord, modtager, vareNavn = map(str, input().split())
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

driver.implicitly_wait(1000)
try:
    new_email = driver.find_element_by_xpath('//*[@class ="T-I T-I-KE L3"]').click()

    driver.find_element(by.CLASS, "vO").send_keys("Test2"+Keys.ENTER)
    # modtager.send_keys("kage")
    #emne = driver.find_element_by_xpath('//*[@name ="subjectbox"]').click()
    #emne.send_keys("Lav mængde af")
    #Besked = driver.find_element_by_xpath('//*[@]')
    driver.find_element(By.NAME, "subjectbox").send_keys("Test" + Keys.ENTER)
except:
    ('Email Failed')
