def main():
    # Definição das funções de conversão
    def quilometros_para_milhas(quilometros):
        return quilometros * 0.621371
    
    def celsius_para_fahrenheit(celsius):
        return celsius * 9/5 + 32

    # Apresentação do programa ao usuário
    print("Bem-vindo ao conversor de unidades!")
    print("Selecione a conversão desejada:")
    print("1. Quilômetros para Milhas")
    print("2. Celsius para Fahrenheit")

    # Solicitação da escolha do usuário
    opcao = input("Digite o número da opção desejada: ")

    # Verificação da escolha do usuário e execução da conversão correspondente
    if opcao == "1":
        quilometros = float(input("Digite a quantidade de quilômetros: "))
        milhas = quilometros_para_milhas(quilometros)
        print(f"{quilometros} quilômetros equivalem a {milhas:.2f} milhas.")
    elif opcao == "2":
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
