# Criar Tarefa

`POST /api/v1/tasks/`

Cria uma nova tarefa.

## Corpo da requisição

```json
{
  "title": "Comprar pão",
  "description": "Na padaria da esquina"
}
```

## Respostas

- `201 Created`: tarefa criada com sucesso
- `422 Unprocessable Entity`: erro de validação
