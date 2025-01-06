# API Casa dos Dados

Este é um projeto de **API** criado com o **FastAPI**, **Cloudscraper**, **BeautifulSoup4** e **Uvicorn**. A API permite coletar e processar dados de páginas da web de forma eficiente e rápida.

## 📋 Descrição

A API foi desenvolvida para fazer scraping de dados da **Casa dos Dados**, fornecendo informações relevantes extraídas de sites de forma automatizada e estruturada. Utiliza tecnologias modernas e eficientes como FastAPI para criação de endpoints, Cloudscraper para contornar proteções de scraping, e BeautifulSoup4 para extrair dados das páginas HTML.

### Funcionalidades
- Realiza scraping de dados de sites da Casa dos Dados.
- Fornece endpoints para acessar dados de maneira estruturada.
- Utiliza Cloudscraper para evitar bloqueios de scraping.
- Implementação de scraping eficiente com BeautifulSoup4.
- API rápida e escalável com FastAPI e Uvicorn.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework para criação da API.
- **Cloudscraper**: Biblioteca para contornar proteções contra scraping.
- **BeautifulSoup4**: Biblioteca para parsing de HTML e extração de dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

## 🛠️ Instalação

Para rodar o projeto, siga os seguintes passos:

1. Clone o repositório:
   ```bash
   git clone https://github.com/miguelbcav/api_casa_dos_dados.git
Navegue até o diretório do projeto:

bash
Copiar código
cd api_casa_dos_dados
Crie um ambiente virtual (opcional, mas recomendado):

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
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute a API com Uvicorn:

bash
Copiar código
uvicorn main:app --reload
Isso iniciará a API em modo de desenvolvimento. O servidor estará disponível em http://127.0.0.1:8000.

🚀 Como Usar
Após a API estar rodando, você pode acessar os endpoints no navegador ou utilizando ferramentas como o Postman.

Por exemplo, para acessar um endpoint de scraping, faça uma requisição GET para:

arduino
Copiar código
http://127.0.0.1:8000/dados
📚 Mais Informações
Para mais detalhes sobre o funcionamento da API, consulte a documentação interativa gerada automaticamente pelo FastAPI em:

arduino
Copiar código
http://127.0.0.1:8000/docs
💬 Como Contribuir
Faça um fork do repositório.
Crie uma nova branch (git checkout -b minha-contribuicao).
Faça suas modificações e commit.
Push para a branch (git push origin minha-contribuicao).
Abra uma pull request.
