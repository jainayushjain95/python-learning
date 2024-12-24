import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(result.text, "lxml")

soup_select_items_computer = soup.select(".mw-file-element")[1]
# print(soup_select_items_computer['src'])

image_link = 'https:' + soup_select_items_computer['src']
image = requests.get(image_link)

f = open('computer.jpg', 'wb')
f.write(image.content)


# print(len(soup.select(".vector-toc-list-item")))
# print(soup.select("title")[0].getText())