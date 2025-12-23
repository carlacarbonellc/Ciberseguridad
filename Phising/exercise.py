# exercises.py

from bs4 import BeautifulSoup

html = "<html><body><a href='test'>Link</a></body></html>"
soup = BeautifulSoup(html, "html.parser")

print("Número de enlaces:", len(soup.find_all("a")))
