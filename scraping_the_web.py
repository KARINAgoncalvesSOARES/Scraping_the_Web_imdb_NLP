"""
Data Scientist Jr.: Karina Gonçalves Soares

Objetivo: Nest script fazemos uma raspagem de informações 
          num site da internet (imdb.com). Depois de coletar as 
          informações salvamos os Dados num arquivo CSV 🤗.

OBS: As vezes o site demora ou dá erro no retorno.
     Tente várias vezes a execução do script.          
"""
import requests # Faz solicitações HTTP
from bs4 import BeautifulSoup # Extrai informações específicadas do conteúdo HTML de uma página web.
import pandas as pd

# Definir o cabeçalho de usuário
# "User-Agent". Esse cabeçalho é comumente usado em solicitações HTTP para identificar o cliente que está fazendo a solicitação.
# Ao especificar um user-agent, você pode simular um navegador ou dispositivo específico e receber a resposta apropriada do servidor.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Recupere o conteúdo HTML do site
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250' # página que desejo acessar

#Nesta linha, é feita uma solicitação GET para a URL especificada. A função requests.get() é usada para enviar a solicitação HTTP e obter a resposta do servidor.
response = requests.get(url, headers=headers) 
print(response)

# Analisar o conteúdo HTML retornado pela solicitação HTTP.
soup = BeautifulSoup(response.text, 'html.parser')

# Encontre todos os elementos do filme
movies = soup.find_all('td', class_='titleColumn')


# Extraia as informações desejadas
# criando uma lista de dicionários, onde cada dicionário representa um filme e contém as informações de título e ano.
data = []
for movie in movies:
    title = movie.find('a').text
    year = movie.find('span', class_='secondaryInfo').text
    data.append({'title': title, 'year': year})


# Criamos um DataFrame e salvamos em um CSV
df = pd.DataFrame(data)
print(df.head())
df.to_csv('imdb_top_movies.csv', index=False) 
# A linha df.to_csv('imdb_top_movies.csv', index=False) salva o DataFrame em um arquivo CSV chamado "imdb_top_movies.csv". 
# O parâmetro index=False é usado para evitar que o índice do DataFrame seja salvo como uma coluna no arquivo CSV.
