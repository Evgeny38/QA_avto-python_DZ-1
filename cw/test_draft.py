from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
import time
import unittest


class TestDataTypesForm(unittest.TestCase):

    def setUp(self):
        # Можно использовать Edge или Safari — ниже примеры для обоих

        # Для Edge:
        self.driver = webdriver.Edge()

        # Для Safari (требуется включить «Разработка» → «Разрешить Remote
        # Automation» в Safari):
        # self.driver = webdriver.Safari()

        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def tearDown(self):
        self.driver.quit()

    def test_form_validation(self):
        driver = self.driver
        # wait = self.wait
        # Заполняем форму
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "zip-code").send_keys("")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            "button[type='submit']")
        submit_button.click()

        # Ожидание применения валидации (некоторое время после отправки)
        time.sleep(5)

        # Проверяем подсветку полей

        # 1. Zip code должен быть подсвечен красным (обычно через наличие
        # класса error или красной границы)
        zip_code_field = driver.find_element(By.NAME, "zip-code")
        zip_code_class = zip_code_field.get_attribute("class")
        self.assertIn("error", zip_code_class.lower(),
                      "Поле Zip code не подсвечено красным "
                      "(ожидался класс с 'error')")

        # 2. Проверяем, что остальные поля подсвечены зелёным
        # Предполагаем, что зелёная подсветка — это отсутствие класса error и
        #  наличие класса success
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_name in fields_to_check:
            field = driver.find_element(By.NAME, field_name)
            field_class = field.get_attribute("class").lower()

            # Проверяем, что нет класса error
            self.assertNotIn("error", field_class, f"Поле {field_name} \
                             подсвечено красным, но должно быть зелёным")

            # Дополнительно можно проверить наличие класса success,
            # если он используется
            # self.assertIn("success", field_class,
            #                 f"Поле {field_name} не подсвечено зелёным
            # (ожидался класс 'success')")


if __name__ == "__main__":
    unittest.main()
