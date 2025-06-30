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
docker compose exec todo_app alembic upgrade head
```

## Realizar chamadas

Usar o endereço `http://localhost:8000/`, se tiver a porta ocupada, pode alterar manualmente no .env do projeto