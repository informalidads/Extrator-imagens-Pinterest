import requests
from bs4 import BeautifulSoup
import os
import urllib

urls = [
    'https://br.pinterest.com/pin/666321707391390090/',
    ]
num_paginas = 5

folder_name = 'Nome-da-pasta-para-salvar'
os.makedirs(folder_name, exist_ok=True)

for url in urls:
    for pagina in range(1, num_paginas + 1):
        url_pagina = f'{url}?page={pagina}'
        response = requests.get(url_pagina)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            
            for img in img_tags:
                img_url = img.get('src')
                if img_url:
                    img_name = os.path.join(folder_name, os.path.basename(img_url))
                    urllib.request.urlretrieve(img_url, img_name)
                    print(f"Imagem salva: {img_name}")
        else:
            print(f"Falha ao acessar a página {pagina} do Pinterest.")
