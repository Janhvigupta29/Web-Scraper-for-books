import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://books.toscrape.com/"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("h3")

    table_data = [(idx, book.get_text(strip=True)) for idx, book in enumerate(books, start=1)]

    print("\n      *** -- Books Found -- ***")
    print(tabulate(table_data, headers=["No.", "Book Title"], tablefmt="fancy_grid"))

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")