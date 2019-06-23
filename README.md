# REST API com Flask e SQL Alchemy
> Desafio Pareto - API REST usando Python Flask e SQL Alchemy

## Usando Pipenv

``` bash
# Ativando venv
$ pipenv shell

# Instalar
$ pipenv install

# Criar DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Init Server (http://localhost:5000)
python app.py
```

## Endpoints

* GET     /climate
* GET     /climate/id
* POST    /climate
* PUT     /climate/id
* DELETE  /climate/id
