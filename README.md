# **LentesPlus QA Automation Project**  
> Proyecto de automatización de pruebas para la plataforma de e-commerce [LentesPlus](https://www.lentesplus.com).  

---

## **Descripción**
Este proyecto implementa un framework de automatización de pruebas diseñado para garantizar la calidad del sitio web de LentesPlus. Las pruebas automatizadas validan funcionalidades clave, flujos de usuario críticos y la integridad de los datos en la plataforma.  

El objetivo principal es reducir los errores en producción, mejorar la experiencia del cliente y asegurar que los cambios en el código no introduzcan fallos.  

---

## **Características**
- Pruebas funcionales y de regresión automatizadas usando **Python** y **Selenium**.  
- Validación de datos contra una base de datos MySQL.  
- Generación de reportes visuales con **Allure-reports** para análisis de resultados.  
- Ejecución de pruebas en múltiples navegadores (Chrome y Firefox).

---

## **Tecnologías utilizadas**
- **Lenguaje:** Python 3.10  
- **Framework de pruebas:** Selenium  
- **Gestión de dependencias:** pip  
- **Base de datos:** MySQL  
- **Herramientas de reporte:** Allure  
- **Navegadores compatibles:** Google Chrome, Mozilla Firefox  

---

## **Requisitos previos**
Antes de instalar y ejecutar este proyecto, asegúrate de tener instalado lo siguiente:
- Python (versión 3.8 o superior)  
- pip (gestor de paquetes de Python)  
- Navegador **Google Chrome** o **Mozilla Firefox**  
- Driver correspondiente:
  - [ChromeDriver](https://chromedriver.chromium.org/) (para Chrome)  
  - [GeckoDriver](https://github.com/mozilla/geckodriver) (para Firefox)  

---

## **Instalación**
1. **Clona este repositorio:**  
   ```bash
   git clone https://github.com/tu-usuario/lentesplus-qa-automation.git
   cd lentesplus-qa-automation
   ```

2. **Crea un entorno virtual:**  
   ```bash
   python -m venv venv
   source venv/bin/activate    # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**  
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:  
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=tu_contraseña
   BASE_URL=https://www.lentesplus.com
   ```

5. **Ejecuta las pruebas:**  
   ```bash
   pytest --browser chrome --base-url https://www.lentesplus.com
   ```

---

## **Estructura del proyecto**
```plaintext
lentesplus-qa-automation/
├── src/                       
│   ├── tests/                 # Scripts de prueba
│   └── utils/                 # Funciones y utilidades
├── reports/                   # Reportes generados por Allure
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Variables de entorno (no subido al repositorio)
├── README.md                  # Documentación principal
└── .gitignore                 # Archivos ignorados por Git
```

---

## **Ejemplo de ejecución**
Ejecuta las pruebas en **Google Chrome**:  
```bash
pytest --browser chrome --base-url https://www.lentesplus.com --alluredir=reports/
```

Genera y sirve el reporte con **Allure**:  
```bash
allure serve reports/
```

---

## **Contribución**
¡Tu ayuda es bienvenida! Si deseas colaborar:  
1. Realiza un fork del repositorio.  
2. Crea una rama para tus cambios:  
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y súbelos:  
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   git push origin nueva-funcionalidad
   ```
4. Abre un Pull Request en este repositorio.

---

## **Autor/es**
- **Julián Vanegas** – QA Automation Engineer  
  - GitHub: Julián Vanegas (https://https://github.com/JulianvanegasTs)  
  - LinkedIn: Julián Vanegas (www.linkedin.com/in/juliánvanegasts) 

---

## **Licencia**
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.  

---

## **Notas adicionales**
- Este proyecto puede integrarse fácilmente con sistemas CI/CD como Jenkins o GitHub Actions.  
- Si encuentras algún problema o tienes sugerencias, abre un **Issue** en este repositorio. 
