# DOJO - Python
 
## Descrição
>A Série de animação "Rick and Morty", estreada em Dezembro de 2013, acabou se tornando um sucesso ao longos dos anos, portanto o número de temporadas, episódios, personagens e cenários cresceram bastante. Assim sendo, para melhor organização desse conjunto de dados, desenvolva uma API, disponibilizando os dados com os requisitos abaixo.
 
### Requisitos
* [ ] Criar [DAOs](https://pt.wikipedia.org/wiki/Objeto_de_acesso_a_dados), para cada uma das entidades correpondentes em [data](./data).
 
* [ ] Carregar os dados disponibilizados em [data](./data), conforme sua entidade correspondente, toda vez que a API for iniciada.
 
* [ ] Disponibilizar os dados de cada uma da entidades, com os seguintes endpoints:
   * GET => /character
   * GET => /character/<id_character>
   * GET => /location
   * GET => /location/<id_location>
   * GET => /episode
   * GET => /episode/<id_epsode>
 
* [ ] Na busca por episódio, é necessário buscar todos os personagens dos respectivos episódios, com seguinte endpoint:
   * GET => /episode/<id_epsode>/character
 
* [ ] Criar busca personalizada de episodios por nome, utilizando [Query Parameters](https://guides.emberjs.com/release/routing/query-params/)
   * GET => /episode?nome=<ep_name>
 
* [ ] Criar busca personalizada de episódios por Temporada, com seguinte endpoint:
   * GET => /episode/season/<number_season>
 
* [ ] Passar em todos os 4 testes :p.
 
***
 
## Tecnologias
* [API](https://rickandmortyapi.com/documentation/) - Dados utilizados da API RickAndMorty
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
 
***
 
## Arquitetura
 
* [\_\_test__](./__test__) - Responsavel por garantir o funcionamento, a confiabilidade da aplicação e que a comunicação das ações estejam de forma correta.
 
* [app](./app) - Tem com objetivo agrupar os serviços que compõe a aplicação.
   * [component](#component) - Tem como objetivo organizar de acordo com cada regra de negócio. (ex: users, posts)
   * [launcher](./app/launcher.py) - Responsável por centralizar todos os componentes da aplicação.
* [requirements](./requirements.txt) - Responsável por definir padronização de versão as dependências.
* [venv](https://docs.python.org/3/library/venv.html) - Responsavel por criar um ambiente virtual, abstraindo configurações locais da máquina sendo utilizada.
* [config](./config.py) - Centralização de constantes, para a aplicação.
* [server](./server.py) - Responsável por iniciar a aplicação.
 
 
### Component
 
* [routes](./app/main/routes.py) - Tem como objetivo, na determinação de qual ação/método deve ser executado na aplicação, criando um acesso externo.
* [model](./examples/model.py) - Tem como responsabilidade na manipulação dos dados de entrada externa, aplicando a regra de negócio proposta e enviar ou não para o armazenamento do banco de dados, através da camada DAO.
* [dao](./examples/dao.py) - Tem como responsabilidade criar uma camada de abstração, para a persistência dos dados, assim, separando a regra de negócio das de acesso ao banco.
 
***
 
# De Terceiros
 
* https://rickandmortyapi.com/