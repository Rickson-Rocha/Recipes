 # Projeto Recipe

 O Projeto Recipe é uma aplicação web desenvolvida com Django e Django Rest Framework. O objetivo da aplicação é permitir que os usuários possam criar uma conta de login e compartilhar receitas, editá-las e excluí-las.

 ## Funcionalidades

* Criação de conta de login
* Autenticação de usuários
* Criação, edição e exclusão de receitas
* Listagem de receitas
* Busca por receitas por nome ou ingredientes

# Instalação
1. Clone o repositório:


```bash
 git clone:   https://github.com/seu-usuario/projeto-recipe.git
```

2. Entre na pasta do projeto::


```bash
 cd projeto-recipe
```

3. Crie e ative um ambiente virtual:


```bash
 python -m venv venv
 source venv/bin/activate
```

4. Execute as migrações:


```bash
   python manage.py migrate
```

5. Crie um superusuário:


```bash
  python manage.py createsuperuser
```

6. Execute a aplicação:


```bash
 python manage.py runserver
```

## Endpoints da API
* GET /api/recipes/ - Lista todas as receitas
* POST /api/recipes/ - Cria uma nova receita
* GET /api/recipes/<int:pk>/ - Exibe uma receita específica
* PUT /api/recipes/<int:pk>/ - Atualiza uma receita
* DELETE /api/recipes/<int:pk>/ - Exclui uma receita

## Tecnologias utilizadas

* Python 3
* Django
* Django Rest Framework
* SQLite
* Bootstrap
* HTML
* CSS
* JavaScript

### Autor
Este projeto foi desenvolvido por Rickson Rocha.



