from requests import get
from bs4 import BeautifulSoup

# Profil des Docteurs de Doctolib

# Extraction du code source de la page
url = "https://www.dabadoc.com" # URL général
soup = BeautifulSoup(get(url).text,"html.parser") # extraction du code html


# dans un premier temps, e

# Extraction des spécialités définies dans le site
def specialities(url):
    html_spec = BeautifulSoup(get(url).text,"html parser")
    specs = html_spec.findAll()
    specs = specs.get_text(strip=True)
    return specs
specialites = specialities(url)
# Extraction des villes définies dans le site par spécialité
def ville(spec):
    html_ville = BeautifulSoup(get(url+spec).text,"html.parser")
    villes = html_ville.findAll()
    villes = villes.get_text(strip=True)

villes_by_spec = []
for spec in specialites:
    pass

# Récupérer tous les médécins selon la spécialité et la ville
medecins = {}        
def all_medecins(spec, ville):
    html_medecin = BeautifulSoup(get(f"https://www.dabadoc.com/ma/{spec}/{ville}").text, "html.parser")
    doctas = html_medecin.findAll("a", attrs={"target" : "_self", "class" : "profile_url"})
    for docta in doctas:
        medecins[docta.get_text(strip=True)] = docta.get("href")



# Extraire le lien du profil du medecin et visister ce lien afin de collecter les infos utiles
def profile(med):
    html_profile = BeautifulSoup(get(med).text, "html.parser")
    profile = html_profile.find()


# NOTES POUR L'EXERCICE 