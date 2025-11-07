from selenium.webdriver.common.by import By

from .utils import driver as _driver, wait_for, navigate


def test_finance_assessment_happy_path(driver):
    navigate(driver, "/riskassessment")

    # Finance form fields
    age = wait_for(driver, By.XPATH, "//label[contains(.,'Age')]/following::input[1]")
    age.clear(); age.send_keys("30")

    gender_select = wait_for(driver, By.XPATH, "//label[contains(.,'Gender')]/following::button[1]")
    gender_select.click()
    male = wait_for(driver, By.XPATH, "//div[@role='option' and .='Male']")
    male.click()

    edu_select = wait_for(driver, By.XPATH, "//label[contains(.,"""Education Level""")]/following::button[1]")
    edu_select.click()
    edu_item = wait_for(driver, By.XPATH, "//div[@role='option' and .="""Bachelor's"""]")
    edu_item.click()

    status_select = wait_for(driver, By.XPATH, "//label[contains(.,'Marital Status')]/following::button[1]")
    status_select.click()
    married = wait_for(driver, By.XPATH, "//div[@role='option' and .='Married']")
    married.click()

    income = wait_for(driver, By.XPATH, "//label[contains(.,'Income')]/following::input[1]")
    income.send_keys("120000")

    loan = wait_for(driver, By.XPATH, "//label[contains(.,'Loan Amount')]/following::input[1]")
    loan.send_keys("10000")

    credit = wait_for(driver, By.XPATH, "//label[contains(.,'Credit Score')]/following::input[1]")
    credit.send_keys("780")

    purpose = wait_for(driver, By.XPATH, "//label[contains(.,'Loan Purpose')]/following::button[1]")
    purpose.click()
    purpose_item = wait_for(driver, By.XPATH, "//div[@role='option' and .='Personal']")
    purpose_item.click()

    employment = wait_for(driver, By.XPATH, "//label[contains(.,'Employment Status')]/following::button[1]")
    employment.click()
    employed = wait_for(driver, By.XPATH, "//div[@role='option' and .='Employed']")
    employed.click()

    years = wait_for(driver, By.XPATH, "//label[contains(.,'Years at Current Job')]/following::input[1]")
    years.send_keys("5")

    payment = wait_for(driver, By.XPATH, "//label[contains(.,'Payment History')]/following::button[1]")
    payment.click()
    good = wait_for(driver, By.XPATH, "//div[@role='option' and .='Good']")
    good.click()

    assets = wait_for(driver, By.XPATH, "//label[contains(.,'Assets Value')]/following::input[1]")
    assets.send_keys("250000")

    dependents = wait_for(driver, By.XPATH, "//label[contains(.,'Number of Dependents')]/following::input[1]")
    dependents.send_keys("1")

    defaults = wait_for(driver, By.XPATH, "//label[contains(.,'Previous Defaults')]/following::input[1]")
    defaults.send_keys("0")

    # Submit
    submit = wait_for(driver, By.XPATH, "//button[contains(.,'Submit')]")
    submit.click()

    # Expect result block showing Risk Rating
    wait_for(driver, By.XPATH, "//h3[contains(.,'Finance Risk Rating')]")


