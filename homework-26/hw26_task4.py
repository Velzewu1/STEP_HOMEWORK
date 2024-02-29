"""Task 4"""
from bs4 import BeautifulSoup
import requests

def get_weather():
    """Gets weather using Bs4"""
    page = requests.get("https://yandex.kz/pogoda/astana", timeout=200)
    soup = BeautifulSoup(page.text, "html.parser")
    real_temp = soup.findAll("span", class_="temp__value temp__value_with-unit")[1]
    feel_temp = soup.findAll("span", class_="temp__value temp__value_with-unit")[2]

    return real_temp.text, feel_temp.text

if __name__ == "__main__":
    weather = get_weather()
    print("Real temperature:", weather[0])
    print("Feel temperature:", weather[1])
    