# API de informações sobre funcionários com IA

## Sobre
 - Nessa API é feita a regra de negócio através da inteligência artificial do Google, com a ideia de trazer qualquer tipo de pergunta sobre todos os funcionários de uma empresa.

## Ferramentas usadas 
    
- Python
- Flask
- Google Generative AI
- PostgreSQL

## Instalaçao de dependências

- Entre na pasta raiz do projeto e execute os comandos a baixo.
    ```
    pip install Flask
    ```

    ```
    pip install flask_sqlalchemy
    ```

    ```
    pip install psycopg2-binary 
    ```
    
    ```
    !pip install -q -U google-generativeai
    ```

## Criação da tabela no Postgres com SQL

- Após a instalação do banco de dados PostgreSQL, crie a tabela employees com o comando SQL a baixo.
    ```
    CREATE TABLE employees (
    emp_no SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender CHAR(1) NOT NULL,
    contract VARCHAR(10) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
    );
    ```

## Execução da aplicação
- Entre na raiz do projeto e execute o comando a baixo.
    ```
    python main.py
    ```

## Informações extras

- [Collection Postman](./postman/API-com-IA.postman_collection.json)
- GET: http://localhost:5000/api/funcionarios (Listar funcionários)
- POST: http://localhost:5000/api/funcionarios (Pergunta sobre funcionários)
- POST: http://localhost:5000/api/criar/funcionarios (Criar Funcionário)

# Evidências

## Listar funcionários
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/7a2370bd-af45-4e68-b61a-edfa86171b7d)

## Quantos funcionarios tenho?
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/cf3f98fa-a0ff-4a29-8c25-b514eedf9adf)

## Nome do funcionario tem o segundo maior salario?
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/4c7e6b5c-a4c7-4dc0-814f-6492a9948547)

## Quantos funcionarios trabalham como PJ e ganha mais de 5500?
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/89c7af77-927a-435a-bd8a-ee6ec65ab640)

## Qual mulher ganha o maior salario, quanto é e qual o seu tipo de contratação ?
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/47d52e07-d9df-4fd8-bf5b-bafac7dc899e)

## Quanto é o meu gasto total somente com funcionarios CLT?
![image](https://github.com/andre-arao/api-funcionarios-IA/assets/99445336/d71a125d-210d-44cb-b98a-2a9492130bda)




