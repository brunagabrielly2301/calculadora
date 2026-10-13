def calculadora_soma():
    print("=== Calculadora de Soma de 2 Números ===")
    
    try:
        # Solicita ao usuário que digite o primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Solicita ao usuário que digite o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Realiza a soma
        resultado = num1 + num2
        
        # Exibe o resultado formatado
        print(f"\nO resultado da soma entre {num1} e {num2} é: {resultado}")
        
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

# Executa a função
calculadora_soma()