# ✈️ Flight Club

This is an automated Python tool that tracks low-cost flight deals and notifies users via email and SMS when a deal is found below a target price. It also supports user registration and stores user data in a Google Sheet using the Sheety API.

---

## 📌 Features

- ✉️ **User Registration**: Collects first name, last name, and email to register users.
- 🌍 **Flight Search**: Uses IATA codes and a flight search API (e.g., Tequila by Kiwi) to find real-time prices.
- 📊 **Google Sheets Integration**: Reads destination data and user list via the Sheety API.
- 🔔 **Notifications**: Sends email and SMS alerts when deals are found under the user's defined price threshold.
- 🛫 **Supports Multiple Destinations**