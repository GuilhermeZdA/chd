# Comunicação Hospitalar Digital (CHD)

Repositório do projeto da disciplina de Fundamentos da Programação.

# Descrição do projeto

Comunicação Hospitalar Digital (CHD) é uma plataforma que permite aos funcionários cadastrarem pacientes, visualizar seus dados ou removerem os pacientes da lista de espera. Além disso, o sistema permite que os próprios pacientes tenham acesso a seus dados.

# Problema

CHD resolve problemas relacionados a organização dos pacientes que precisam do hospital, a dificuldade que os pacientes tem para adquirir informações sobre suas consultas.

# Instruções de execução

1. O programa deve ser executado enquanto tiver acesso a um **terminal** (terminal do VSCODE).
2. O programa inicia com uma tela que permite escolher entre **funcionário** ou **paciente**.
### Funcionário
1. Caso seja escolhido **funcionário**, o usuário será direcionado a uma tela de login para confirmar se realmente é um funcionário, necessitando de um login e senha.
2. Após a confirmação, o usuário terá acesso a uma nova tela de menu com as opções: Cadastro paciente, Ler dados, Remover paciente e Sair.
#### Cadastro
O usuário deve informar, o nome, a data de nascimento e o CPF do paciente para realizar o cadastro.
#### Ler dados
Os dados sobre todos os pacientes são informados.
#### Remover
Os usuário deve informar o CPF de um paciente para retira-lo do cadastro.
### Paciente
1. Caso seja escolhido a opção **Paciente**, o usuário será direcionado a uma tela, a qual pede que o paciente digite seu CPF.
2. Com o CPF correto enviado, o paciente tem acesso a seus próprios dados sobre a consulta.
# Exemplos de uso, quando possível

# Tarefas entre os integrantes
### Guilherme Zacarias de Andrade
- Organizou o Kanban.
- Organizou o readME.
- Desenvolveu as funcionalidades:
    - LerDados.py
    - GeradorHash.py
    - ValidarHash.py
    - AtualizarDados.py
    - BuscarPaciente.py

### Emanuel Hilley
- Organizou os slides.
- Desenvolveu as funcionalidades:
    - medico_service.py
    - paciente_service.py

### Ezequiel Ferreira
- Organizou os arquivos do projeto.
- Desenvolveu as funcionalidades:
    - auth_services.py
    - db_manager.py
    - caminhos.py

### Leonardo Mendonça
- Organizou os slides.
- Desenvolveu as funcionalidades:
    - menu.py
