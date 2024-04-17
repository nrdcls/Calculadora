import sys
import io

class GerenciadorTarefas:
    def __init__(self):
        # Inicializa a lista de tarefas como vazia
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        # Adiciona uma nova tarefa à lista de tarefas
        self.tarefas.append(tarefa)
        # Imprime uma mensagem indicando que a tarefa foi adicionada com sucesso
        print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self, indice):
        # Verifica se o índice está dentro dos limites da lista de tarefas
        if 0 <= indice < len(self.tarefas):
            # Remove a tarefa com o índice especificado
            tarefa_removida = self.tarefas.pop(indice)
            # Imprime uma mensagem indicando que a tarefa foi removida com sucesso
            print(f"Tarefa '{tarefa_removida}' removida com sucesso")
        else:
            # Caso o índice seja inválido, imprime uma mensagem de erro
            print("Índice inválido.")

    def visualizar_tarefas(self):
        # Verifica se há tarefas na lista
        if self.tarefas:
            # Se houver tarefas, imprime cada uma delas com seu número de índice
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i + 1}. {tarefa}")
        else:
            # Se não houver tarefas, imprime uma mensagem indicando que não há tarefas pendentes
            print("Não há tarefas pendentes.")

def main():
    # Define a codificação UTF-8 para a saída padrão
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Cria uma instância do GerenciadorTarefas
    gerenciador = GerenciadorTarefas()

    while True:
        # Exibe o menu de opções
        print("\n=== Menu ===")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Visualizar Tarefas")
        print("4. Sair")

        # Solicita ao usuário que escolha uma opção
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Se a opção escolhida for adicionar uma tarefa, solicita uma nova tarefa e a adiciona
            tarefa = input("Digite a nova tarefa: ")
            gerenciador.adicionar_tarefa(tarefa)
        elif opcao == "2":
            # Se a opção escolhida for remover uma tarefa, solicita o índice da tarefa a ser removida e a remove
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            gerenciador.remover_tarefa(indice)
        elif opcao == "3":
            # Se a opção escolhida for visualizar as tarefas, exibe as tarefas pendentes
            gerenciador.visualizar_tarefas()
        elif opcao == "4":
            # Se a opção escolhida for sair, encerra o programa
            print("Saindo do programa...")
            break
        else:
            # Se a opção escolhida for inválida, exibe uma mensagem de erro
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
