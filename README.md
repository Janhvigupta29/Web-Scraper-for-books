📚 Books to Scrape — Web Scraping Project
📖 Overview

This project demonstrates a Python-based web scraper that extracts book titles from the Books to Scrape website using requests and BeautifulSoup.
The extracted data is then displayed in a well-formatted table for easy readability.

🛠 Features

Scrapes book titles from the given website.

Uses BeautifulSoup for HTML parsing.

Displays data in tabular format using the tabulate library.

Handles HTTP requests with custom User-Agent for better compatibility.

📂 Project Structure
books-to-scrape/
│
├── books_scraper.py    # Main Python script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

📦 Installation
1️⃣ Clone this repository
git clone https://github.com/your-username/books-to-scrape.git
cd books-to-scrape

2️⃣ Install dependencies
pip install -r requirements.txt


(Make sure you have Python 3 installed.)

🚀 Usage

Run the script to scrape book titles:

python books_scraper.py


Example Output:

╒════╤════════════════════════════════════════════╕
│ No │ Book Title                                 │
╞════╪════════════════════════════════════════════╡
│ 1  │ A Light in the Attic                        │
│ 2  │ Tipping the Velvet                          │
│ 3  │ Soumission                                  │
│ 4  │ Sharp Objects                               │
│ 5  │ Sapiens: A Brief History of Humankind       │
╘════╧════════════════════════════════════════════╛

📜 Code Explanation

Import Libraries — requests for fetching web pages, BeautifulSoup for parsing HTML, tabulate for formatting tables.

Set URL & Headers — Use a proper User-Agent to mimic a browser request.

Fetch & Parse HTML — Extract all <h3> tags containing book titles.

Display in Table — Show results neatly using tabulate.

🧰 Requirements

Python 3.x

requests

beautifulsoup4

tabulate

Install them manually:

pip install requests beautifulsoup4 tabulate

⚠ Disclaimer

This project is for educational purposes only. Please ensure you comply with the website's terms of service when scraping.

💡 Future Improvements

Add author names & prices to the table.

Export data to CSV or JSON.

Use rich library for colorful tables.

Implement pagination to scrape all pages.

👩‍💻 Author

Janhvi Gupta
💼 Aspiring Engineer | 💻 Full Stack Developer in Progress | 📊 Tech Enthusiast
