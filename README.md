# SauceDemo Playwright Python

Proyecto de automatización de pruebas E2E para [SauceDemo](https://www.saucedemo.com/)
utilizando Playwright y Python.

## 🛠️ Tecnologías

- Python 3.x
- Playwright
- Pytest
- Allure Reports
- Jenkins (CI/CD)

## 📁 Estructura del proyecto

```
SauceDemoPlaywright/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_two_page.py
│   └── checkout_complete_page.py
├── tests/
│   └── test_login.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## ✅ Casos de prueba

| Test                 | Descripción                                             |
| -------------------- | ------------------------------------------------------- |
| `test_login_success` | Verifica login exitoso con credenciales válidas         |
| `test_e2e`           | Flujo completo de compra desde login hasta confirmación |

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Maab-7/SauceDemoPlaywright.git
cd SauceDemoPlaywright
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Ejecutar tests

```bash
# Modo visual
pytest tests/test_login.py -v

# Modo headless
HEADLESS=true pytest tests/test_login.py -v
```

### 5. Ver reporte Allure

```bash
allure serve allure-results
```

## 📊 Allure Reports

El proyecto genera reportes detallados con Allure mostrando cada paso
de los tests con duración y estado.

## 🔄 CI/CD

El proyecto está integrado con Jenkins para ejecución automática
en modo headless con generación de reportes Allure.

## 🏗️ Patrón de diseño

Implementa el patrón **Page Object Model (POM)** para mantener
el código organizado, reutilizable y fácil de mantener.
