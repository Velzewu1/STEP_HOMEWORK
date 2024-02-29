import os
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By

from pathlib import Path

def get_platform() -> str:
    """
    A function that returns the platform as a string.
    """
    # Определяем операционную систему
    return platform.system()

def load_chrome_driver(platform: str) -> webdriver.Chrome:
    """
    Load the Chrome driver based on the given platform and return the loaded webdriver.Chrome object.

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

driver = load_chrome_driver(webdriver.Chrome())
driver.get("https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut")

numbers = driver.find_elements(By.TAG_NAME, "td")
elements = driver.find_elements(By.CLASS_NAME, "text-left")

currencies = {}
for el in elements:
    for num in numbers:
        try:
            currencies[el.text] = float(num.text)
        except ValueError as e:
            pass
print(currencies)


        
