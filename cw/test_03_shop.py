from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_shopping_cart_total():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    sleep(3)
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # Словарь: название товара → кнопка "Add to cart"
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    # sleep(3)
    # Добавляем каждый товар в корзину
    for item_name in items_to_add:
        # Формируем локатор кнопки по тексту
        add_button = driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        add_button.click()

    cart_badge = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_badge.click()
    # sleep(3)
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    driver.find_element(By.ID, "first-name").send_keys("Вася")
    driver.find_element(By.ID, "last-name").send_keys("Слон")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # Ждём, пока загрузится страница итогов
    total_label = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    # Получаем текст итоговой суммы: "Total: $58.29"
    total_text = total_label.text.strip()

    # Извлекаем число: убираем "Total: $" и преобразуем в float
    total_value = float(total_text.replace("Total: $", ""))

    # Проверяем, что итоговая сумма равна 58.29
    assert total_value == 58.29, \
        f"Ожидалось $58.29, но получено: ${total_value}"

    print(f"Итоговая сумма: ${total_value} — проверка пройдена.")
    sleep(5)

    driver.quit()
