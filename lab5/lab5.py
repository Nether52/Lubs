# --------------------------
# Імпорти бібліотек
# --------------------------
import requests          # HTTP-запити (отримання даних з інтернету)
import numpy             # Робота з масивами та математичними операціями
import pandas            # Робота з таблицями (DataFrame)
from PIL import Image    # Бібліотека Pillow — робота з зображеннями
import matplotlib.pyplot as plt   # Побудова графіків
from dateutil import parser       # Розбір дат у різних форматах
from bs4 import BeautifulSoup     # Парсинг HTML-коду
from tqdm import tqdm              # Прогрес-бар для циклів
from rich.console import Console   # Красива кольорова консоль
import pyfiglet                   # ASCII-арт із тексту

console = Console()  # Створюємо консоль для rich


# --------------------------
# 1. Використання requests
# --------------------------
try:
    # GET-запит до API, отримання JSON
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1") #робить HTTP-запит до сайту
    print("Requests result:", response.json())  #перетворює JSON у Python-об’єкт (словник)
except Exception as e:
    print("Requests error:", e)


# --------------------------
# 2. Використання numpy
# --------------------------
try:
    arr = numpy.array([1, 2, 3])   # Створення NumPy масиву
    print("NumPy sum:", arr.sum()) # Обчислення суми елементів масиву
except Exception as e:
    print("NumPy error:", e)


# --------------------------
# 3. Використання pandas
# --------------------------
try:
    # Створюємо просту таблицю
    df = pandas.DataFrame({"A": [1, 2], "B": [3, 4]})
    print("Pandas DataFrame:")  #Тут створюється таблиця DataFrame з двома колонками: колонка A → значення [1, 2], колонка B → значення [3, 4]
    print(df)
except Exception as e:
    print("Pandas error:", e)


# --------------------------
# 4. Використання matplotlib
# --------------------------
try:
    # Побудова простого графіка
    plt.plot([1, 2, 3], [3, 1, 4]) #перша дужка — це X-координати,друга — це Y-координати.
    plt.title("Test plot")      # Назва графіку
    plt.savefig("plot.png")     # Збереження у файл
    print("Matplotlib: графік збережено як plot.png")
except Exception as e:
    print("Matplotlib error:", e)


# --------------------------
# 5. Використання pyfiglet + rich
# --------------------------
try:
    ascii_art = pyfiglet.figlet_format("Lab 5!")  # Створюємо ASCII-текст який складається тільки з простих символів, без картинок, без форматування, без стилів
    console.print(ascii_art)                      # Виводимо красиво через бібліотеку rich
except Exception as e:
    print("pyfiglet error:", e)