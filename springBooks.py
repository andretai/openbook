import requests
import csv
from bs4 import BeautifulSoup
from csv import writer

file_name = 'statistics.csv'

with open(file_name, 'w', encoding="utf-8") as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Id', 'Title', 'Author(s)', 'Url']
  csv_writer.writerow(headers)

def extract (books):
  global id
  global count
  for book in books:
    id += 1
    count += 1
    if count > len(books):
      break
    title = book.find('a', {'class':'title'}).get_text()
    link = 'https://link.springer.com' + book.find('a', {'class':'title'})['href']
    if book.find('span', {'class':'authors'}):
      authors_a = book.find('span', {'class':'authors'}).select('a')
    elif book.find('span', {'class':'enumeration'}):
      authors_a = book.find('span', {'class':'enumeration'}).select('a')
    else:
      authors_a = '-'
    arr = []
    for author in authors_a:
      arr.append(author.get_text())
    row = [id, title, ', '.join(arr), link]
    with open(file_name, 'a', encoding="utf-8") as csv_file:
      csv_writer = writer(csv_file)
      csv_writer.writerow(row)
    print(len(books))
    print(id, count)

def get (url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  books = soup.find_all(class_='has-cover')
  return books

id = 0
count = 0
discipline = 'Statistics'
pages = 1

for page in range(1, (pages+1)):
  extract(get('https://link.springer.com/search/page/'
          +str(page)+'?facet-discipline=%22'
          +discipline+'%22&facet-content-type=%22Book%22&showAll=false'))
  count = 0