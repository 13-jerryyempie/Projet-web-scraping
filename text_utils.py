import re

def clean_text(text):
    # Supprimer les espaces multiples et nettoyer le texte
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

# Test du nettoyage lorsque le fichier est exécuté directement
if __name__ == "__main__":
    sample_text = "   Ceci est   un test.    Avec   plusieurs   espaces!   "
    print("Texte original:", sample_text)
    cleaned_text = clean_text(sample_text)
    print("Texte nettoyé:", cleaned_text)
