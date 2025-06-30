# 📝 To-Do List API

API RESTful construída com **FastAPI**, **PostgreSQL** e **SQLAlchemy assíncrono**, com autenticação via **Bearer Token**.

---

## 🚀 Stack e escolhas técnicas

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy (async)**
- **Alembic**
- **Poetry**
- **Docker + Docker Compose**

---

## ⚙️ Como rodar o projeto com Docker

### 1. Clone o repositório


### 2. Copie o arquivo `.env.example`

```bash
cp .env.example .env
```

> O conteúdo já estará corretamente configurado para uso local via Docker.

### 3. Suba os containers

```bash
docker-compose up --build -d
```

### 4. Execute as migrações

```bash
docker compose exec todo_app alembic upgrade head
```

Acesse a documentação interativa em:  
📍 http://localhost:8000/docs

---

## 🧪 Como usar a API

### 1. Criar um usuário

```http
POST /users

{
  "username": "admin"
}
```

### 2. Usar o token nas requisições protegidas

Envie o token no header `Authorization`:

```
Authorization: Bearer seu_token_aqui
```

---

## ✅ Endpoints principais

- `POST /tasks` – Criar tarefa
- `GET /tasks` – Listar todas as tarefas
- `GET /tasks/{id}` – Obter uma tarefa
- `PUT /tasks/{id}` – Atualizar uma tarefa
- `DELETE /tasks/{id}` – Remover uma tarefa

---

## 🧠 Exemplo de criação de tarefa

```http
POST /tasks
Authorization: Bearer seu_token_aqui

{
  "title": "Estudar FastAPI",
  "description": "Revisar a documentação oficial"
}
```

---

## 📄 Documentação interativa

Disponível em:

📍 http://localhost:8000/docs  
📍 http://localhost:8000/redoc
