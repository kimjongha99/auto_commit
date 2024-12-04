# crawler.py
import requests
from bs4 import BeautifulSoup as bs4

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


class NewsCrawler:
    def __init__(self, url='https://www.infoq.com/development/news/'):
        self.url = url
        self.title = []
        self.href = []
        self.desc = []

    def crawl(self):
        res = requests.get(self.url, headers=header)
        soup = bs4(res.text, 'html.parser')

        titles = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__title > a')
        descriptions = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__excerpt')

        self.title = [t.text.strip() for t in titles]
        self.href = [h.attrs['href'] for h in titles]
        self.desc = [d.text.strip() for d in descriptions]

    def save_to_file(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for i in range(len(self.title)):
                content = (
                    f"{i + 1}번째 검색 내용\n"
                    f"제목: {self.title[i]}\n"
                    f"주소: https://www.infoq.com{self.href[i]}\n"
                    f"설명: {self.desc[i]}\n\n"
                )
                f.write(content)
