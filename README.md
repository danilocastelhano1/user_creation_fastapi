# Cadastro de Usuários - SHIPAY

## Considreações
Respondendo ao item 5 do teste

## Tecnologias usuadas:
- FastAPI
- Docker Compose (não foi solicitado, mas considero como um plus)


## Passos
- Rodar o comando: ```docker-compose up --build```, uma vez que o docker está rodando você
conseguirar testar a aplicação


### cUrl's:
cUrl enviando SEM senha (deve-se gerar uma senha random)
```curl
curl --location 'http://127.0.0.1:8000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Maria da Silva Sauro",
    "email":"mariazinha_2023@outlook.com",
    "role": "gerente"
}'
```
cUrl enviando COM senha (deve-se gerar uma senha random)
```curl
curl --location 'http://127.0.0.1:8000/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Maria da Silva Sauro",
    "email":"mariazinha_2023@outlook.com",
    "password":"teste@123",
    "role": "gerente"
}'
```

## Criado 2 testes sobre a API (não foi solicitado, mas considero como um plus)
Rodar dentro do docker:
```docker-compose run web bash```
então:
```pytest```
