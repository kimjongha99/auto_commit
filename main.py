# main.py
import os
from datetime import datetime
from crawler import NewsCrawler


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    # 현재 날짜로 디렉토리와 파일명 생성
    date = datetime.today()
    month_dir = date.strftime('%Y-%m')
    filename = date.strftime('%Y-%m-%d')

    # 월별 디렉토리 생성
    create_directory(month_dir)

    # 뉴스 크롤링 및 저장
    crawler = NewsCrawler()
    crawler.crawl()
    crawler.save_to_file(f"{month_dir}/{filename}.txt")


if __name__ == "__main__":
    main()
