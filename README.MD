# SpaceX Launches Viewer

Este projeto é uma aplicação web desenvolvida com Django que exibe informações sobre lançamentos da SpaceX, como lançamentos bem-sucedidos, falhados e futuros. A aplicação consome a API pública da SpaceX e exibe os dados de uma forma organizada.

## Funcionalidades

- Exibe **lançamentos bem-sucedidos** da SpaceX.
- Exibe **lançamentos falhados** da SpaceX.
- Exibe **lançamentos futuros** da SpaceX.
- Interface interativa para navegar entre as diferentes seções de lançamentos.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para desenvolver a aplicação.
- **Requests**: Biblioteca para fazer requisições HTTP à API da SpaceX.
- **HTML/CSS**: Usado para estruturar e estilizar a interface do usuário.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- **Python 3.8+**
- **Django 5.1.3**
- **Requests**

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/spaceX-launches-viewer.git
   cd spaceX-launches-viewer

2. Crie um ambiente virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt

4. Execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver

5. Acesse a aplicação no seu navegador:

    ```arduino
    http://127.0.0.1:8000