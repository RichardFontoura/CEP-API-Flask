<h1 align="center"> CEP - API </h1>

# Índice 

- [Introdução](#Introdução)
- [Tecnologias Utilizadas](#Tecnologias-Utilizadas)
- [Descrição do Projeto](#Descrição-do-Projeto)
- [Endpoints](#Endpoints)
- [Link](#Link)

# Introdução
Este projeto foi desenvolvido em Python e tem como objetivo consumir dados de CEP de APIs externas, armazená-los em um banco de dados local e retornar os dados armazenados em formato JSON para o usuário.

#Tecnologias-Utilizadas
- Flask: Framework web utilizado para criar a API.
- Flask-RESTful: Extensão do Flask para simplificar a criação de APIs RESTful.
- Flask-SQLAlchemy: Extensão do Flask para integração com SQLAlchemy.
- python-dotenv: Carrega variáveis de ambiente de um arquivo .env.
- Requests: Biblioteca HTTP para realizar as requisições às APIs externas.
- Flasgger: Extensão do Flask para gerar documentação Swagger.

#Descrição-do-Projeto
- Consulta de CEP: Consome dados de CEP de APIs externas (BrasilAPI e ViaCEP).
- Armazenamento Local: Insere os dados de CEP no banco de dados local SQLite utilizando SQLAlchemy.
- API RESTful: Fornece uma API RESTful para retornar os dados de CEP armazenados em formato JSON.
- Documentação Swagger: Utiliza Flasgger para documentação automática da API.

#Endpoints
- GET /cep/{cep}: Retorna os dados do CEP especificado. Se o CEP não estiver no banco de dados, será consultado nas APIs externas e inserido no banco de dados local.
- PUT /cep/{cep}/auto_repair: Atualiza os dados do CEP especificado consultando novamente nas APIs externas.

- A documentação Swagger pode ser acessada em http://localhost:5000/apidocs.

#Link
A API pode ser utilizada publicamente pela URL https://apidecepbr.squareweb.app, fiquem a vontade utilizar :)
