''' Calculadora com while'''
while True:
    # Escolhe os números para a operação
    numero_1 = float(input('Digite um número: '))
    numero_2 = float(input('Digite um número: '))

    # Escolhe uma das operações
    print('Digite: (1) - soma, (2) - subtração, (3) - multiplicação, (4) - divisão')
    operacao = str(input('Escolha operação: '))

    # Desenvolvimento da calculadora
    if operacao == '1': #Identação o if tem que ficar na mesma linha do 'numero_1, numer_2...""
        resultado = numero_1 + numero_2
        print('A soma de {} + {} é igual: {}'.format(numero_1, numero_2, resultado))
    elif operacao == '2':
        resultado = numero_1 - numero_2
        print('A subtração de {} - {} é igual: {}'.format(numero_1, numero_2, resultado))
    elif operacao == '3':
        resultado = numero_1 * numero_2
        print('A multiplicação de {} * {} é igual: {}'.format(numero_1, numero_2, resultado))
    elif divisao == '4': 
        resultado = numero_1 / numero_2
        print('A divisão de {} / {} é igual: {}'.format(numero_1, numero_2, resultado))
    else:
        print('Operação inválida')

    sair = str(input('Digite "sair" para encerrar ou pressione Enter para continuar: ')).lower()
    if sair == 'sair':
        break