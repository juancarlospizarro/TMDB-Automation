import requests
from bs4 import BeautifulSoup


url = "https://www.themoviedb.org/movie?language=es"

response = requests.get(url)

raw_code = response.text

soup = BeautifulSoup(raw_code, "html.parser")

#print(soup.prettify())


peliculas = soup.find(id="page_1")
#print(peliculas)

pelicula = peliculas.select("h2 a")

títulos = list()
for a in pelicula:
    títulos.append(a.string)

#print(títulos)

enlaces = list()
for a in pelicula:
    enlaces.append("https://www.themoviedb.org" + a["href"])

#print(enlaces)

imagenes = peliculas.select("img")

posters = list()

for img in imagenes:
    posters.append(img["src"])

#print(posters)

fecha = peliculas.select(".content p")
fechas = list()
for i in range(len(fecha)-1):
    fechas.append(fecha[i].string)
#print(fechas)

rating = peliculas.select("div[class*='user_score_chart']")
ratings = list()
for r in rating:
    ratings.append(r["data-percent"])
#print(ratings)