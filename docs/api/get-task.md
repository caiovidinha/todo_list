# Listar Tarefas

`GET /api/v1/tasks/`

Retorna a lista de tarefas do usuário autenticado.

## Respostas

```json
[
  {
    "id": "uuid",
    "title": "Comprar pão",
    "description": "Ir na padaria",
    "is_done": false,
    "created_at": "2024-06-28T12:34:56.789Z",
    "updated_at": null
  }
]
```

- `200 OK`: lista de tarefas
- `401 Unauthorized`: token inválido ou ausente

---

# Buscar Tarefa por ID

`GET /api/v1/tasks/{task_id}`

Retorna os dados de uma tarefa específica do usuário autenticado.

## Parâmetros

- `task_id` (UUID): ID da tarefa

## Respostas

```json
{
  "id": "uuid",
  "title": "Comprar pão",
  "description": "Ir na padaria",
  "is_done": false,
  "created_at": "2024-06-28T12:34:56.789Z",
  "updated_at": null
}
```

- `200 OK`: tarefa encontrada
- `401 Unauthorized`: token inválido ou ausente
- `404 Not Found`: tarefa não encontrada
- `422 Unprocessable Entity`: formato de UUID inválido
