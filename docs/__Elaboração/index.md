
# Projeto Arquitetural

## Visão Geral da Arquitetura
A plataforma **FitLife** utiliza o padrão **MVT (Model-View-Template)** do Django, estendido pelo **Django REST Framework (DRF)** para fornecer uma arquitetura baseada em serviços (API REST).

## Fluxo de Dados
1. **Middleware:** Gerencia a autenticação via JWT (JSON Web Token).
2. **Serializers:** Validam e transformam os dados de entrada (JSON) em objetos Python/Django.
3. **Views/Viewsets:** Implementam a lógica de negócio e as regras de filtragem.
4. **Models:** Representam a camada de persistência no banco de dados SQLite.

## Endpoints da API (Contrato)
| Verbo | Endpoint | Descrição | Parâmetros |
| :--- | :--- | :--- | :--- |
| GET | `/api/exercicios/` | Lista catálogo de exercícios | `grupo_muscular` |
| POST | `/api/treinos/` | Cria um novo plano de treino | `nome`, `descricao` |
| POST | `/api/execucoes/` | Registra a realização de um treino | `treino_id`, `playlist_url`, `exercicios_data` |
| GET | `/api/progresso/` | Retorna métricas de evolução | `data_inicio`, `data_fim` |