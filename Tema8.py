# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app
#
# (obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)
#
# 3 selectors by:
# Id
# Link text
# Partial link text
# Name
# Tag*
# Class name*
# Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)
#
# *La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
#
# La Xpath:
# 3 dupa atribut valoare
# 3 dupa textul de pe element
# 1 dupa partial text
# 1 cu SAU, folosind pipe |
# 1 cu *
# 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# 1 in care sa folosesti parent::
# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
#
# Studiu extra daca doriti:
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# selector by ID
# # 1
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# #
# # # maximizam fereastra
# chrome.maximize_window()
#
# # # navigam catre un url
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# create_account = chrome.find_element(By.ID, 'email_create')
# create_account.clear()
# create_account.send_keys('tarzioru.antonia@yahoo.com')
# sleep(4)
# chrome.quit()


# #2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# location = chrome.find_element(By.ID,'locality')
# location.clear()
# location.send_keys(f' Brasov')
# sleep(4)
# chrome.quit()
# #3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?id_category=4&controller=category')
# location = chrome.find_element(By.ID,'newsletter-input')
# location.clear()
# location.send_keys(f'tarzioru.antonia@yahoo.com')
# sleep(4)
# chrome.quit()
#
#
#
# # selector by Link Text
# #1
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get(' http://automationpractice.com/index.php?id_category=4&controller=category' )
# chrome.find_element(By.LINK_TEXT, 'Faded Short Sleeve T-shirts').click()
# sleep(4)
# chrome.quit()

##2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get(' http://automationpractice.com/index.php?id_category=11&controller=category' )
# chrome.find_element(By.LINK_TEXT, 'Printed Chiffon Dress').click()
# sleep(4)
# chrome.quit()
##3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get(' https://formy-project.herokuapp.com/' )
# chrome.find_element(By.LINK_TEXT, 'Switch Window').click()
#
# sleep(4)
# chrome.quit()

## Partial link text
##1
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get(' https://formy-project.herokuapp.com/' )
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Page ').click()
#
# sleep(4)
# chrome.quit()
##2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get('https://the-internet.herokuapp.com/' )
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Disappearing ').click()
#
# sleep(4)
# chrome.quit()
##3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get('https://the-internet.herokuapp.com/' )
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Codes').click()
#
# sleep(4)
# chrome.quit()


# selector by Name
##1&2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
#
# chrome.get('https://www.phptravels.net/contact' )
# chrome.find_element(By.NAME, 'name').clear()
# chrome.find_element(By.NAME, 'name').send_keys('Alex')
# chrome.find_element(By.NAME, 'email').clear()
# chrome.find_element(By.NAME, 'email').send_keys('blabla@gmail.com')
# sleep(4)
# chrome.quit()
#
#
#
# #3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.NAME, 'id_order').send_keys('001')
#
# sleep(4)
# chrome.quit()
# #4
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/forgot_password')
# chrome.find_element(By.NAME, 'email').clear()
# chrome.find_element(By.NAME, 'email').send_keys(' blabla@gmail.com')
# sleep(4)
# chrome.quit()



#find by tag
##1
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/login')
# chrome.find_element(By.TAG_NAME, 'input').send_keys('tomsmith')
#
# input_list = chrome.find_elements(By.TAG_NAME, 'input')
# input_list[1].send_keys('SuperSecretPassword!')
# sleep(4)
# chrome.quit()

##2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.TAG_NAME, 'input').send_keys('Ana')
#
# lista_numere = chrome.find_elements(By.TAG_NAME, 'input')
# lista_numere[1].send_keys('Are')
# lista_numere[2].send_keys('mere cu m mic')
# sleep(4)
# chrome.quit()
# ##3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.TAG_NAME, 'input').send_keys('Ana')
#
# lista_numere = chrome.find_elements(By.TAG_NAME, 'input')
# lista_numere[1].send_keys('Are')
# lista_numere[2].send_keys('mere cu m mic')
# sleep(4)
# chrome.quit()

# selector by Class - ia primul tot timpul- e ok doar daca avem clasa unica

##1

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
# chrome.find_element(By.CLASS_NAME, 'subcategory-name').click()
# sleep(4)
# chrome.quit()
##2&3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/signup')
#
# chrome.find_elements(By.CLASS_NAME,'form-control')[2].send_keys('123456798')#telefon
# chrome.find_elements(By.CLASS_NAME,'form-control')[1].send_keys('ana')#last name
# chrome.find_elements(By.CLASS_NAME,'form-control')[0].send_keys('popescu')#first name
#
# sleep(4)
# chrome.quit()


#_____________________________________________________________________________________________________________
#Css(1 dupa id, 1 dupa clasa, 1 dupa atribut = valoare_partiala)
#id
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?id_category=7&controller=categoryp')
#
# chrome.find_element(By.CSS_SELECTOR,'input#newsletter-input').send_keys('exampleInputEmail1')
# sleep(4)
# chrome.quit()
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/signup')
# #clasa
# chrome.find_elements(By.CSS_SELECTOR,'input.form-control')[4].send_keys('1234')#password
# # selector by CSS - atribut=valoare partiala + parinte -> copil
# chrome.find_element(By.CSS_SELECTOR,'div input[placeholder*="Email"]').send_keys('itclass@gmail.com')
#
# sleep(4)
# chrome.quit()

#_____________________________________________________________________________________________________________
#La Xpath:
# 3 dupa atribut valoare
# 3 dupa textul de pe element
# 1 dupa partial text
# 1 cu SAU, folosind pipe |
# 1 cu *
# 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# 1 in care sa folosesti parent::
# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.

# selector by Xpath - atribut=valoare
##1
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
#
# chrome.find_element(By.XPATH, '//input[@id="postal_code"]').send_keys('507190')
# sleep(4)
# chrome.quit()

##2
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/login')
# chrome.find_element(By.XPATH, '//input[@name="email"]').send_keys('email@email.com')
# sleep(4)
# chrome.quit()
##3
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.XPATH, '//input[@name="lastname"]').click()
# chrome.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('aaaa')
# sleep(4)
# chrome.quit()

## selector by Xpath - in f de textul vizibil
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.XPATH,'//button[text()="Button"]').click() #Process finished with exit code 0
# sleep(4)
# chrome.quit()


# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?controller=password')
# chrome.find_element(By.XPATH,'//span[text()="Retrieve Password"]').click()#Process finished with exit code 0si eroare de email invalid
# sleep(4)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/buttons#')
# chrome.find_element(By.XPATH,'//button[text()="Middle"]').click()#Pcrocess finished with exit code 0 yaay
# sleep(4)
# chrome.quit()


##1 dupa partial text
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('http://automationpractice.com/index.php?id_category=5&controller=category')
chrome.find_element(By.XPATH, '//a[contains(text(), "Faded")]').click()##Process finished with exit code 0 yaay
sleep(4)
chrome.quit()