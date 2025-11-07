from selenium.webdriver.common.by import By

from .utils import driver as _driver, wait_for, navigate


def test_health_assessment_happy_path(driver):
    navigate(driver, "/riskassessment")

    # Health form fields
    gender_btn = wait_for(driver, By.XPATH, "//h2[contains(.,'Health Risk Assessment')]/../../..//label[contains(.,'Gender')]/following::button[1]")
    gender_btn.click()
    male = wait_for(driver, By.XPATH, "//div[@role='option' and .='Male']")
    male.click()

    age = wait_for(driver, By.XPATH, "//h2[contains(.,'Health Risk Assessment')]/../../..//label[contains(.,'Age')]/following::input[1]")
    age.clear(); age.send_keys("40")

    edu_btn = wait_for(driver, By.XPATH, "//h2[contains(.,'Health Risk Assessment')]/../../..//label[contains(.,'Education')]/following::button[1]")
    edu_btn.click()
    edu_item = wait_for(driver, By.XPATH, "//div[@role='option' and .="""Bachelor's"""]")
    edu_item.click()

    smoker_btn = wait_for(driver, By.XPATH, "//label[contains(.,'Current Smoker')]/following::button[1]")
    smoker_btn.click()
    no_item = wait_for(driver, By.XPATH, "//div[@role='option' and .='No']")
    no_item.click()

    cigs = wait_for(driver, By.XPATH, "//label[contains(.,'Cigarettes Per Day')]/following::input[1]")
    cigs.send_keys("0")

    bpmeds_btn = wait_for(driver, By.XPATH, "//label[contains(.,'Blood Pressure Medicines')]/following::button[1]")
    bpmeds_btn.click()
    bp_no = wait_for(driver, By.XPATH, "//div[@role='option' and .='No']")
    bp_no.click()

    stroke_btn = wait_for(driver, By.XPATH, "//label[contains(.,'Prevalent Stroke')]/following::button[1]")
    stroke_btn.click()
    stroke_no = wait_for(driver, By.XPATH, "//div[@role='option' and .='No']")
    stroke_no.click()

    hyp_btn = wait_for(driver, By.XPATH, "//label[contains(.,'Prevalent Hypertension')]/following::button[1]")
    hyp_btn.click()
    hyp_no = wait_for(driver, By.XPATH, "//div[@role='option' and .='No']")
    hyp_no.click()

    diab_btn = wait_for(driver, By.XPATH, "//label[contains(.,'Diabetes')]/following::button[1]")
    diab_btn.click()
    diab_no = wait_for(driver, By.XPATH, "//div[@role='option' and .='No']")
    diab_no.click()

    totchol = wait_for(driver, By.XPATH, "//label[contains(.,'Total Cholesterol')]/following::input[1]")
    totchol.send_keys("180")

    sys = wait_for(driver, By.XPATH, "//label[contains(.,'Systolic Blood Pressure')]/following::input[1]")
    sys.send_keys("118")

    dia = wait_for(driver, By.XPATH, "//label[contains(.,'Diastolic Blood Pressure')]/following::input[1]")
    dia.send_keys("78")

    bmi = wait_for(driver, By.XPATH, "//label[contains(.,'BMI')]/following::input[1]")
    bmi.send_keys("22.5")

    hr = wait_for(driver, By.XPATH, "//label[contains(.,'Heart Rate')]/following::input[1]")
    hr.send_keys("70")

    glu = wait_for(driver, By.XPATH, "//label[contains(.,'Glucose')]/following::input[1]")
    glu.send_keys("95")

    submit = wait_for(driver, By.XPATH, "//h2[contains(.,'Health Risk Assessment')]/../../..//button[contains(.,'Submit')]")
    submit.click()

    # Expect result block showing Health Prediction Result
    wait_for(driver, By.XPATH, "//h3[contains(.,'Health Prediction Result')]")


