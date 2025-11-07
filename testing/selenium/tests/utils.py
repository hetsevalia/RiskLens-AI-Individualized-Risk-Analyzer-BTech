import os
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = os.environ.get("RISKLENS_BASE_URL", "http://localhost:3000")


def create_driver(headless: bool = True) -> webdriver.Chrome:
    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1440,900")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.implicitly_wait(2)
    return driver


@pytest.fixture()
def driver() -> Generator[webdriver.Chrome, None, None]:
    d = create_driver(headless=True)
    try:
        yield d
    finally:
        d.quit()


def wait_for(driver: webdriver.Chrome, by: By, value: str, timeout: int = 10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


def go_home(driver: webdriver.Chrome):
    driver.get(BASE_URL)
    wait_for(driver, By.CSS_SELECTOR, "a[href='/riskassessment']")


def navigate(driver: webdriver.Chrome, path: str):
    driver.get(f"{BASE_URL}{path}")


