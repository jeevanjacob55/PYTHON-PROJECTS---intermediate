# 🎵 Musical Time Machine

Create a personalized **Spotify playlist** of the Billboard Hot 100 songs from any past date — just input a date, and the program does the rest!

---

## 📌 What This Project Does

- Prompts the user to enter a date in `YYYY-MM-DD` format.
- Scrapes the Billboard Hot 100 chart from that date using `BeautifulSoup`.
- Searches each song on **Spotify** using the **Spotify Web API**.
- Automatically creates a **private playlist** in your Spotify account with those top tracks.

---

## 🛠️ Tools & Concepts Used

- `BeautifulSoup` & `Requests` – Web scraping and HTTP handling.
- `spotipy` – Spotify Web API wrapper.
- `re` – Regex-based input validation.

---

## 🧾 Setup Instructions

### 1. Clone This Repository
### 2. Install required packages (pip install -r requirements.txt)
### 3. Create a Spotify Developer App
 - goto https://developer.spotify.com/
 - Create an app and get:
 - Client ID
 - Client Secret
 - Create A Redirect URL www.example.com

Set a redirect URI, e.g., http://example.com
### 4. Create a .env File
 - Add the following
 - CLIENT_ID=your_spotify_client_id
 - CLIENT_SECRET=your_spotify_client_secret
### 5. Run main.py