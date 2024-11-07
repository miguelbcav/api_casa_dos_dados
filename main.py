from fastapi import FastAPI, HTTPException
from cloudscraper import create_scraper
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

app = FastAPI()

# Função para fazer a requisição e coletar os CNPJs de cada página
def fetch_data(payload, max_pages=10):
    scraper = create_scraper()
    base_url = "https://api.casadosdados.com.br/v2/public/cnpj/search"
    collected_cnpjs = []

    for page in range(1, max_pages + 1):
        payload['page'] = page
        response = scraper.post(base_url, json=payload)
        
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Erro ao acessar a API externa.")
        
        data = response.json()
        if not data.get("success"):
            break  # Encerra se não houver mais dados

        # Coleta apenas os CNPJs da página atual
        cnpjs = [item["cnpj"] for item in data["data"]["cnpj"]]
        collected_cnpjs.extend(cnpjs)

        # Se o número de CNPJs for menor que o limite por página, encerra
        if len(cnpjs) < 20:
            break

    return collected_cnpjs
scraper = create_scraper()
# Função para processar um único CNPJ
def process_cnpj(cnpj):
    url = f"https://casadosdados.com.br/solucao/cnpj/{cnpj}"
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extração de números de telefone
        telefones = [tel.text for tel in soup.find_all('a', href=lambda href: href and "tel:" in href)]
        telefone_1 = telefones[0] if len(telefones) > 0 else "N/A"
        telefone_2 = telefones[1] if len(telefones) > 1 else "N/A"

        # Extração de sócios
        socios_pattern = r'([A-Z\s]+)\s-\s(Sócio(?:-Administrador)?)\s-\s(\d{2}/\d{2}/\d{4})'
        socios_matches = re.findall(socios_pattern, response.text)
        socios_list = [f"{socio[0].strip()} ({socio[1].strip()})" for socio in socios_matches] if socios_matches else ["N/A"]
        lista_socios = ', '.join(socios_list)

        cnpj_data = {
            "CNPJ": cnpj,
            "Nome Fantasia": soup.find('label', text='Nome Fantasia:').find_next('p').text if soup.find('label', text='Nome Fantasia:') else "N/A",
            "Razão Social": soup.find('label', text='Razão Social:').find_next('p').text if soup.find('label', text='Razão Social:') else "N/A",
            "Situação Cadastral": soup.find('label', text='Situação Cadastral:').find_next('p').text if soup.find('label', text='Situação Cadastral:') else "N/A",
            "Data de Abertura": soup.find('label', text='Data de Abertura:').find_next('a').text if soup.find('label', text='Data de Abertura:') else "N/A",
            "UF": soup.find('label', text='Estado:').find_next('p').text if soup.find('label', text='Estado:') else "N/A",
            "Município": soup.find('label', text='Municipio:').find_next('p').text if soup.find('label', text='Municipio:') else "N/A",
            "Bairro": soup.find('label', text='Bairro:').find_next('p').text if soup.find('label', text='Bairro:') else "N/A",
            "CEP": soup.find('label', text='CEP:').find_next('p').text if soup.find('label', text='CEP:') else "N/A",
            "Telefone_1": telefone_1,
            "Telefone_2": telefone_2,
            "Email": soup.find('a', href=lambda href: href and "mailto" in href).text if soup.find('a', href=lambda href: href and "mailto" in href) else "N/A",
            "WhatsApp Link 1": soup.find('a', href=lambda href: href and "api.whatsapp.com" in href)['href'] if soup.find('a', href=lambda href: href and "api.whatsapp.com" in href) else "N/A",
            "WhatsApp Link 2": "N/A",  # Adicionar lógica para segundo WhatsApp se necessário
            "CNAE Principal": soup.find('label', text='CNAE Principal:').find_next('p').text if soup.find('label', text='CNAE Principal:') else "N/A",
            "Sócios": lista_socios
        }

        return cnpj_data
    else:
        print(f'Erro ao consultar CNPJ: {cnpj}')
        return None

# Endpoint para processar o payload e retornar apenas os CNPJs
@app.post("/api/payload")
async def get_cnpjs(payload: dict):
    try:
        result = fetch_data(payload)
        return {"success": True, "cnpjs": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para processar lista de CNPJs e retornar as informações detalhadas
@app.post("/api/cnpjs")
async def get_cnpj_data(cnpjs: dict):
    try:
        cnpj_list = cnpjs.get("cnpjs", [])
        if not cnpj_list:
            raise HTTPException(status_code=400, detail="Nenhum CNPJ fornecido")

        # Define o número de threads
        max_threads = 10  # Ajuste esse número conforme necessário

        # Executa a função process_cnpj em paralelo
        result = []
        with ThreadPoolExecutor(max_threads) as executor:
            future_to_cnpj = {executor.submit(process_cnpj, cnpj): cnpj for cnpj in cnpj_list}
            for future in as_completed(future_to_cnpj):
                cnpj_data = future.result()
                if cnpj_data:
                    result.append(cnpj_data)

        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
