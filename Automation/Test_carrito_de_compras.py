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

    # Zoom para pantallas pequeñas (opcional)
    driver.execute_script("document.body.style.zoom='60%'")
    time.sleep(2)

    # Buscar el producto específico "Anyday Party Lens"
    buscador = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    buscador.send_keys("Anyday Party Lens")
    buscador.send_keys(Keys.ENTER)

    # Click en el producto
    producto = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Anyday Party Lens")))
    producto.click()

    # Esperar que cargue el botón con la clase "selectCustom-button-2-2"
    dropdowns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "selectCustom-button-2-2")))
    
    # Hacer click en el primer botón (ojo izquierdo)
    color_dropdown_izq = dropdowns[0]
    driver.execute_script("arguments[0].click();", color_dropdown_izq)

    # Usar la clase del dropdown (primer elemento es el ojo izquierdo)
    dropdowns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "selectCustom-button-2-2")))
    color_dropdown_izq = dropdowns[0]
    
    # Esperar que aparezca la lista y seleccionar la primera opción (Jade)
    jade_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[text()='Jade']")))
    jade_option.click()
    
    # Esperar boton de agregar al carrito y seleccionar
    add_to_car = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "productFullDetail-lpi_bag-Gm2")))
    add_to_car.click()
    time.sleep(2)
    
    print("✅ Carrito de compra")
    
    # Pausa para visualizar el resultado 
    time.sleep(5)  

finally:
    driver.quit()
