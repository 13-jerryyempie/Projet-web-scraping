import chromadb
from sentence_transformers import SentenceTransformer
import os
from crawler import scrape_article  # Assure-toi que crawler.py est correctement configuré

# 🗂️ Initialisation de ChromaDB (stockage persistant)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# 📌 Création ou récupération de la collection
collection = chroma_client.get_or_create_collection(name="articles")

# 🔹 Chargement du modèle d'embeddings avec sentence-transformers
model = SentenceTransformer("all-MiniLM-L6-v2")  # Tu peux changer de modèle si besoin

def embed_text(text):
    """
    Génère un embedding pour le texte à l'aide de sentence-transformers.
    Affiche un extrait du vecteur généré pour vérification.
    """
    embedding = model.encode(text).tolist()  # Conversion en liste pour compatibilité avec ChromaDB
    # Affiche les 10 premières valeurs du vecteur pour vérifier (tu peux afficher plus si nécessaire)
    print("Embedding généré (extrait) :", embedding[:10])
    return embedding

def add_article(url):
    """
    Récupère l'article via le scraper, génère son embedding et l’ajoute à ChromaDB.
    Affiche également le vecteur complet pour vérification.
    """
    text = scrape_article(url)  # Scraping en direct depuis l'URL
    if not text:
        print(f"❌ Impossible de récupérer l'article {url}")
        return
    
    embedding = embed_text(text)
    # Pour voir le vecteur complet, décommente la ligne suivante (attention, cela peut être long)
    print("Vecteur complet :", embedding)
    
    collection.add(
        ids=[url],                # Utilisation de l'URL comme identifiant unique
        embeddings=[embedding],   # Embedding généré pour l'article
        metadatas=[{"url": url, "content": text}]  # Stockage des métadonnées
    )
    print(f"✅ Article {url} ajouté avec succès !")

def search_similar(query, n_results=5):
    """
    Recherche les articles les plus proches du texte de la requête.
    Affiche l'embedding de la requête pour vérification.
    """
    query_embedding = embed_text(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    
    if results["ids"]:
        return [(res, metadata["url"]) for res, metadata in zip(results["ids"][0], results["metadatas"][0])]
    else:
        return "❌ Aucun article pertinent trouvé."

# 🛠️ TEST : Ajout d'un article réel via le scraper et recherche similaire
if __name__ == "__main__":
    # Remplace par une URL d'article réel que tu souhaites indexer
    url = "https://www.lemonde.fr/gouvernement-bayrou/"
    add_article(url)  # Scraping + Indexation
    
    # Effectuer une recherche avec une requête
    query = "le gouvernement"
    results = search_similar(query)
    print("📌 Résultats de recherche :", results)
