# API Casa dos Dados

Este projeto implementa uma **API** para coletar informações detalhadas sobre CNPJs, utilizando **FastAPI**, **Cloudscraper**, **BeautifulSoup4** e **Uvicorn**. Ele permite realizar scraping de dados da Casa dos Dados e retornar informações como **Nome Fantasia**, **Razão Social**, **Sócios**, **Telefone** e **WhatsApp**, além de outras informações detalhadas sobre o CNPJ.

## 📋 Descrição

A API consiste em dois principais endpoints:

1. **/api/payload**: Recebe um payload contendo parâmetros de pesquisa e retorna uma lista de CNPJs encontrados, de acordo com os critérios fornecidos.
2. **/api/cnpjs**: Recebe uma lista de CNPJs e retorna as informações detalhadas para cada um, incluindo dados como nome, telefone, sócios, e outros detalhes importantes.

O sistema faz uso de técnicas de scraping para extrair os dados diretamente do site da Casa dos Dados, utilizando **Cloudscraper** para evitar bloqueios de scraping e **BeautifulSoup4** para a extração dos dados.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework rápido e moderno para construção de APIs.
- **Cloudscraper**: Biblioteca para contornar bloqueios e fazer requisições HTTP de forma eficiente.
- **BeautifulSoup4**: Biblioteca para parsing de HTML e extração de dados.
- **Uvicorn**: Servidor ASGI de alta performance para rodar a aplicação FastAPI.
- **Regex**: Usado para extrair dados específicos, como sócios, dos textos HTML.

## 🛠️ Instalação

### Passo 1: Clone o repositório
Clone o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/miguelbcav/api_casa_dos_dados.git
Passo 2: Acesse o diretório do projeto
Navegue até o diretório do projeto:

bash
Copiar código
cd api_casa_dos_dados
Passo 3: Crie e ative um ambiente virtual (opcional, mas recomendado)
Crie um ambiente virtual para isolar as dependências:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar código
.\venv\Scripts\activate
No Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Passo 4: Instale as dependências
Instale as bibliotecas necessárias para o projeto:

bash
Copiar código
pip install -r requirements.txt
Passo 5: Execute a API
Execute a API com o servidor Uvicorn:

bash
Copiar código
uvicorn main:app --reload
A API estará disponível no endereço http://127.0.0.1:8000.

🔧 Como Usar
Endpoint 1: /api/payload
Este endpoint recebe um payload contendo parâmetros de pesquisa e retorna uma lista de CNPJs encontrados.

Exemplo de Requisição (POST):
json
Copiar código
{
    "criterio1": "valor1",
    "criterio2": "valor2"
}
Resposta:
json
Copiar código
{
    "success": true,
    "cnpjs": ["12345678000195", "98765432000123", ...]
}
Endpoint 2: /api/cnpjs
Este endpoint recebe uma lista de CNPJs e retorna informações detalhadas sobre cada um, como telefone, sócios, email, entre outros.

Exemplo de Requisição (POST):
json
Copiar código
{
    "cnpjs": ["12345678000195", "98765432000123"]
}
Resposta:
json
Copiar código
{
    "success": true,
    "data": [
        {
            "CNPJ": "12345678000195",
            "Nome Fantasia": "Exemplo LTDA",
            "Razão Social": "Exemplo Ltda",
            "Situação Cadastral": "Ativa",
            "Data de Abertura": "01/01/2000",
            "Telefone_1": "(11) 1234-5678",
            "Telefone_2": "(11) 8765-4321",
            "Email": "contato@exemplo.com.br",
            "WhatsApp Link 1": "https://api.whatsapp.com/send?phone=551112345678",
            "Sócios": "João da Silva (Sócio-Administrador), Maria de Souza (Sócia)"
        },
        ...
    ]
}
💡 Como Funciona
Requisição e Coleta de Dados: O sistema faz uma requisição à API da Casa dos Dados, coletando os CNPJs encontrados conforme os parâmetros fornecidos.
Processamento em paralelo: Para garantir desempenho, o processamento dos dados de cada CNPJ é feito em paralelo, utilizando múltiplas threads para acelerar a coleta das informações.
Extração de Dados: Para cada CNPJ, o sistema faz scraping do site da Casa dos Dados, extraindo informações como telefone, sócios e emails.
⚙️ Como Contribuir
Faça um fork do repositório.
Crie uma nova branch (git checkout -b minha-contribuicao).
Faça suas modificações e commit.
Push para a branch (git push origin minha-contribuicao).
Abra uma pull request.
📚 Documentação da API
A documentação interativa da API gerada pelo FastAPI pode ser acessada no seguinte link:

arduino
Copiar código
http://127.0.0.1:8000/docs
