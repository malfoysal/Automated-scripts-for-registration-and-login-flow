from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Initialize WebDriver
driver = webdriver.Chrome()

# URL
base_url = "https://parabank.parasoft.com/parabank/index.htm"

# Wait
wait = WebDriverWait(driver, 10)

def test_registration():
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Register").click()

    # Positive Scenario: Valid Data Entry
    try:
        driver.find_element(By.ID, "customer.firstName").send_keys("John")
        driver.find_element(By.ID, "customer.lastName").send_keys("Doe1")
        driver.find_element(By.ID, "customer.address.street").send_keys("123 Elm St")
        driver.find_element(By.ID, "customer.address.city").send_keys("Springfield")
        driver.find_element(By.ID, "customer.address.state").send_keys("IL")
        driver.find_element(By.ID, "customer.address.zipCode").send_keys("62701")
        driver.find_element(By.ID, "customer.phoneNumber").send_keys("1234567890")
        driver.find_element(By.ID, "customer.ssn").send_keys("123-45-6789")
        driver.find_element(By.ID, "customer.username").send_keys("john_doe3")
        driver.find_element(By.ID, "customer.password").send_keys("password123")
        driver.find_element(By.ID, "repeatedPassword").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]"))
        )
        assert success_message.is_displayed(), "Registration failed!"
        print("Registration successful.")
    except NoSuchElementException as e:
        print("Element not found:", e)

def test_login():
    driver.get(base_url)

    # Positive Scenario: Valid Login
    try:
        driver.find_element(By.NAME, "username").send_keys("john_doe3")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

        dashboard = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Accounts Overview')]"))
        )
        assert dashboard.is_displayed(), "Login failed!"
        print("Login successful.")
    except NoSuchElementException as e:
        print("Element not found:", e)

# Run Tests
test_registration()
test_login()

# Close Browser

