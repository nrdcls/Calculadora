class GerenciadorTarefas:
    def __init__(self) :
        self.tarefas = []
    def adicionar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)
        print ("Tarefa adicionada com sucesso!")
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice)
            print (f"Tarefa '{tarefa_removida}' removida com sucesso")
        else: print("Índice inválido.")
    def visualizar_tarefas(self):
        if self.tarefas:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i + 1}. {tarefa}")
        else:
            print("Não há tarefas pendentes.")
def main():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Tarefas")
        print("2. Remover Tarefas")
        print("3. Visualizar Tarefas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            gerenciador.adicionar_tarefas(tarefa)
        elif opcao == "2":
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            gerenciador.remover_tarefas(indice)
        elif opcao == "3":
            gerenciador.visualizar_tarefas()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()