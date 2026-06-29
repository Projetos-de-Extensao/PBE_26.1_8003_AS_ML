# Modelagem de Dados
@startuml

class Usuario {
  +String nome
  +Float peso_atual
}

class Playlist {
  +String nome
  +String objetivo_do_ciclo
  +DateTime data_criacao
}

class Treino {
  +String titulo
  +String descricao
}

class RegistroExecucao {
  +DateTime data_realizacao
  +String observacoes_gerais
  +Float volume_total_calculado
}

class DetalheExercicio {
  +Float carga_utilizada
  +Integer series_feitas
  +Integer repeticoes_feitas
}

Usuario "1" -- "*" Playlist : gerencia
Playlist "1" -- "*" RegistroExecucao : contém
RegistroExecucao "*" -- "1" Treino : baseia-se em
RegistroExecucao "1" -- "*" DetalheExercicio : detalha
@enduml