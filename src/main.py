"""
TaskTracker - Gerenciador de Tarefas (CLI)
Bootcamp II - Fase 2
"""

# =====================================================================
# 1. ESTRUTURA DE DADOS
# =====================================================================

tarefas = []


# =====================================================================
# 2. CADASTRO
# =====================================================================

def criar_tarefa(titulo, descricao, prioridade, data_limite):
    return {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "data_limite": data_limite.strip(),
        "status": "Pendente",
    }


def cadastrar_tarefa():
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Alta / Média / Baixa): ")
    data_limite = input("Data limite (ex.: DD/MM/AAAA): ")

    tarefa = criar_tarefa(titulo, descricao, prioridade, data_limite)
    tarefas.append(tarefa)
    print(f"✅ Tarefa '{tarefa['titulo']}' cadastrada com sucesso! (Status: {tarefa['status']})")


# =====================================================================
# 3. LISTAGEM
# =====================================================================

def visualizar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print("-" * 40)
        print(f"  Título      : {tarefa['titulo']}")
        print(f"  Descrição   : {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade  : {tarefa['prioridade']}")
        print(f"  Data limite : {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status      : {tarefa['status']}")
    print("-" * 40)
    print(f"Total: {len(tarefas)} tarefa(s).")


# =====================================================================
# 4. MENU E LOOP PRINCIPAL
# =====================================================================

def exibir_menu():
    print("\n" + "=" * 40)
    print("   TASKTRACKER - GERENCIADOR DE TAREFAS")
    print("=" * 40)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\n👋 Encerrando o TaskTracker. Até logo!")
            break
        else:
            print(f"❌ Opção '{opcao}' inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()