# Atualizar Tarefa

`PUT /api/v1/tasks/{task_id}`

Atualiza uma tarefa existente pelo `task_id`.

## Corpo da Requisição

```json
{
  "title": "Atualizar título",
  "description": "Nova descrição",
  "is_done": true
}
```

Campos são opcionais. Envie apenas os que deseja alterar.

## Respostas

- `200 OK`: tarefa atualizada com sucesso
- `401 Unauthorized`: token inválido ou ausente
- `404 Not Found`: tarefa não encontrada
- `422 Unprocessable Entity`: erro de validação