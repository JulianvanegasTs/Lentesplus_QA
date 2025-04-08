from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

chrome_options = Options()
chrome_options.add_argument("--disable-features=UseOzonePlatform")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    driver.get("https://www.lentesplus.com/co/")
    time.sleep(3)
    
    driver.execute_script("document.body.style.zoom='80%'")
    time.sleep(3)
    
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Lentes de contacto")
    time.sleep(1)
    
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

finally:
    driver.quit()


