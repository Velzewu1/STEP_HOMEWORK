"""TAsk 6"""
import os
import platform

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_platform() -> str:
    """
    A function that returns the platform as a string.
    """
    # Определяем операционную систему
    return platform.system()

def load_chrome_driver(platform: str) -> webdriver.Chrome:
    """
    Load the Chrome driver based on the given platform and return the loaded webdriver.Chrome object

    Args:
        platform (str): The platform for which the Chrome driver is being loaded.

    Returns:
        webdriver.Chrome: The loaded Chrome webdriver object.
    """
    # Загружаем драйвер Chrome
    chrome_driver_path = str(
        Path(__file__).parent / "parser_drivers" / "chromedriver" / "chromedriver"
    )

    platform = get_platform()

    if platform == "Windows":
        os.environ["PATH"] = chrome_driver_path + ".exe"
    elif platform == "Linux":
        os.environ["PATH"] = chrome_driver_path
    else:
        raise Exception("Не поддерживаемая операционная система")

    return webdriver.Chrome()

if __name__ == "__main__":
    URL = "https://kaspi.kz/shop/c/computers/?utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_common_new&gclid=CjwKCAiA0PuuBhBsEiwAS7fsNTVDtwGuZhuOWqi4sEazR0gEj8N72cXTHMxrbxS9wuzLn1Zdy4DMdxoCAfMQAvD_BwE"
    driver = load_chrome_driver(webdriver.Chrome())
    driver.get(URL)

    elements = driver.find_elements(By.CLASS_NAME, "item-card__prices-price")

    for el in elements:
        print(el.text)
