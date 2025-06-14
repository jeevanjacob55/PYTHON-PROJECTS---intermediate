# 📉 Amazon Price Tracker

This Python script monitors the price of a specific Amazon product and sends you an **email alert** when the price drops below a specified threshold.

---

## 🚀 What It Does

- Scrapes the current price of a product from its Amazon page.
- Parses the price using `BeautifulSoup`.
- If the price is lower than your set threshold, it sends you an **email alert** with the product link.

---

## 🧰 Tools & Libraries Used

- `requests` – To fetch the product page HTML.
- `BeautifulSoup` – For scraping the price from the HTML.
- `smtplib` – For sending email alerts.
- Amazon product metadata and pricing.

---

## ⚙️ How to Set It Up

### 1. Clone the Repository
- change directory by using -cd Amazon-Price-Tracker
-install required packages

### 2. Configure Your Email Credentials
- store your credentials in a .env file
- USER_EMAIL=your_email@gmail.com
- PASS=your_password

### 3. Set The Price Threshold

- Update the condition in your script (currently set to min(prices) < 100) to the price you want to monitor.

