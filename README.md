# TaskTracker – Gerenciador de Tarefas

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas, desenvolvida na **Fase 2 (Entrega Intermediária)** do Bootcamp II.

## O problema a ser resolvido

No dia a dia, pode ocorrer de muitas pessoas e equipes terem muitas tarefas e compromissos ao mesmo tempo: trabalhar, estudar, entregas e prazos, reuniões, etc. Quando não há uma organização sistemática, é fácil esquecer esses compromissos e perder prazos, ou não saber o que já foi realizado e o que ainda está pendente. Isso pode resultar em adiamentos e acúmulos de tarefas que causam desordem, estresse, retrabalho e perda de produtividade.

## A solução proposta

O TaskTracker é um sistema de gerenciamento de tarefas que ajuda os usuários a manter suas tarefas e compromissos organizados em um único lugar.

## Funcionalidades

A aplicação funciona por meio de um menu contínuo no terminal:

```
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
```

- **Cadastrar nova tarefa:** informa título, descrição, prioridade e data limite. Toda tarefa é criada com status **Pendente**.
- **Visualizar tarefas cadastradas:** mostra todas as tarefas, ordenadas por prioridade (Alta → Média → Baixa), com o total de tarefas pendentes e concluídas. Se não houver tarefas, exibe um aviso.
- **Sair da aplicação:** encerra o programa.

### Regras de negócio

| Campo | Regra |
|---|---|
| Título | Obrigatório. Não aceita vazio, só espaços ou um título que já exista. |
| Descrição | Texto livre. |
| Prioridade | Aceita apenas **Alta**, **Média** (ou Media) e **Baixa**. Outros valores geram erro e a pergunta é repetida. |
| Data limite | Formato livre ou DD/MM/AAAA. |
| Status | Definido automaticamente como **Pendente** no cadastro. |

## Tecnologias utilizadas

- **Python 3** (apenas biblioteca padrão, sem dependências externas)
- **Git** para versionamento
- **GitHub** para hospedagem do repositório
- **VS Code** como editor

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md                    # Documentação do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf  # Planejamento da Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação
```

## Instalação e execução

**Pré-requisitos:** Python 3 e Git instalados.

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd NOME-DO-REPOSITORIO
   ```
3. Execute a aplicação:
   ```bash
   python3 src/main.py
   ```
   No Windows, use `python src/main.py`.

## Próximos passos


- Fase 3: empacotamento da aplicação, containerização com Docker, testes e deploy.