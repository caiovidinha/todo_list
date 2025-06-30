# Criar Usuário

`POST /api/v1/users/`

Cria um novo usuário e retorna um token de autenticação.

## Corpo da Requisição

```json
{
  "username": "seu_nome_de_usuário"
}
```

- `username`: obrigatório, mínimo de 3 e máximo de 30 caracteres.

## Respostas

- `201 Created`:

```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

- `409 Conflict`: usuário já existe.
- `422 Unprocessable Entity`: erro de validação no corpo da requisição.
