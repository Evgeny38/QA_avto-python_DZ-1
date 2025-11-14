from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


# self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver = webdriver.Edge()
wait = WebDriverWait(driver, 30)


def test_form():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip-code оставляем пустым
    driver.find_element(By.NAME, "zip-code").send_keys("")
    # driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(123)
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    # Нажимаем кнопку Submit
    submit_button = driver.find_element(By.CSS_SELECTOR,
                                        "button[type='submit']")
    submit_button.click()

    # Проверяем, что поле Zip code подсвечено красным
    # (класс "alert-danger")
    # zip_code_field = driver.find_element(By.ID, "zip-code")
    # assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле\
    # Zip-code должно быть красным!"

    # Проверяем поля на цвет (красные-пустые, зелёные полные)
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "zip-code", "city", "country", "job-position", "company"
    ]

    # for field_name, value in fields_to_check:
    for field_name in fields_to_check:
        field = driver.find_element(By.NAME, field_name)
        field_class = field.get_attribute("class")
        # Поле пустое → должно быть красным (alert-danger)
        assert "alert-danger" in field_class, f"Поле {field_name} пустое,\
                но НЕ подсвечено красным!"
        print(f"Поле {field_name} пустое — подсвечено красным.")
        # Поле заполнено → должно быть зелёным (alert-success)
        assert "alert-success" in field_class, f"Поле {field_name}\
                заполнено, но НЕ подсвечено зелёным!"
        print(f"Поле {field_name} заполнено — подсвечено\
                зелёным.")
        # if value == "":
        #     # Поле пустое → должно быть красным (alert-danger)
        #     assert "alert-danger" in field_class, f"Поле {field_name} \
        # пустое,\
        #           но НЕ подсвечено красным!"
        #     print(f"Поле {field_name} пустое — подсвечено красным.")
        # else:
        #     # Поле заполнено → должно быть зелёным (alert-success)
        #     assert "alert-success" in field_class, f"Поле {field_name}\
        #           заполнено, но НЕ подсвечено зелёным!"
        #     print(f"Поле {field_name} заполнено — подсвечено\
        #            зелёным.")

    sleep(5)
    driver.quit()
