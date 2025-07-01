💻 PRODIGY_ST_04: Cross-Browser Testing with BrowserStack

📌 Internship Task - 04 | Prodigy InfoTech

This project involves conducting cross-browser testing using BrowserStack's Selenium Grid to ensure a login page behaves consistently across different browsers and platforms.

🌐 Site Under Test

https://www.saucedemo.com/

🎯 Objective

To run automated Selenium test scripts across different browsers and devices using BrowserStack.

To identify layout issues, functionality differences, or broken elements across:

Chrome (Windows)

Firefox (macOS)

Safari (macOS)

Edge (Windows)

🛠️ Tools & Technologies

Selenium WebDriver

Python

BrowserStack (Cloud Testing Platform)

GitHub (Version Control)

🪜 Steps Followed

1. Environment Setup

Python installed

Selenium installed using: pip install selenium

Created project folder with virtual environment

Created requirements.txt

2. BrowserStack Setup

Created BrowserStack account

Retrieved username and access_key

3. Selenium Script for Login Test

from selenium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': 'latest',
    'name': 'Login Test - Chrome',
    'build': 'PRODIGY_ST_04'
}

USERNAME = 'your_browserstack_username'
ACCESS_KEY = 'your_browserstack_access_key'

url = f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'
driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

assert "inventory" in driver.current_url
driver.quit()

4. Testing Across Browsers

Modified desired_cap for each test run to test on:

Chrome (Windows 10)

Firefox (macOS Monterey)

Safari (OS X Catalina)

Edge (Windows 11)

✅ Test Results Summary

Browser

OS

Issue Found

Status

Chrome

Windows 10

No issues

✅ Pass

Firefox

macOS

Slight input lag

⚠️ Minor

Safari

macOS

UI slightly misaligned

⚠️ Minor

Edge

Windows 11

No issues

✅ Pass

📄 Task Report File

TASK-04_CrossBrowser_Report.md

📁 Folder Structure

PRODIGY_ST_04/
├── test_login_browserstack.py
├── requirements.txt
├── README.md
└── TASK-04_CrossBrowser_Report.md

🔗 GitHub Repository

https://github.com/ITRENUKAS/PRODIGY_ST_04

🧑‍💼 LinkedIn Post Template

✅ Completed Task-04 of my Software Testing Internship at Prodigy InfoTech!

🔍 Performed Cross-Browser Testing using BrowserStack’s Selenium Grid on https://www.saucedemo.com.

💻 Browsers tested:
- Chrome (Windows)
- Firefox (macOS)
- Safari (macOS)
- Edge (Windows)

🧪 Tools used:
- Selenium WebDriver
- BrowserStack

🚀 GitHub: https://github.com/ITRENUKAS/PRODIGY_ST_04

#ProdigyInfoTech #Selenium #BrowserStack #SoftwareTesting #CrossBrowserTesting

📌 Status

✅ Task-04 Completed
