from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

# Login

driver.find_element(By.ID,"username").click()

driver.find_element(By.ID,"username").send_keys("*****")
time.sleep(2)

# Senha

driver.find_element(By.ID,"password").click()

driver.find_element(By.ID,"password").send_keys("****")
time.sleep(5)

driver.find_element(By.CLASS_NAME,"login__form_action_container ").click()
time.sleep(5)

#Entrando em vagas
driver.find_element(By.XPATH,"/html/body/div[4]/header/div/nav/ul/li[3]/a").click()

time.sleep(3)

#clicando em pesquisar vagas
driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[3]/a").click()

time.sleep(3)
#mandando a vaga  -   COM ERRO
driver.find_element(By.ID,"jobs-search-box-keyword-id-ember771").send_keys("Analista Comercial")

driver.find_element(By.ID,"jobs-search-box-keyword-id-ember771").send_keys(Keys.TAB)

driver.find_element(By.ID,"jobs-search-box-location-id-ember771").send_keys("Jundiaí")

driver.find_element(By.ID,"jobs-search-box-location-id-ember771").send_keys(Keys.ENTER)


#selecionando candidatura simplificada

driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div").click()