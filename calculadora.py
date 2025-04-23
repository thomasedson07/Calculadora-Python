while True:
    # Receber os números do usuário
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Opções de operação
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Receber a escolha do usuário
    operacao = input("Escolha a operação (1/2/3/4/5): ")

    # Realizar a operação
    if operacao == '1':
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro! Não pode dividir por zero.")
    elif operacao == '5':
        print("Saindo da calculadora. Até mais!")
        break
    else:
        print("Opção inválida! Escolha uma operação válida.")







