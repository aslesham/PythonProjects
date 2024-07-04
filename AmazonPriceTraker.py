import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "AMAZON LINK OF YOUR DESIRED PRODUCT"
SET_PRICE = YOUR PRICE LIMIT
my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
amazon_page = response.text
#print(amazon_page)

soup = BeautifulSoup(amazon_page, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
formatted_price = int(price.replace(",", ""))
title = soup.find(id="productTitle").get_text().strip()

message = f"{title} is now {formatted_price}!"

if formatted_price <= SET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=TO ADDRESS,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))

