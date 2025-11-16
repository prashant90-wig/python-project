class BankAccount:

    def __init__(self, acc_holder, initial_balance = 0):
        self.acc_holder = acc_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        try:
            if amount <= 0:
                print("Deposit must be positive")
                return False
            
            self.balance += amount
            self.transactions.append(f"Deposited: Rs.{amount}")
            print(f"Deposited Rs.{amount}. New Balance: Rs.{self.balance}")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return True
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                print("Withdrawal must be positive")
                return False
            
            self.balance -= amount
            self.transactions.append(f"Withdrew: Rs.{amount}")
            print(f"Withdrew Rs.{amount}. New Balance: Rs.{self.balance}")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return True
        
    def check_balance(self):
        print(f"Account Holder: {self.acc_holder}")
        print(f"Current balance: Rs.{self.balance}")
        return self.balance
    
    def transaction_history(self):
        print(f"\n--- Transaction History for {self.acc_holder} ---")
        if not self.transactions:
            print(f"No transactions yet!")
        else:
            for t in self.transactions:
                print(t)
        print(f"Current Balance: Rs.{self.balance}\n")

def main():

    acc = BankAccount("Pranish Joshi", 1000)

    acc.check_balance()
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(5000) #should fail hahaha
    acc.deposit(-100) #should fail hahahah
    acc.transaction_history()

    #multiple accounts

    print("\n--- Testing for Multiple Accounts ---")
    acc2 = BankAccount("Prashant")
    acc2.deposit(3000)
    acc2.withdraw(200)
    acc.check_balance()

if __name__ == "__main__":
    main()


        