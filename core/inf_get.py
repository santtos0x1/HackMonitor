from bs4 import BeautifulSoup
import requests
from typing import List, Tuple
import logging

def getNews() -> Tuple[List[str], List[str], List[str], List[str]]:
    url: str = "https://news.ycombinator.com/news"

    
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    titleline: List[BeautifulSoup] = soup.find_all('span', class_='titleline')
    subline: List[BeautifulSoup] = soup.find_all('span', class_='score')
    age: List[BeautifulSoup] = soup.find_all('span', class_='age')

    try:
        links: List[str] = [i.a['href'] for i in titleline]
        titles: List[str] = [i.a.get_text() for i in titleline]
        time: List[str] = [i.get_text() for i in age]
        score: List[str] = [i.get_text() for i in subline]
        
    except AttributeError:
        logging.error("Error parsing the HTML structure. Please check the email's layout.")
    
    logging.info(f"Successfully retrieved {len(titles)} articles from Hacker News.")
    return titles, links, time, score
