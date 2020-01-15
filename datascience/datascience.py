import pandas as pd
import io
import requests

url = "https://raw.githubusercontent.com/alura-cursos/formacao-data-science/master/movies.csv"
filmes = pd.read_csv(url)
filmes.columns = ["ID", "Titulo", "Genero"]
filmes.head()