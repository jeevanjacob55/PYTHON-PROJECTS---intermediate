import requests, smtplib
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
amazon_url = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/'
amazon_header = {
    'Accept-Language':'en-US,en;q=0.9,id;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}


user_mail = os.getenv(USER_EMAIL)
user_password = os.getenv(PASS)

amazon_page = requests.get(url = amazon_url, headers=amazon_header).text


amazon_soup = BeautifulSoup(amazon_page, 'html.parser')


amazon_prices = amazon_soup.find_all(name="p", class_="twisterSwatchPrice")
prices = [float(amazon_price.get_text().strip().split('$')[1]) for amazon_price in amazon_prices]


if len(prices)>0 and min(prices)<100:
    message = '\n'.join([
        'Subject: Instant Pot News Alert!\n', 
        f'Price of the instant pot you wanted have dropped to ${min(prices)}!\n',
        'Tap on the link below!', 
        amazon_url
    ])
  
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user = user_mail, password = user_password)
        connection.sendmail(from_addr = user_mail, to_addrs = user_mail, msg = message)
    print(message)