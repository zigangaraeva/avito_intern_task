from selenium import webdriver
from selenium.webdriver.common.by import By

# активируем драйвер
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
try:
    # открытие страницы обьявления
    driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

    # поиск кнопки "избранное" и нажатие на неё
    favorite_button = driver.find_element(By.XPATH, "//div[@class='style-header-add-favorite-M7nA2']//button[@data-marker='item-view/favorite-button']")
    favorite_button.click()

    print("Успешное выполнение теста")

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # закрываем браузер
    driver.quit()
