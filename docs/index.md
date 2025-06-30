# Documentação - ToDo API

Bem-vindo à documentação oficial do projeto ToDo API. Aqui você encontrará todas as informações necessárias para integrar, utilizar e contribuir com a aplicação.

## Organização do projeto

- `app/`: Código da aplicação
- `app/domain`: Divisão por entidades (user, task)
- `app/core`: Configurações como DB e settings
- `app/auth`: Autenticação e dependências
- `docs/`: Documentação via MkDocs

## Boas práticas

- Uso de exceptions customizadas
- Tipagem forte
- SQLAlchemy assíncrono
- Separação por camadas: model, repository, service, use_case, routes
