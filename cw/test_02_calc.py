from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_calculator_with_wait():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("3")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 7)

    # Ждём, пока результат в элементе result станет равным "15"
    # result = wait.until(
    #     EC.text_to_be_present_in_element((By.ID, "screen"), "15")
    # )

    result = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    # result = wait.until(EC.visibility_of_element_located((By.XPATH, "\
    # //div[contains(text() = '15')]")))

    # result = wait.until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "screen"), "15"))

    # # Проверяем, что результат равен "15"

    # assert result == "15", f"Ожидалось 15, но получено: {result}"
    print(result)
    sleep(5)
    driver.quit()
