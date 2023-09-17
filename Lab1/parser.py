import os

from bs4 import BeautifulSoup
import requests

from Lab1.logic_search import path


def collect(url, name):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "lxml")
    file_name = path + "\\" + name + ".txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(soup.text)

    result = []
    for root, dirs, files in os.walk(path, topdown=False):
        for index, name in enumerate(files, start=1):
            result.append(name)

    return result


def main():
    collect("https://nice-books.ru/books/fantastika-i-fjentezi/"
            "boevaja-fantastika/309924-oranzhereya-na-krayu-sveta-kim-chhoep.html")


if __name__ == '__main__':
    main()