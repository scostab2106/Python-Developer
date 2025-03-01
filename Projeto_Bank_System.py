# DEPÓSITO:
# -  Depositar valores positivos para a propria conta bancária
# - Todos os depósitos devem ser armezenados em uma variável e exibidos na operação extrato
# - Apenas 1 usuário

# SAQUE:
# - 3 saques diários com limite máximo de 500 reais por saque,
# - Caso nao tenha saldo em conta o sistema deve exibir uma mensagem informando que não sera possível sacar por falta de saldo
# - Todos os saques devem ser armezenados em uma variável e exibidos na operação extrato

# EXTRATO:
# - Listar todos os depositos e saques realizados na conta.
# - No fim da listagem deve ser exibido o saldo atual da conta
# - Devem ser exibidos utilizando o formato  R$ xxx.xx


menu = """
[D] - Deposit
[W] - Withdraw
[E] - Extract
[X] - Leave

=> """

balance = 0.00
limit = 500.00
extract = ""
number_of_withdraw = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(menu)


    if option.upper() == 'D' :
        print("DEPOSIT...")

        deposit = float(input("Enter the deposit value: "))

        if deposit > 0:
            balance = balance + deposit
            extract = f"{extract}" + str(f"\n+R${deposit}")
            continue

        else:
            deposit = float(input("Invalid value, please write value big than 0: "))
            balance = balance + deposit
            extract = f"{extract}" + str(f"\n+R${deposit}")

            if deposit <= 0:
                print("Invalid value, backing to menu...")
                continue
            else:
                continue


    elif option.upper() == 'W':
        print("WITHDRAW...")

        withdraw = -1

        while withdraw < balance:

            withdraw = float(input("Enter the withdraw value: "))
            if withdraw > balance:
                print("Insuficient Balance...")
                continue

            elif withdraw > 500:
                print("Withdraw out of limit...")
                continue

            else:
                number_of_withdraw = number_of_withdraw +  1

                if number_of_withdraw > WITHDRAW_LIMIT:
                    print("Daily limit exceded, come back tomorrow...")
                    break

                balance = balance - withdraw
                extract = f"{extract}" + str(f"\n-R${withdraw}")
                break
        continue





    elif option.upper() == 'E':
        print("EXTRACT...")

        print(extract)
        print(f"\nTOTAL DA CONTA = R${balance}")
        continue

    elif option.upper() == 'X':

        print("LEAVE PROGRAM!")
        break


    else:

        print("WRITE A CORRECT OPTION: ")

        continue
