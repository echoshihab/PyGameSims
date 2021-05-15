from bs4 import BeautifulSoup
import requests
import smtplib



headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

#email configs
sender_email = "sender_email@email.com"
to_email = "to_email@email.com"
sender_email_password = "sender_password"

#replace product url to deired product
product_url = "https://www.amazon.ca/Dual-Monitor-Mount-Stand-Adjustable/dp/B0834JH3P1/\
ref=sr_1_12?dchild=1&keywords=clamp+monitor&qid=1619876478&sr=8-12"

#replace price to desired price
desired_price = 100

amazon_response = requests.get(url=product_url, headers=headers)

soup = BeautifulSoup(amazon_response.text, "html.parser")

price = soup.select_one("#priceblock_ourprice").getText().split('$')[1]

if float(price) < desired_price:
    contents = f"Price alert: {price} , buy now! at {product_url}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_email_password)
        connection.sendmail(from_addr=sender_email, to_addrs=f"{to_email}", msg=f"Subject:Price Alert!\n\n{contents}")






