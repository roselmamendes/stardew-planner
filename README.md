# Stardew Planner

Um gerenciador para o jogo Stardew Valley.

## Desenvolvimento

- Docker
- Django
- Postgres

### Comandos

- Para executar o projeto localmente: docker-compose up
- Para abrir o terminal no container do Django - após executar o compose: docker exec -it stardew-planner-web-1 /bin/sh
- Para abrir o terminal do container do Postgres: docker exec -it stardew-planner-db-1 /bin/sh

**Comandos container Django**

- python manage.py makemigrations
- python manage.py migrate
- python manage.py shell

**Comandos container Postgres**

- psql -U postgres postgres

### Urls locais

- http://0.0.0.0/planner
- http://0.0.0.0/admin