import json
from pathlib import Path

ARQUIVO = Path("tarefas.json")


def carregar_tarefas():
    if ARQUIVO.exists():
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["concluida"] else "✖"
        print(f"{i:>2} - [{status}] {tarefa['descricao']}")


def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()

    if not descricao:
        print("Descrição não pode ser vazia.")
        return

    tarefas.append({
        "descricao": descricao,
        "concluida": False
    })

    print("Tarefa adicionada com sucesso!")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Número da tarefa concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Número inválido.")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Número da tarefa para remover: ")) - 1
        removida = tarefas.pop(indice)
        print(f"Tarefa '{removida['descricao']}' removida.")
    except (ValueError, IndexError):
        print("Número inválido.")


def menu():
    print("""
1 - Listar tarefas
2 - Adicionar tarefa
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair
""")


def main():
    tarefas = carregar_tarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            salvar_tarefas(tarefas)
            print("Tarefas salvas. Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
