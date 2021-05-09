from bs4 import BeautifulSoup

with open('index.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_a_tags = soup.find_all(name="a")

# get tag text
print("--Get anchor tag text from html content--")
for a_tag in all_a_tags:
    print(a_tag.getText() + '\n')

print("--Get anchor tag links from html content--")
for a_tag in all_a_tags:
    print(a_tag.get("href") + '\n')


#get item content by id
print("--Get tag by id--")
h1_name = soup.find(name="h1", id="name")
print(h1_name.getText() + '\n')

#get items by class
print("--Get tags by class--")
skill_rows = soup.findAll(name="div", class_="skill-row")
for row in skill_rows:
    print(row.find('p').getText() + '\n')

#get item by css selector
print("--Get specfic items by css selector--")
profile_pic_info = soup.select_one(selector=".middle-container .profile .profile-img")
print(profile_pic_info.get('src'))
