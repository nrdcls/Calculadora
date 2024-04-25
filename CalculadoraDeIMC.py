def main():
    # Mensagem de boas-vindas
    print("Calculadora de Índice de Massa Corporal (IMC)")
    
    # Solicita ao usuário que insira seu peso em kg
    peso = float(input("Digite o seu peso em kg: "))
    
    # Solicita ao usuário que insira sua altura em metros
    altura = float(input("Digite a sua altura em metros: "))
    
    # Calcula o IMC (Índice de Massa Corporal)
    imc = peso / altura ** 2
    
    # Exibe o valor do IMC formatado com duas casas decimais
    print("\nSeu IMC é: {:.2f}".format(imc))
    
    # Com base no valor do IMC, fornece uma mensagem sobre a condição de peso
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Seu peso está dentro da faixa saudável.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")

# Verifica se o script está sendo executado como um programa principal
if __name__ == "__main__":
    main()
