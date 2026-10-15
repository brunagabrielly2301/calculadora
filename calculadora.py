def calculadora():
    print("=== Calculadora de Soma, Subtração e Multiplicação ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação (NOVO!)")
    
    # Solicita a escolha da operação
    opcao = input("Escolha a operação (1, 2 ou 3): ")
    
    if opcao not in ['1', '2', '3']:
        print("\nErro: Opção inválida. Escolha 1, 2 ou 3.")
        return
        
    try:
        # Solicita ao usuário que digite os números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realiza a operação escolhida
        if opcao == '1':
            resultado = num1 + num2
            operacao_str = "soma"
            sinal = "+"
        elif opcao == '2':
            resultado = num1 - num2
            operacao_str = "subtração"
            sinal = "-"
        else:
            resultado = num1 * num2
            operacao_str = "multiplicação"
            sinal = "×"
            
        # Exibe o resultado formatado
        print(f"\nO resultado da {operacao_str} ({num1} {sinal} {num2}) é: {resultado}")
        print("Obrigado por usar a nossa calculadora melhorada!")
        
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

# Executa a função
calculadora()