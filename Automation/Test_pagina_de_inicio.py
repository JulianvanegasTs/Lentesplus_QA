from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-features=UseOzonePlatform")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    driver.get("https://www.lentesplus.com/co/")
    time.sleep(3)
    
    # Zoom para pantalla
    driver.execute_script("document.body.style.zoom='60%'")
    time.sleep(1)
    
    print("✅ Página de Lentesplus")
   
finally:
    driver.quit()
