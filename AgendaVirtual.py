class Contato:
    def __init__(self, nome, telefone, email):
        # Inicializa um novo contato com nome, telefone e email
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        # Retorna uma string formatada representando o contato
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Agenda:
    def __init__(self):
        # Inicializa uma nova agenda sem contatos
        self.contatos = []

    def adicionar_contato(self, contato):
        # Adiciona um novo contato à agenda
        self.contatos.append(contato)

    def visualizar_contatos(self):
        # Verifica se a agenda possui contatos
        if self.contatos:
            print("Lista de contatos:")
            # Itera sobre os contatos e os imprime
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. {contato}")
        else:
            # Se a agenda estiver vazia, exibe uma mensagem
            print("A agenda está vazia.")

def main():
    # Cria uma nova agenda
    agenda = Agenda()

    while True:
        # Exibe o menu de opções
        print("\nAgenda Virtual")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Sair")

        # Solicita ao usuário que escolha uma opção
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adiciona um novo contato à agenda
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            novo_contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(novo_contato)
            print("Contato adicionado com sucesso!")
        elif opcao == "2":
            # Exibe os contatos da agenda
            agenda.visualizar_contatos()
        elif opcao == "3":
            # Encerra o programa
            print("Saindo...")
            break
        else:
            # Mensagem de erro para opções inválidas
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
