# 💼 LinkedIn Job Saver Bot

This Python automation bot uses **Selenium** to log in to LinkedIn, search for jobs based on a query and location, and automatically save all available job listings.

---

## 🔍 Features

- Opens LinkedIn and navigates to a specific job search.
- Logs in using user credentials.
- Clicks on each job card and saves the job.
- Handles exceptions where save button isn't found.

---

## 🧰 Technologies Used

- `selenium` for browser automation.
- `dotenv` for secure environment variable management.

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Create a env file
- EMAIL=your_email@example.com
- PASSWORD=your_linkedin_password
- CHROME_PATH=/path/to/your/chromedriver

### 3. Run main.py
