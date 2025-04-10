# API RENAVE

### Requisitos Funcionais

- [x] Deve ser possível buscar cliente
- [] Deve ser possível buscar o veículo
- [x] Deve ser possível cadastrar um cliente no Renave
- [] Deve ser possível cadastrar um veículo no Renave

### Regras de Negócio
- [x] Só pode ser enviado os dados com o Token de Autenticação
- [x] Só vai ser enviado os dados de Clientes com Status 0

### Requisitos não funcionais
- [x] A Aplicação deve ter uma agendador de tarefas (CRON)
- [x] Precisa alterar no Banco de dados para Status 1, retornar com sucesso da API
