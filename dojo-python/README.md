# DOJO - Python

## Descrição
A Serie de animação "Rick and Morty", estreada em Dezembro de 2013, acabou se tornando um sucesso ao longos dos anos, portanto o numero de temporadas, episodios, personagens e cenarios cresceram bastante. Assim sendo, para melhor organização desse conjunto de dados, desenvolva uma API, disponibilizando os dados com os requisitos a baixo.

### Requisitos
* [ ] Criar [DAOs](https://pt.wikipedia.org/wiki/Objeto_de_acesso_a_dados), para cada uma das entidades correpondentes em [data](./data).

* [ ] Carregar os dados disponilizados em [data](./data), conforme sua entidade correspondente, toda vez que a API for iniciada.

* [ ] Disponibilizar os dados de cada uma da entidades, com os seguintes endpoitons:
    * GET => /character
    * GET => /character/<id_character>
    * GET => /location
    * GET => /location/<id_location>
    * GET => /episode
    * GET => /episode/<id_epsode>

* [ ] Na busca por episodio, é necessario buscar todos os personagens dos respectivos espisodios, com seguinte endpoint:
    * GET => /episode/<id_epsode>/character

* [ ] Criar busca personalizada de episodios por nome, utilizando [Query Parameters](https://guides.emberjs.com/release/routing/query-params/)
    * GET => /episode?nome=<ep_name>

* [ ] Criar busca personalizada de episodios por Temporada, com seguinte endpoint:
    * GET => /episode/season/<number_season>

* [ ] Passar em todos os 4 testes :p.

## Tecnologias
* [API](https://rickandmortyapi.com/documentation/)
* [Python 3](https://www.python.org/download/releases/3.0/) - ultima versão python
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework server
* [PyTest](https://docs.pytest.org/en/latest/getting-started.html) - Framework test

## Instalação
```bash
> python -m venv venv
> source ./venv/bin/active
> pip install -r requirements.txt
```

## Pós Instalação
```bash 
> python extract_data.py
```

## Como Testar?
```bash
> pytest
```

## Como usar?
```bash
> python server.py
```
