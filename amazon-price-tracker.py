from bs4 import BeautifulSoup
import requests
import smtplib

MY_MAIL = ### Enter mail address on which you will receive price notifications from this script.
URL = ### Set Amazon item URL here.

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

response = requests.get(URL, headers=HEADERS)
item_site = response.text

soup = BeautifulSoup(item_site, "html.parser")
price = float(soup.find(name="span", id="price_inside_buybox").getText().split("\n")[1].split("£")[1])
product_title = soup.find(name="span", id="productTitle").getText().strip()

TARGET_PRICE = ### Set your target price here.
EMAIL = ### Set email from which the price notification will be sent.
PASSWORD = ### Set the password of above email.

if price < TARGET_PRICE:
    message = f"{product_title} --> price is now under your targert {TARGET_PRICE}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs= MY_MAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}"
        )