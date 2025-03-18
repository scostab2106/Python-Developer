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

#FUNÇÕES
# - Criar 2 novas funções "Cadastrar usuario" e "Cadastrar conta bancária"
# - Cadastrar Usuário: Armazenar numa lista(nome, data de nascimento, cpf(único) e edereço(logradouro, num - bairro - cidade/sigla estado))
# - Criar Conta: Armazenar numa lista(agencia(fixo = "0001"), numero da conta e usuário) 
# - Saque: Argumentos Keyword only -> (saldo, valor, extrato, limit, numero_saques, limite_saques) - Retorno -> (saldo e extrato)
# - Depósito: Argumentos Positional only -> (saldo, valor, extrato) - Retorno -> (sado e extrato)
# - Extrato: Positional and Keyword ->  Posicionais(saldo) Nomeados(extrato)

from datetime import date, datetime, time

date_save = datetime.now().date



menu = """
[U] - Create User
[C] - Create account
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
users = []
accs = []



    
def deposit(balance, value, extract, number_transations, / ): 
        global date_save
        date_d = datetime.now().date

        if date_d != date_save:
            number_transations = 0  
            date_save = date_d

        if number_transations >= 10:
            print("Number of transitions exceded!")
            return 

              

        if value > 0: 
            balance += value
            number_transations += 1
            date_save = datetime.now().date()
            date_transation = datetime.now().strftime("%d/%m/%Y %H:%M")
            extract = f"{date_transation}  " f"{extract}" + str(f"\n+ R${value} ")
                

        else:
            print("Invalid value, deposit should must be bigger than 0, backing to menu...")     

        return balance, extract, number_transations              
            


def withdraw(*, balance, value, extract, number_transations, number_of_withdraw , WITHDRAW_LIMIT):
    global date_save    

    date_d = datetime.now().date

    if date_d != date_save:
        number_transations = 0  
        number_of_withdraw = 0  
        date_save = date_d

    if  number_transations >= 10:
        print("Number of transitions exceded!")
        return
    
    if number_of_withdraw > WITHDRAW_LIMIT:
        print("Daily limit exceded, come back tomorrow...")
        return

    if value > balance:
        print("Insuficient Balance...")
        return
        
    if value > 500:
        print("Withdraw out of limit...")
        return

    
    balance -= value
    number_of_withdraw += 1
    number_transations += 1
    date_transation = datetime.now().strftime("%d/%m/%Y %H:%M")
    extract = f"{date_transation}  "  f"{extract}" + str(f"\n- R${value} ")
            
    return balance, extract, number_transations, number_of_withdraw

def show_extract(balance,*, extract):
    print("\nEXTRACT... \n" )
    print(extract if extract else "No transactions yet.")            
    print(extract + f"\nTOTAL ACCOUNT = R${balance}")

def create_acc():
    cpf = input("CPF: ")
    if cpf in accs:
        print("User already have account!")
        return
              
    agency = '0001'
    account_number = len(accs) + 1  
    
    accs.append([cpf,agency,account_number])
    print("Account created successfully!")


    return

def create_user():
    name = input("Name: ") 
    birt = input("Birthday (DD/MM/YYYY): ")
    cpf = input("CPF: ")

    for user in users:
        if  cpf == user[2]:
            print("User already registered!")
            return
              
    address = f"{input("Place: ")},{int(input("Number: "))} - {input("Neighborhood: ")} - {input("City: ")}/{input("State(UF): ")}"

    users.append([name, birt,cpf,address])
    print("User registered successfully!")


while True:

    option = input(menu).strip().upper()

    if option == 'D' :
        print("DEPOSIT...")
        value = float(input("Enter the deposit value: "))
        balance, extract, number_transations = deposit(balance, value, extract, number_transations)
       
    elif option == 'W':
        print("WITHDRAW...")
        balance, extract, number_transations, number_of_withdraw = withdraw(
            balance = balance, 
            value = float(input("Enter the withdraw value: ")), 
            extract = extract, 
            number_transations = number_transations, 
            number_of_withdraw = number_of_withdraw, 
            WITHDRAW_LIMIT = WITHDRAW_LIMIT)
      
    elif option == 'E':
        show_extract(balance, extract = extract)

    elif option == 'U':
        create_user()

    elif option == 'C':
        create_acc()

    elif option == 'X':
        print("LEAVE PROGRAM!")
        break
    else:
        print("CHOSE A CORRECT OPTION: ")
        continue


   
    
    

   


    