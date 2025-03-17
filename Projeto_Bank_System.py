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


#TIME
# - Estabelecer um limite de 10 transações diárias para uma conta
# - Se o Usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele axcedeu o número de transações permitidas para aquele dia
# - Mostra no extrato, a data e hora de todas as transações.

from datetime import date, datetime, time

date_save = datetime.date()



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
number_transations = 0




    
def deposit(): 
        date_d = datetime.date()

        if date_d == date_save and number_transations >= 10:
            print("Number of transitions exceded!")
            return

        else:        
            print("DEPOSIT...")

            deposit = float(input("Enter the deposit value: "))

            if deposit > 0: 
                balance = balance + deposit
                number_transations = number_transations + 1
                date_save = datetime.now()
                date_ptbr = date_save.strftime("%d/%m/%Y %H:%M")
                date_transation = str(date_ptbr)
                extract = f"{date_transation}  " f"{extract}" + str(f"\n+ R${deposit} ")
                return

            else:
                deposit = float(input("Invalid value, please write value big than 0: "))
                balance = balance + deposit
                number_transations = number_transations + 1
                date_save = datetime.now()
                date_ptbr = date_save.strftime("%d/%m/%Y %H:%M")
                date_transation = str(date_ptbr)
                extract = f"{date_transation} " f"{extract}" + str(f"\n+ R${deposit} ")
                

                if deposit <= 0:
                    print("Invalid value, backing to menu...")
                    return
                else:
                    return
    

def withdraw():
        print("WITHDRAW...")

        date_d = datetime.date()

        if date_d == date_save and number_transations >= 10:
            print("Number of transitions exceded!")
            return

        else:
            withdraw = -1

            while withdraw < balance:

                withdraw = float(input("Enter the withdraw value: "))
                if withdraw > balance:
                    print("Insuficient Balance...")
                    return

                elif withdraw > 500:
                    print("Withdraw out of limit...")
                    return

                else:
                    number_of_withdraw = number_of_withdraw +  1

                    if number_of_withdraw > WITHDRAW_LIMIT:
                        print("Daily limit exceded, come back tomorrow...")
                        break

                    balance = balance - withdraw
                    date_save = datetime.now()
                    date_ptbr = date_save.strftime("%d/%m/%Y %H:%M")
                    date_transation = str(date_ptbr)
                    extract = f"{date_transation}  "  f"{extract}" + str(f"\n- R${withdraw} ")
                    number_transations = number_transations + 1
                    break
            return


def show_extract(extract):
        print("\nEXTRACT... \n" )        
        
        return print(extract + f"\nTOTAL DA CONTA = R${balance}")


while True:

    option = input(menu)

    if option.upper() == 'D' :
        deposit()
       
    elif option.upper() == 'W':
        withdraw()
      
    elif option.upper() == 'E':
        show_extract()
    elif option.upper() == 'X':
        print("LEAVE PROGRAM!")
        break
    else:
        print("WRITE A CORRECT OPTION: ")
        continue


   
    
    

   


    