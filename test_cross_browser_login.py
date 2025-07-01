from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time

# ✅ Your BrowserStack credentials
USERNAME = "RAJA_SGYNVm"
ACCESS_KEY = "H8zKkuCCqoaQzUQibHgK"

# ✅ List of browser configurations
browsers = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Chrome"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Monterey",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Firefox"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Big Sur",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Safari"
        }
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Edge"
        }
    }
]

def run_test(capabilities):
    print(f"\n🔍 Running test on {capabilities['browserName']} ({capabilities['bstack:options']['os']} {capabilities['bstack:options']['osVersion']})")

    url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    # ✅ Use Selenium 4 syntax for capabilities
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", capabilities["browserName"])
    options.set_capability("browserVersion", capabilities["browserVersion"])
    options.set_capability("bstack:options", capabilities["bstack:options"])

    # ✅ Launch remote WebDriver session
    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        if "inventory" in driver.current_url:
            print("✅ Login successful.")
        else:
            print("❌ Login failed or unexpected redirect.")

    except NoSuchElementException as e:
        print("❌ Element not found:", e)

    finally:
        driver.quit()

# ✅ Run tests
for caps in browsers:
    run_test(caps)
