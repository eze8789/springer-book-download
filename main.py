"""The objective is to get the ebooks published by springer. """

import requests
import bs4
import os

# List of computer science urls books
urls = [
    'https://link.springer.com/openurl?genre=book&isbn=978-3-662-44874-8'
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-13072-9',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-47831-9',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4612-1844-9',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-84800-070-4',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4471-7307-6',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-642-33143-5',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-12742-2',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4471-5134-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-84882-935-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-14142-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-540-77974-2',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-21936-3',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-57883-5',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-55444-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-63913-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-44561-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-84800-322-4',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-642-04101-3',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-57750-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-05290-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-14240-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-29659-3',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4471-6642-9',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-24280-4',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-50017-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4471-5601-7',
    'https://link.springer.com/openurl?genre=book&isbn=978-1-4471-6684-9',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-55606-2',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-70790-7',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-64410-3',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-72547-5',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-58487-4',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-73004-2',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-75771-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-662-56509-4',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-73132-2',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-89491-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-63588-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-75502-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-94463-0',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-72347-1',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-92429-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-98833-7',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-91155-7',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-030-00581-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-319-99420-8',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-030-20290-3',
    'https://link.springer.com/openurl?genre=book&isbn=978-3-030-25943-3'
]

base_url = 'https://link.springer.com'

os.makedirs('./books/', exist_ok=True) # Create dir to store the books

def get_url(url):
    r = requests.get(url)
    r.raise_for_status()
    return r

def download_ebook(content):
    web_soup = bs4.BeautifulSoup(r.content)
    title = web_soup.title.string.split(' |')[0]
    if '/' in title:
        title = title.replace('/', "")
        print(title)
    ebook_section = web_soup.find('div', attrs={'class': 'cta-button-container__item'})
    ebook_url = f"{base_url}{ebook_section.find('a', href=True).get('href')}"
    book = requests.get(ebook_url)
    return book.content, title

def save_ebook(book, title):
    filename = f"{title}.pdf"
    with open(os.path.join('./books', filename), 'wb') as ebook:
        ebook.write(book)

for url in urls:
    r = get_url(url)
    get_book = download_ebook(r.content)
    book = get_book[0]
    title = get_book[1]
    print(f"Saving the ebook {title}")
    save_ebook(book, title)
    
print('Done')
