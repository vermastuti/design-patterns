
class BankAccount:
    def __init__(self):
        self.account_number = "123456789"  # public attribute
        self._balance = 10000000 # protected attribute
        self.__pin = "1234" # private attribute
        self.__password = "securepassword"

    
    def get_balance(self):
        return self._balance
    
    def _validate_transaction(self, amount):
        return  0 < amount <= self._balance
    
    def __authenticate(self, pin, password):
        return pin == self.__pin and password == self.__password
    

class SecureBankAccount:
    def __init__(self, initial_balance=10000000):
        self.__balance = initial_balance # private attribute

        @property
        def balance(self):
            return self.__balance
        
        @balance.setter
        def balance(self, amount):
            print("Setting balance...", amount < 0)
            if amount < 0:
                raise ValueError("Balance cannot be negative")
            self.__balance = amount

    
if __name__ == "__main__":
    account = BankAccount()

    print("Account Number:", account.account_number) # Accessing public attribute
    print("Balance:", account.get_balance()) # Accessing protected attribute via public method

    # Attempting to access private attributes and methods will result in an AttributeError
    # try:
    print("Balance:", account._balance) # Accessing protected attribute directly (not recommended)
    # except AttributeError as e:
    #     print(e)

    try:
        print("PIN:", account.__pin) # Accessing private attribute directly (will raise an error)
    except AttributeError as e:
        print(e)

    print("PIN:", account._BankAccount__pin) # When you use double underscores, Python internally changes 
    # __attribute to _ClassName__attribute. This makes accidental access less likely but doesn't provide true privacy.


    # create a SecureBankAccount instance
    secure_account = SecureBankAccount()
    secure_account.balance = 20000000000  # Update balance using setter
    print("Secure Account Balance:", secure_account.balance)  # Access balance using getter

    secure_account.__balance = -5000  # This will not change the actual private variable
    print("Secure Account Balance:", secure_account.balance)  # Access balance using getter

    secure_account.balance = -5000  # Attempt to set a negative balance (will raise ValueError)
    print("Secure Account Balance:", secure_account.balance)  # Access balance using getter


class SecureAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = value

account = SecureAccount(1000)
account.__balance = -500     # AttributeError
# But still accessible via name mangling:
print("Balance:", account.balance)  # Output: 1000
account._SecureAccount__balance = -500  # Still works!
print("Balance after mangling:", account.balance)  # Output: -500
    