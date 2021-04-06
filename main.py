import requests

# Bloco de endpoints e token
token = '3bdfe52c5b254680abe6c4a9c93ec3df'
url = f'https://api.vagalume.com.br/search.php?apikey={token}'
url_artista = f'https://www.vagalume.com.br/'
url_rank_art = f'https://api.vagalume.com.br/rankArtist.php?apikey={token}'
url_rank_geral = f'https://api.vagalume.com.br/rank.php?'

'''
procurar artista  
- posicão
- qtdd de views 
- genero 
- artista relacionado 
- musica maisvista 
- detalhes do artista)
'''
artista = str(input('Digite o nome do artista: ')).lower()
url_artista_final = f'{url_artista}{artista}/index.js?{token}'  # em nomes conjuntos tem que ter um traço
# Bloco informações do artista + rank artistas
response = requests.get(url=url_artista_final)
artistas_info = response.json()
#print(artistas_info)
artista_id = artistas_info['artist']['id']
response_rank = requests.get(url=url_rank_art, params={'period': 'monthly', 'artID': artista_id})
result_rank = response_rank.json()
#print(result_rank['artist']['month'][2]["period"])
#Usuário escolhe o mês da posição do artista que quer ver

#Receber a data. Ex: 202009
data = int(input('Digite o ano e o mês no formato AAAAMM: '))

#Percorrer a lista de períodos
#Acessar cada elemento
#Ver qual elemento bate com a data do usuário
#Imprimir a posição daquela data
#ata = 202007
#lista = [202006,202007...]
for i in range(len(result_rank['artist']['month'])): #[0,1,2..10] 
  print(result_rank["artist"]["month"][i]["period"])
  if result_rank["artist"]["month"][i]["period"] == data: 
    pass
  else: pass
    
''''
result_rank=
{"artist":
  "month":
      [{"period:" 202006, "pos":100, "rank":5},
      {"period:" 202007, "pos":101, "rank":5},
      {"period:" 202008, "pos":102, "rank":5},
      {"period:" 20209, "pos":103, "rank":5},
      {"period:" 20210, "pos":104, "rank":5},]}
'''

'''
lista = [1,2,3]
for i in len(lista): #[0,1,2]
  lista[i]
'''
#print(result_rank['artist']['month'])


#print(len(result_rank['artist']['month']))

'''
