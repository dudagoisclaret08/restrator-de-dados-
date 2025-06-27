import bs4

with open('index.html', encoding='UTF-8') as examploFile:
    examploSoup = bs4.BeautifulSoup(examploFile.read(), 'html.parser')

elems = examploSoup.select('#author')

if elems:
    print("Texto encontrado:", elems[0].get_text())
else:
    print("Elemento com id = 'author' não encontrado")