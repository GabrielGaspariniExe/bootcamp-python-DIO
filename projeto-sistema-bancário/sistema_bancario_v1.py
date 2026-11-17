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
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "D":
        print ("Depositar\n")
        while True:
            deposito = int(input("Digite o valor que você deseja depositar: R$"))
            if deposito <= 0:
                print("O valor deve conter apenas números positivos.")
            else:
                break
            saldo = deposito
            
    elif opcao == "S" and numero_saques :
        print ("Sacar")
        quantidades_saques -= LIMITES_SAQUES
        if LIMITES_SAQUES >= 1 and saque :
            

    #elif opcao == "E":
        #print ("Extrato")

    elif opcao == "F":
        print("Finalizando, obrigado por escolher o JurandasBank!")
        break

    else:
        print("Escolha uma das opções com a correspondência exata.")

print(deposito)



