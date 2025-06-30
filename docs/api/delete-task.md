# Deletar Tarefa

`DELETE /api/v1/tasks/{task_id}`

Remove uma tarefa existente do usuário autenticado.

## Parâmetros de Caminho

- `task_id`: UUID da tarefa que será deletada.

## Respostas

- `204 No Content`: tarefa removida com sucesso (sem corpo de resposta).
- `404 Not Found`: tarefa não encontrada.
- `401 Unauthorized`: token inválido ou ausente.
- `422 Unprocessable Entity`: ID malformado.
