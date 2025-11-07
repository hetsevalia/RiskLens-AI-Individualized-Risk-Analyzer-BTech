from selenium.webdriver.common.by import By

from .utils import driver as _driver, go_home, wait_for, navigate


def test_signup_and_login(driver):
    go_home(driver)
    # Go to auth page
    navigate(driver, "/auth")

    # Switch to Sign Up
    toggle = wait_for(driver, By.XPATH, "//span[contains(text(),'Sign Up')]")
    toggle.click()

    name = wait_for(driver, By.XPATH, "//input[@placeholder='Name']")
    email = wait_for(driver, By.XPATH, "//input[@placeholder='Email']")
    password = wait_for(driver, By.XPATH, "//input[@placeholder='Password']")

    name.send_keys("Test User")
    email.send_keys("tester+demo@example.com")
    password.send_keys("Password123!")

    submit = wait_for(driver, By.XPATH, "//button[contains(.,'Sign Up')]")
    submit.click()

    # Back to Login and login with same creds
    toggle_login = wait_for(driver, By.XPATH, "//span[contains(text(),'Login')]")
    toggle_login.click()

    email_login = wait_for(driver, By.XPATH, "//input[@placeholder='Email']")
    password_login = wait_for(driver, By.XPATH, "//input[@placeholder='Password']")
    email_login.clear(); email_login.send_keys("tester+demo@example.com")
    password_login.clear(); password_login.send_keys("Password123!")

    login_btn = wait_for(driver, By.XPATH, "//button[contains(.,'Login')]")
    login_btn.click()

    # Expect redirect to home
    wait_for(driver, By.XPATH, "//a[@href='/riskassessment' and contains(.,'Get My Risk Score')]")


def test_admin_login(driver):
    navigate(driver, "/auth")
    email = wait_for(driver, By.XPATH, "//input[@placeholder='Email']")
    password = wait_for(driver, By.XPATH, "//input[@placeholder='Password']")
    email.send_keys("admin@gmail.com")
    password.send_keys("admin")

    login_btn = wait_for(driver, By.XPATH, "//button[contains(.,'Login')]")
    login_btn.click()

    # Admin dashboard access
    wait_for(driver, By.XPATH, "//h1[contains(.,'Dashboard') or contains(.,'Admin')]")


