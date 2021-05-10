import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(".storylink")
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_score_index= scores.index(max(scores))

article_texts=[]
article_links=[]

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

print("Article with highest point")
print(article_texts[highest_score_index])
print(article_links[highest_score_index])

#
