'''
    Para essa primeira versão, devemos criar um sistema bacário que realize apenas 3 operações, sendo elas depósito, saque e extrato.
        - Operação Depósito:
            Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma
            não precisamos identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos
            na operação de extrato.
        - Operação Saque:
            O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o
            sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser
            armazenados em uma variável e exibidos na operação de extrato.
        - Operação de Extrato:
            Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
            Os valores devem ser exibidos utilizando o formato R$ xxx.xx,exemplo:
            1500.45 = R$ 1500.45
'''
#menu de opções do sistema bancário
menu = """

Bem vindo ao JurandasBank

[D] Depositar
[S] Sacar
[E] Extrato
[F] Finalizar

=> """

saldo = 0
limite = 500
extrato = ""
valor_sacado = 0
numero_saques = 0
LIMITES_SAQUES = 3

# Laço de repetição que contém as opções possíveis para serem realizadas do sistema.
while True:
    opcao = input(menu)
    # Na primeira operação nos recebemos um valor do usuário e realizamos a validação do valor, se é positivo ou negativo.
    # E após finalizar armazenamos na variável global "saldo"
    if opcao == "D":
        print ("Depositar\n")
        while True:
            deposito = int(input("Digite o valor que você deseja depositar: R$"))
            if deposito <= 0:
                print("O valor deve conter apenas números positivos.")
            else:
                break
        saldo += deposito
            
    elif opcao == "S":
        numero_saques += 1
        if numero_saques > LIMITES_SAQUES:
            print("Você não pode realizar essa operação defido ao limite de saque diário excedido, volte amanhã.\n Agradecemos por usar o JurandasBank!")
            break
        else:
            valor_sacado = int(input("Digite o valor que você deseja sacar: R$"))
            while True:
                if valor_sacado > limite:
                    valor_sacado = int(input("Não é permitio realizar essa operação, saque é maior que R$500\nDigite outro valor: R$"))
                elif valor_sacado > saldo:
                    valor_sacado = int(input(f"O valor para saque excede o valor do saldo atual.\nSaldo atual é de R${saldo}.\nFavor digitar um valor válido para a operação: R$"))
                else:
                    print(f"Realizando saque no valor de R${valor_sacado}.")
                    break

    #elif opcao == "E":
        #print ("Extrato")

    elif opcao == "F":
        print("Finalizando, obrigado por escolher o JurandasBank!")
        break

    else:
        print("Escolha uma das opções com a correspondência exata.")

print(deposito)
print(valor_sacado)



