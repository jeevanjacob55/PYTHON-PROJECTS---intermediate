# 🏠 Zillow Rental Scraper

This Python script automates the process of scraping real estate rental listings from [Zillow](https://www.zillow.com) and submitting the information into a **Google Form** using **Selenium** and **BeautifulSoup**.

---

## 🔍 Features

- Scrapes rental data: address, price, and listing URL from Zillow.
- Fills out a Google Form with each listing's information.
- Fully automated using Selenium and ChromeDriver.

---

## 🧰 Technologies Used

- `selenium` – Browser automation.
- `bs4` (BeautifulSoup) – HTML parsing and scraping.
- `requests` – Fetching page content.
- `dotenv` – Managing environment variables securely.

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
pip install -r requirements.txt
### 2. Set Environment Variables
- Create a .env file in the project root and include:


-CHROME_PATH=/path/to/your/chromedriver
-Replace with the actual path to your ChromeDriver.

### 3. Run the Script

python main.py