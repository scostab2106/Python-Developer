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

from datetime import datetime

from abc import ABC, abstractmethod

date_save = datetime.now().date



menu = """
[U] - Create User
[C] - Create account
[D] - Deposit
[W] - Withdraw
[E] - Extract
[X] - Leave

=> """


extract = ""


class Account:
    def __init__(self, number, client):

        self._balance = 0
        self._number = number
        self._agency = '0001'
        self._client = client
        self._history = History()


    @property
    def balance(self):

        return self._balance

    @property
    def number(self):

        return self._number
    
    @property
    def agency(self):
        return self._agency
    
    @property
    def client(self):
        return self._client
    
    @property
    def history(self):
        return self._history

    @classmethod
    def new_account(cls, client, number):

        return cls(number, client)


    def withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("Insuficient Balance!")
            return False

        elif value > 0:
            self._saldo -= value
            print("Seccess!")
            return True
        
        else: 
            print("Invalid Value!")
            return False
   


    def deposit(self, value): 
        
            
        if value > 0:
            self._saldo += value
            print("Success!")
            
        else:
            print("Invalid Value!")
            return False
        
        return True
      
            
class Corrent_Account(Account):
    def __init__(self, number, client, limit = 500, withdraw_limit = 3):
        super().__init__(number, client)

        self.limit = limit
        self.withdraw_limit = withdraw_limit
    
    def withdraw(self, value):

        global date_save 
        
        number_of_withdraw = len([transation for transation in self.history.transations if transation["type"] == Withdraw.__name__])
        
        
        date_d = datetime.now().date

        if date_d != date_save:
            number_transations = 0  
            number_of_withdraw = 0  
            date_save = date_d

        if  number_transations >= 10:
            print("Number of transitions exceded!")
            return False
        
        elif number_of_withdraw > self.withdraw_limit :
            print("Daily limit exceded, come back tomorrow...")
            return False

        elif value > balance:
            print("Insuficient Balance...")
            return False
            
        elif value > 500:
            print("Withdraw out of limit...")
            return False
        
        else:
            self._balance -= value
            number_of_withdraw += 1
            number_transations += 1
            date_transation = datetime.now().strftime("%d/%m/%Y %H:%M")
            extract = f"{date_transation}  "  f"{extract}" + str(f"\n- R${value} ")
                          
            print("Success!")
            return super().withdraw(value), extract
        

    def deposit(self, value): 
        
            
        global date_save
        date_d = datetime.now().date

            
        if date_d != date_save:
            number_transations = 0  
            date_save = date_d

        if number_transations >= 10:
                print("Number of transitions exceded!")
                return False
                
        if value > 0: 
            self._balance += value
            number_transations += 1
            date_save = datetime.now().date()
            date_transation = datetime.now().strftime("%d/%m/%Y %H:%M")
            extract = f"{date_transation}  " f"{extract}" + str(f"\n+ R${value} ")
            print("Success!")
            return super().deposit(value), extract
                    

        else:
            print("Invalid value, deposit should must be bigger than 0, backing to menu...")     
            return False


class Client:
    def __init__(self, address):

        self.address = address
        self.accounts = []
        
    def make_transation(self, account, transation):
        transation.register(account)
        

    def add_account(self, account):
        self.accounts.append(account)
        

class FisicPerson(Client):
    def __init__(self, name, birthday, cpf, address):

        super().__init__(address)
        self.name = name
        self.birthday = birthday
        self.cpf = cpf


class History:
    def __init__(self):
        self._transations = [] 


    @property
    def transations(self):
        return self._transations
    

    def add_transations(self, transation):
        self._transations.append(

        {    
        "Type": transation.__class__.__name__,
        "Value": transation.value,
        "Date": datetime.now().strftime("%d/%m/%Y %H:%M:%s"),
        }
    )


class Transation(ABC):

    @property

    @abstractmethod

    def value(self):
        pass

    @abstractmethod

    def register(self, account):
        pass


class Withdraw(Transation):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self.value
    
    def register(self, account):
        transation_success = account.withdraw(self.value)

        if transation_success:
            account.history.add_transation(self)


class Deposit(Transation):

    @property
    def value(self):
        return self.value
    
    def register(self, account):
        transation_success = account.deposit(self.value)

        if transation_success:
            account.history.add_transation(self)

        


def show_extract(balance,*, extract):
    print("\nEXTRACT... \n" )
    print(extract if extract else "No transactions yet.")            
    print(extract + f"\nTOTAL ACCOUNT = R${balance}")


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


   
    
    

   


    