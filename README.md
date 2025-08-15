<h1>📚 Web Scraper for books Project</h1>

<h2>📖 Overview</h2>
This project demonstrates a Python-based web scraper that extracts book titles from the Books to Scrape website using requests and BeautifulSoup.
The extracted data is then displayed in a well-formatted table for easy readability.


<h2>🛠 Features</h2>

1. Scrapes book titles from the given website.
2. Uses BeautifulSoup for HTML parsing.
3. Displays data in tabular format using the tabulate library.
4. Handles HTTP requests with custom User-Agent for better compatibility.


<h2>📦 Installation</h2>

1️⃣ Clone this repository
git clone [https://github.com/your-username/books-to-scrape.git](https://github.com/Janhvigupta29/Web-Scraper-for-books)
cd books-to-scrape

2️⃣ Install dependencies
pip install -r requirements.txt (Make sure you have Python 3 installed.)


<h2>📜 Code Explanation</h2>

Import Libraries — requests for fetching web pages, BeautifulSoup for parsing HTML, tabulate for formatting tables.

Set URL & Headers — Use a proper User-Agent to mimic a browser request.

Fetch & Parse HTML — Extract all tags containing book titles.

Display in Table — Show results neatly using tabulate.

<h2>🧰 Requirements</h2>

Python 3.x

requests

beautifulsoup4

tabulate

Install them manually:

pip install requests beautifulsoup4 tabulate

<h2>⚠ Disclaimer</h2>

This project is for educational purposes only. Please ensure you comply with the website's terms of service when scraping.

<h2>💡 Future Improvements</h2>

Add author names & prices to the table.

Export data to CSV or JSON.

Use rich library for colorful tables.

Implement pagination to scrape all pages.

<h2>👩‍💻 Author</h2>

Janhvi Gupta
💼 Aspiring Engineer | 💻 Full Stack Developer in Progress | 📊 Tech Enthusiast
