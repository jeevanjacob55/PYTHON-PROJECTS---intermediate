# ✈️ Flight Deal Tracker

This project is a Python automation script that checks for low-priced flight deals and sends notifications when prices drop below a predefined threshold. It integrates with flight APIs, a Google Sheet (via Sheety), and a notification system like Twilio or email.

## 📌 Features

- Automatically checks for flights to multiple destinations.
- Retrieves flight prices using IATA codes.
- Compares live flight prices with user-defined lowest acceptable prices.
- Sends alerts via SMS/email when cheaper flights are found.

## 🧩 Modules Used

- `DataManager`: Handles reading and updating destination data from Google Sheets.
- `FlightSearch`: Searches for flights using a third-party flight API (e.g., Tequila by Kiwi).
- `FlightData`: (Not shown here, but typically formats and stores flight details.)
- `NotificationManager`: Sends alert notifications (via SMS or email).



