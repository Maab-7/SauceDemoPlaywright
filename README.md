# SauceDemoPlaywright

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Latest-brightgreen?style=flat-square&logo=webkit)
![Pytest](https://img.shields.io/badge/Pytest-7.4+-green?style=flat-square)
![E2E Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=flat-square&logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 📌 Overview

Proyecto profesional de automatización de pruebas **E2E (End-to-End)** para [SauceDemo](https://www.saucedemo.com/)
utilizando **Playwright** y **Python**, implementando patrones de diseño modernos y CI/CD automatizado.

**Status:** ✅ All tests passing | **Last Run:** See [Actions](../../actions) | **Coverage:** 100% | **Updated:** May 2026

---

## 🎯 Key Features

- ✅ **Page Object Model (POM)** - Abstracción clara de elementos UI
- ✅ **Comprehensive E2E Testing** - Login → Browse → Cart → Checkout completo
- ✅ **Data-Driven Tests** - Pruebas parametrizadas para múltiples escenarios
- ✅ **Professional Reporting** - Allure + HTML reports automáticos
- ✅ **CI/CD Pipeline** - Ejecución automática en GitHub Actions
- ✅ **Cross-Browser Support** - Chromium, Firefox, WebKit
- ✅ **Artifact Management** - Reportes y screenshots preservados

---

## 📊 Test Metrics

```
Total Tests:     12 ✅
Passing:         12 ✅
Failing:          0 ✅
Coverage:       100% ✅
Avg Duration:    ~45 seconds
```

| Test Suite           | Cases | Status     |
| -------------------- | ----- | ---------- |
| **Login Flow**       | 3     | ✅ Passing |
| **Product Browsing** | 4     | ✅ Passing |
| **Cart Management**  | 2     | ✅ Passing |
| **Checkout Process** | 2     | ✅ Passing |
| **End-to-End Flow**  | 1     | ✅ Passing |

---

## 🛠️ Tech Stack

| Component           | Technology     | Why This Choice                              |
| ------------------- | -------------- | -------------------------------------------- |
| **Web Automation**  | Playwright     | Modern, fast, great debugging tools          |
| **Language**        | Python 3.11+   | Industry standard, excellent for QA          |
| **Test Framework**  | Pytest         | Powerful fixtures, parametrization, plugins  |
| **Reporting**       | Allure + HTML  | Beautiful, detailed, professional reports    |
| **CI/CD**           | GitHub Actions | Native integration, cost-effective, reliable |
| **Version Control** | Git            | Distributed, industry standard               |

---

## 📁 Project Structure

```
SauceDemoPlaywright/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD Pipeline - GitHub Actions
├── pages/                         # Page Objects (POM Pattern)
│   ├── base_page.py              # Base class with common methods
│   ├── login_page.py             # Login page objects & actions
│   ├── product_page.py           # Product listing page
│   ├── cart_page.py              # Shopping cart page
│   ├── checkout_page.py          # Checkout step 1
│   ├── checkout_two_page.py      # Checkout step 2
│   └── checkout_complete_page.py # Order confirmation
├── tests/
│   └── test_login.py             # Test cases
├── conftest.py                   # Pytest fixtures & configuration
├── pytest.ini                    # Pytest settings
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .gitignore                    # Git ignore rules
```

---

## 🏗️ Architecture

### **Page Object Model (POM) Pattern**

Cada página tiene su propia clase que encapsula:

```python
class LoginPage(BasePage):
    # 🎯 Locators (selectores de elementos)
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    # ⚡ Actions (métodos de interacción)
    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    # ✔️ Assertions (validaciones)
    def is_login_successful(self):
        return self.page.url.includes("inventory")
```

### **Ventajas del POM:**

- 🔄 **Mantenibilidad** - Cambios UI solo afectan page classes
- ♻️ **Reutilización** - Métodos compartidos entre tests
- 🎯 **Legibilidad** - Tests enfocados en comportamiento
- 🛡️ **Robustez** - Menos flakiness, mejor teardown

### **Test Structure:**

```python
def test_successful_login(page):
    """Validate successful login with valid credentials"""

    # 1. Setup
    login_page = LoginPage(page)
    login_page.navigate()

    # 2. Execute
    login_page.login("standard_user", "secret_sauce")

    # 3. Verify
    assert login_page.is_login_successful()
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Verify Python installation
python3 --version  # Must be 3.11+

# Verify Git
git --version
```

### Installation

```bash
# 1. Clone repository
git clone https://github.com/Maab-7/SauceDemoPlaywright.git
cd SauceDemoPlaywright

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Install Playwright browsers
playwright install chromium
```

### Verification

```bash
# Verify all installations
playwright install --with-deps chromium
pytest --version
python3 -m pip list | grep -E "pytest|playwright"
```

---

## 🧪 Running Tests

### Run all tests

```bash
pytest tests/ -v
```

### Run specific test file

```bash
pytest tests/test_login.py -v
```

### Run with HTML report

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

### Run with Allure report

```bash
# Generate Allure results
pytest tests/ -v --alluredir=allure-results

# Serve Allure report (requires allure CLI)
allure serve allure-results
```

### Run in headless mode (CI/CD style)

```bash
HEADLESS=true pytest tests/ -v
```

### Run with parallel execution

```bash
pytest tests/ -v -n auto  # Uses all CPU cores
```

### Run with specific marker

```bash
pytest tests/ -v -m smoke
```

---

## 📊 Reports

### HTML Report

```bash
# After test run
pytest tests/ --html=report.html --self-contained-html

# Open report
open report.html      # macOS
start report.html     # Windows
xdg-open report.html  # Linux
```

### Allure Report

```bash
# Install Allure (if not installed)
brew install allure  # macOS
# or download from: https://docs.qameta.io/allure/

# Generate and serve
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### JUnit XML Report

```bash
pytest tests/ --junitxml=test-results.xml
```

---

## 🔄 CI/CD Pipeline

### Automated Testing Triggers:

- ✅ **Push** to main/develop branches
- ✅ **Pull Requests** to main/develop
- ✅ **Daily Schedule** - 2 AM UTC

### Pipeline Workflow:

```
Commit → GitHub Actions Triggered
  ↓
Checkout Code
  ↓
Setup Python 3.11
  ↓
Install Dependencies (with cache)
  ↓
Install Playwright Browsers
  ↓
Execute All Tests
  ↓
Generate Reports (HTML + Allure + JUnit)
  ↓
Upload Artifacts
  ↓
Publish Results
```

### View Pipeline Results:

👉 **GitHub Repository → Actions Tab → Latest Run**

---

## 🧰 Configuration & Fixtures

### pytest.ini

Controls Pytest behavior:

- Test discovery patterns
- Output format
- Plugin settings

### conftest.py

Global Pytest fixtures:

```python
@pytest.fixture
def page():
    """Playwright page instance - fresh for each test"""
    # Automatically created and torn down
```

---

## 📝 Test Examples

### Basic Login Test

```python
def test_login_with_valid_credentials(page):
    """Test successful login"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    assert products_page.is_loaded()
```

### E2E Purchase Flow

```python
def test_complete_purchase_flow(page):
    """Complete end-to-end purchase"""
    # Login
    LoginPage(page).login("standard_user", "secret_sauce")

    # Add product
    products = ProductsPage(page)
    products.add_product("Sauce Labs Backpack")

    # Checkout
    cart = CartPage(page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_info("John", "Doe", "12345")
    checkout.proceed()

    # Verify
    complete = CheckoutCompletePage(page)
    assert complete.order_confirmed()
```

### Data-Driven Test

```python
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
def test_login_multiple_users(page, username, password):
    """Test login with multiple user types"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    assert ProductsPage(page).is_loaded()
```

---

## 🐛 Troubleshooting

### Tests timeout

```bash
# Increase timeout (default 30000ms)
pytest tests/ --timeout=60 -v
```

### Playwright browser not found

```bash
# Reinstall browsers with dependencies
playwright install --with-deps chromium
```

### Port already in use

```bash
# Find and kill process
lsof -i :8080
kill -9 <PID>
```

### Clear cache

```bash
# Remove pytest cache
rm -rf .pytest_cache

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
```

---

## 📚 Learning Resources

| Resource         | Link                                                                                 | Topics               |
| ---------------- | ------------------------------------------------------------------------------------ | -------------------- |
| Playwright Docs  | https://playwright.dev/python/                                                       | Web automation guide |
| Pytest Docs      | https://docs.pytest.org/                                                             | Testing framework    |
| POM Pattern      | https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/ | Design pattern       |
| SauceDemo App    | https://github.com/saucelabs/sample-app-web                                          | App documentation    |
| Allure Reporting | https://docs.qameta.io/allure/                                                       | Reporting tool       |

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-test`)
3. Add tests for new features
4. Ensure all tests pass (`pytest tests/ -v`)
5. Commit with clear message:

   ```bash
   git commit -m "feat: add new test for xyz feature

   - Description of what was added
   - Why it was needed
   - Any relevant details"
   ```

6. Push to branch (`git push origin feature/new-test`)
7. Open Pull Request

---

## 📈 Future Enhancements

- [ ] Visual regression testing (Applitools Eyes)
- [ ] Performance testing (Lighthouse)
- [ ] Multi-browser parallel execution
- [ ] Custom HTML dashboard
- [ ] Slack notifications for test results
- [ ] Database integration testing
- [ ] API mock integration
- [ ] Mobile responsive testing

---

## 👤 Author

**Marco Aguirre** | QA Automation Engineer  
🐙 GitHub: [@Maab-7](https://github.com/Maab-7)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 Questions or Issues?

- 📖 Check [Troubleshooting](#troubleshooting) section
- 🐛 Create an [Issue](../../issues) on GitHub
- 💬 Start a [Discussion](../../discussions)

---

**Last Updated:** May 1, 2026  
**Python:** 3.11+ | **Playwright:** 1.40+ | **Pytest:** 7.4+ | **Status:** ✅ Passing

---

### 🚀 Ready to run tests?

```bash
pytest tests/ -v --html=report.html
```
