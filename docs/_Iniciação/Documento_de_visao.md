---
id: documento_de_visao
title: Documento de Visão
---

## Introdução
Este documento define o escopo e os requisitos da plataforma FitLife, uma solução voltada para a gestão de treinos e acompanhamento de indicadores de bem-estar, desenvolvida como API REST.


## Descrição do Problema 

### Problema

Dificuldade em gerenciar e organizar rotinas de exercícios de forma analítica, muitas vezes dependendo de anotações físicas que dificultam a visualização do progresso a longo prazo.


### Impactados

Alunos da IBMEC praticantes de atividades físicas, entusiastas de bem-estar e que buscam uma rotina mais saudável.

### Consequência

A falta de um registro estruturado leva à desmotivação, estagnação nos resultados e dificuldade em ajustar cargas e intensidades de treino.

### Solução

Utilizar a aplicação que será desenvolvida visando resolver o planejamento de treinos, o catálogo de exercícios e o monitoramento de métricas corporais associando uma Playlist específica, permitindo uma análise baseada em dados (progresso e intensidade dos treinos registrados)

## Objetivos

- Prover uma interface para cadastro de rotinas de treino personalizadas.
- Permitir o acompanhamento contínuo da jornada fitness do usuário (engajamento) 
- Fornecer dados estruturados para que ele visualize sua evolução (progresso). 


## Descrição do Usuário 

- **Usuário Comum:** Pessoa que busca registrar seus treinos e acompanhar sua evolução física.
- **Administrador:** Responsável por manter o catálogo global de exercícios e grupos musculares.


## Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais
- **RF001:** O sistema deve permitir o CRUD de usuários com autenticação.
- **RF002:** O sistema deve permitir que o usuário crie planos de treino (ex: Treino A, Treino B).
- **RF003:** O sistema deve permitir a associação de múltiplos exercícios a um treino.
- **RF004:** O sistema deve permitir o registro periódico de métricas corporais (peso, altura, IMC).

### Requisitos Não Funcionais (RNF)
- **RNF001 (Segurança):** A API deve utilizar autenticação via Token JWT.
- **RNF002 (Performance):** A listagem de treinos deve carregar em menos de 300ms.
- **RNF003 (Documentação):** A API deve ser documentada automaticamente via Swagger/OpenAPI.


#### Usuários 

Alunos da IBMEC e Administradores

## Regras de Negócio

- **RN001:** Um treino só pode ser excluído se não houver registros de execução vinculados a ele.
- **RN002:** O cálculo do IMC deve ser automatizado pelo sistema após o registro de peso e altura.


## Arquitetura

A aplicação seguirá o padrão de arquitetura REST, utilizando Django no Back-end e banco de dados relacional SQLite para persistência de dados.

## Restrições

A aplicação não será responsável pelo processamento de pagamentos ou pela prescrição médica de dietas, focando estritamente na gestão de atividades físicas e métricas de bem-estar.





