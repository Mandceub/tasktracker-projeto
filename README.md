# TaskTracker – Gerenciador de Tarefas

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas, desenvolvida no Bootcamp II e **conteinerizada com Docker na Fase 3 (Entrega Final)**.

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
- **Docker** para conteinerização da aplicação
- **Docker Compose** para orquestrar a execução interativa
- **Git** para versionamento
- **GitHub** para hospedagem do repositório
- **VS Code** como editor

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md                    # Documentação do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
├── Dockerfile                   # Receita para construir a imagem Docker
├── docker-compose.yml           # Configuração da execução interativa do container
├── docs/
│   └── planejamento_logico.pdf  # Planejamento da Fase 1
└── src/
    └── main.py                  # Código-fonte da aplicação
```

## Executando com Docker (recomendado)

**Pré-requisito:** Docker Desktop instalado e aberto.

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/Mandceub/tasktracker-projeto.git
```

```bash
cd tasktracker-projeto
```

### 1. Construir a imagem

```bash
docker build -t tasktracker .
```

### 2. Rodar o container em modo isolado

```bash
docker run -it --rm tasktracker
```

O `-it` é necessário porque a aplicação usa `input()`: o `-i` mantém a entrada de dados aberta e o `-t` cria um terminal para o menu interativo.

### 3. Rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker
```

O `docker compose run` gera um nome automático para o container. Para usar o nome definido no `docker-compose.yml` (`tasktracker-app`), rode:

```bash
docker compose run --rm --name tasktracker-app tasktracker
```

### Dockerfile x docker-compose.yml

- **Dockerfile:** é a receita que gera a imagem. Define a imagem base (Python 3.11), copia o código para dentro do container e indica o comando que inicia a aplicação.
- **docker-compose.yml:** orquestra a execução do container. Guarda as configurações em um arquivo, como o nome do container e as opções `stdin_open: true` (entrada de dados aberta) e `tty: true` (terminal virtual), que permitem usar o menu interativo.

## Executando sem Docker (Python local)

**Pré-requisitos:** Python 3 e Git instalados.

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mandceub/tasktracker-projeto.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python3 src/main.py
   ```
   No Windows, use `python src/main.py`.

## Próximos passos

- Implementar a opção de marcar tarefa como concluída (prevista no planejamento da Fase 1).
- Implementar a persistência dos dados, para que as tarefas não se percam ao encerrar a aplicação.
