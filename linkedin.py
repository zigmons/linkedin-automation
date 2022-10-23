from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver = webdriver.Chrome()

driver.get("https://www.google.com.br")