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
    wait = WebDriverWait(driver, 10)
    
    # Zoom para pantalla
    driver.execute_script("document.body.style.zoom='60%'")
    time.sleep(1)

    # Buscar el producto específico "Anyday Party Lens"
    buscador = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    buscador.send_keys("Anyday Party Lens")
    buscador.send_keys(Keys.ENTER)

    # Click en el producto
    producto = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Anyday Party Lens")))
    producto.click()
    time.sleep(2)
    
    print("✅ Página de producto")

    # Pausa para visualizar el resultado
    time.sleep(5)

finally:
    driver.quit()
