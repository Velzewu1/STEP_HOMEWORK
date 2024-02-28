"""Madlibs"""
from random import randint
import requests 
from bs4 import BeautifulSoup

def get_page(url):
    """Gets page"""
    return requests.get(url, timeout=200)

def get_html(page):
    """Gets html"""
    return BeautifulSoup(page.text, "html.parser").findAll("div", "anekdot")

if __name__ == "__main__":
    anekdot_list = get_html(get_page("http://www.anekdotov.net/"))
    rand_num = randint(1, len(anekdot_list))

    ANEKDOT = str(anekdot_list[rand_num].text)
    while ANEKDOT == "Умные мысли приходят лишь тогда, когда все глупости уже сделаны":
        ANEKDOT = str(anekdot_list[rand_num].text)

    indexes = []
    word_list = ANEKDOT.lower().split()
    print(ANEKDOT)
    while True:
        letter = input("Введите букву: ")
        chosen_words = []
        for word in word_list:
            if word.startswith(letter) is True:
                chosen_words.append(word)
                indexes.append(word_list.index(word))

        if len(chosen_words) < 3:
            indexes = []
            continue
        else:
            break


    to_change = chosen_words
    print(chosen_words)
    print(indexes)

    first_word = input("Введите существительное: ")
    second_word = input("Введите глагол: ")
    third_word = input("Введите прилагательное: ")

    change_word = [first_word, second_word, third_word]


    for i in range(0, 3):
        chosen_words[i] = change_word[i]

    ITER_COUNT = 0
    for i in indexes:
        word_list[i] = chosen_words[ITER_COUNT].upper()
        ITER_COUNT += 1

    print(" ".join(word_list))
