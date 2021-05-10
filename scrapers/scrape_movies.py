from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://www.empireonline.com/movies/features/best-movies-2/")
r.html.render()
results = r.html.find(selector="h3")

with open("movies.txt", mode='w') as file:
    for i in range(len(results) - 1, 0, -1):
        movie = f'1) {results[i].text}' \
            if i == len(results) - 1 else results[i].text
        file.write(f'{movie}\n')
