from bs4 import BeautifulSoup
import requests 
import pandas as pd 


books = []
for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    page = requests.get(url)
    print('pages:', page)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    #print(lists)
    for list in lists:
        title = list.find('h3').text
        price =float(list.find('p', class_="price_color").text[1:])
        star = list.find('p')['class'][1]
        books.append([title, price, star])
    


    df = pd.DataFrame(books, columns=['Title', 'Price', 'Rating'])
    df.to_csv('books.csv')

