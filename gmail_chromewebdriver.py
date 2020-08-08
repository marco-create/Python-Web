from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

print('Insert your email: ')
email = input()
print('Insert your password: ')
password = input()
print('Insert recipient address: ')
send_to = input()
print('Insert the subject for your mail: ')
subject = input()
print('Write your text below (remember that to wrap the text, you need {} when you want the text to be wrapped.'.format(r'\n'))
maintext = input()
print('==='*7)

## LOGIN VIA STACK OVERFLOW.
## Connecting using chromewebdriver.exe causes google to block the direct login. To avoid this, login in google via Stack Overflow.
driver = webdriver.Chrome()
driver.get('https://stackoverflow.com/')
driver.find_element_by_link_text('Log in').click()
time.sleep(6)    # avoid reCAPCHA
main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()
driver.implicitly_wait(5)

## LOGIN IN GOOGLE. Email box by name...
driver.find_element_by_name('identifier').send_keys(email)
print('EMAIL: found')
driver.find_element_by_class_name('VfPpkd-RLmnJb').click()
print('EMAIL: done')

## Depending from your settings, could be that Chrome will ask you to validate your login via mobilephone instead insert the password.
## If so, you need to check your phone. To avoid timing problems, let's the program wait for a while.
driver.implicitly_wait(10)
try:
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    print('PASSWORD: found box')
    driver.find_element_by_id('passwordNext').click()
    print('PASSWORD: done')
except:
    print('PASSWORD: validation via mobile')
finally:
    pass
time.sleep(6)

## Eventually, we can redirect into Gmail and locate the "Compose" button by xpath.
driver.get('https://mail.google.com/mail/u/0/#inbox')
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Compose")]'))).click()
print('NEW MAIL: pressed')

try:
    recipient = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//textarea[contains(@name,"to")]'))
    )
    recipient.send_keys(send_to)
    print('RECIPIENT: filled')
    text_subj = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.NAME, 'subjectbox'))
    )
    
    text_subj.send_keys(subject)
    print('SUBJECT: filled')
    try:
        main_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=":rt"]/div/div/div/div/div/div/div/div/p[1]')))   
    except:
        main_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id=":rt"]/div/div/div/div/div/div/div/div/p[1]')))
    finally:
    print('main text-box found') 
    driver.implicitly_wait(3)  
    main_box.send_keys(maintext.replace('\\n',' \n'))
    
    time.sleep(20)    # wait for the writing
    driver.find_element_by_xpath('//div[contains(text(),"Send") and @role="button"]').click()
    print("Message Sent Successfully")
except:
    print('Main mail box error')
