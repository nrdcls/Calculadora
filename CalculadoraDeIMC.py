def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    
    imc = peso / altura ** 2
    
    print("\nSeu IMC é: {:.2f}".format(imc))
    
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Seu peso está dentro da faixa saudável.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")

if __name__ == "__main__":
    main()

