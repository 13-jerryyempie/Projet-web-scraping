import requests
from bs4 import BeautifulSoup
from text_utils import clean_text 

def scrape_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Sélecteurs CSS pour extraire le texte de l'article
    article_sections = soup.select("section.teaser.teaser--inline-picture, .thread section.teaser.teaser--inline-picture")
    
    if not article_sections:
        return None
    
    # Extraire et concaténer le texte
    article_text = " ".join(section.get_text(separator=" ", strip=True) for section in article_sections)
    
    # Nettoyage du texte avant de le retourner
    return clean_text(article_text) if article_text else None

# Test du scraping et du nettoyage
if __name__ == "__main__":
    url = "https://www.lemonde.fr/gouvernement-bayrou/"  
    article_text = scrape_article(url)

    if article_text:
        print("Article extrait et nettoyé :\n", article_text)
    else:
        print("Impossible d'extraire le contenu de l'article.")
