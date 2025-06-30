# Setup

## Requisitos
- Python 3.12
- Docker e Docker Compose
- Poetry

## Subir banco, api e documentação

```bash
cp .env.example .env
```

```bash
docker compose up --build -d
```

## Executar migrations

```bash
docker exec todo_app alembic upgrade head
```

## Realizar chamadas

Usar o endereço `http://localhost:8000/`. Se tiver a porta ocupada, ela será realocada manualmente pelo uvicorn, mas caso prefira, pode alterar manualmente no docker-compose e Dockerfile do projeto.