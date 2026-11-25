# SauceDemo Playwright E2E Tests

End-to-end test automation for [SauceDemo](https://www.saucedemo.com/) using Playwright, Python, and pytest. The project follows the Page Object Model (POM) and runs in GitHub Actions.

## Tests

| File | Test | Description |
|---|---|---|
| `tests/test_login.py` | `test_login_success` | Valid credentials redirect to the Products page |
| `tests/test_login.py` | `test_e2e` | Full purchase flow: login, add to cart, checkout, order confirmation |

The end-to-end test also checks that the order total equals the subtotal plus tax.

## Tech Stack

- Python 3.11+
- Playwright (Python)
- pytest
- Allure reports
- GitHub Actions

## Project Structure

```
pages/            Page objects (login, products, cart, checkout)
tests/            Test files
conftest.py       Shared pytest fixtures
pytest.ini        pytest configuration
requirements.txt  Dependencies
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run the end-to-end test only
pytest tests/test_login.py::test_e2e -v

# Generate Allure results and open the report (requires the Allure CLI)
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```

## CI

The GitHub Actions workflow in `.github/workflows/tests.yml` runs on pushes and pull requests to `main` and `develop`, and daily at 02:00 UTC. It installs dependencies, runs the test suite, and publishes the results.

## Possible Improvements

- Negative login tests (invalid credentials, locked-out user)
- Data-driven login tests with `pytest.mark.parametrize`
- Split the end-to-end test into smaller checkout tests

## Author

Marco Antonio Alfaro Bustillos, QA Engineer

## License

MIT
