import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Exemple pour récupérer les paragraphes (à adapter selon la structure de la page)
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.get_text() for para in paragraphs])

    return article_text
