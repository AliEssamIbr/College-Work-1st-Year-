class BankAccount:
    def __init__(self,account_id,name,balance=0):
        self.account_id = account_id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print(f"\ndeposit {amount}$ succussful!")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("\ninvalid operation, you do not have enough funds in your account!")
        else:
            self.__balance = self.__balance - amount
            print(f"\nyou withdrew {amount}$ succussfully")
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance = amount
    def print_info(self):
        print(f"""\n\n        account info\n{"-"*40}\n        account ID : {self.account_id}
        account holder name : {self.name}
        account balance : {self.__balance}""")


class savings_account(BankAccount):
    def __init__(self,account_id,name,balance=0):
        super().__init__(account_id,name,balance)
    def cal_interest(self):
        balance = self.get_balance()
        interest = balance * (20/100)
        print(f"\nyour interest rate is {interest} $")
    def withdraw(self,amount):
        if amount > 2000:
            print("\ninvalid operation, you cannot withdraw more than 2000$ from your savings account!")
        else:
            withdrawl = self.get_balance()
            if amount > withdrawl:
                print("\ninvalid operation, you do not have enough funds in your account!")
            else:
                withdrawl -= amount
                self.set_balance(withdrawl)
                print(f"\nyou withdrew {amount}$ succussfully")


class checking_account(BankAccount):
    def __init__(self,account_id,name,balance=0):
        super().__init__(account_id,name,balance)
    def cal_interest(self):
        balance = self.get_balance()
        interest = balance * (5/100)
        print(f"\nyour interest rate is {interest} $")
    def withdraw(self,amount):
        if amount > 1000:
            print("\ninvalid operation, you cannot withdraw more than 1000$ from your checking account!")
        else:
            withdrawl = self.get_balance()
            if amount > withdrawl:
                print("\ninvalid operation, you do not have enough funds in your account!")
            else:
                withdrawl -= amount
                self.set_balance(withdrawl)
                print(f"\nyou withdrew {amount}$ succussfully")



class account_list:
    def __init__(self):
        self.list_of_accounts = []
    def add_account(self,account_type,account_id,account_holder_name):
        temp_list = []
        temp_list.append(account_type)
        temp_list.append(account_id)
        temp_list.append(account_holder_name)
        self.list_of_accounts.append(temp_list)
    def print_list(self):
        print("\n\n")
        for i in self.list_of_accounts:
            print("="*30)
            print(f"Account Type : {i[0]}\nAccount ID : {i[1]}\nAccount Holder Name : {i[2]}")
        print("\n\n")



s = account_list()
ali = checking_account(123,"ali",400)
s.add_account("checking account",123,"ali")
ali.print_info()
ali.deposit(40)
ali.withdraw(300000000)
ali.withdraw(30)
ali.cal_interest()
ali.print_info()
print("\n","-"*60,sep="")
ahmed = savings_account(321,"ahmed",400)
s.add_account("savings account",321,"ahmed")
ahmed.print_info()
ahmed.deposit(40)
ahmed.withdraw(10000)
ahmed.withdraw(400)
ahmed.cal_interest()
ahmed.print_info()
s.print_list()