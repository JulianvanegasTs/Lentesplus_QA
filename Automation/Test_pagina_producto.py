from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-features=UseOzonePlatform")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.lentesplus.com/co/")
    wait = WebDriverWait(driver, 20)
    
    driver.execute_script("document.body.style.zoom='80%'")
    time.sleep(2)

    buscador = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    buscador.send_keys("lentes de contacto")
    buscador.send_keys(Keys.ENTER)

    producto = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".item-image-LiM.item-loaded-nHr")
    ))

    driver.execute_script("arguments[0].click();", producto)

    titulo_producto = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.base"))
    )

    time.sleep(2)

finally:
    driver.quit()
