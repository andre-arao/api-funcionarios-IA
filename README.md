# API de informações sobre funcionários com IA

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

## Informações extras

- [Collection Postman](./postman/API com IA.postman_collection.json)
- GET: http://localhost:5000/api/funcionarios (Listar funcionários)
- POST: http://localhost:5000/api/funcionarios (Pergunta sobre funcionários)
- POST: http://localhost:5000/api/criar/funcionarios (Criar Funcionário)

# Evidências