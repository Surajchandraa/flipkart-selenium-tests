from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Firefox()

def header_test():
    try:
        header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        if "A/B Test" in header.text or "A/B Test Control" in header.text:
            print("Test Passed: A/B Test header is displayed correctly")
        else:
            print(f"Test Failed: Unexpected header text '{header.text}'")
    except Exception as e:
        print(f"Test Failed: {e}")

def title_test():
    try:
        expected_title = "The Internet"
        actual_title = driver.title
        assert expected_title in actual_title, f"Expected '{expected_title}' but got '{actual_title}'"
        print("Test Passed: Title is correct")
    except Exception as e:
        print(f"Test Failed: Title is not correct - {e}")

def elemental_selenium_link():
    try:
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/a"))
        )
        link.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/nav/div[1]/div[1]/a/div/img'))
        )
        assert "Home | Elemental Selenium" in driver.title, f"Expected title to contain 'Home | Elemental Selenium' but got {driver.title}"
        print("Test Passed: Elemental Selenium link works correctly")
    except Exception as e:
        print(f"Test Failed: Elemental Selenium link - {e}")

def run_tests():
    try:
        driver.get("https://the-internet.herokuapp.com/abtest")
        header_test()
        title_test()
        elemental_selenium_link()
    finally:
        driver.quit()

run_tests()