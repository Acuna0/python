class Account:
    """
    A class representing the monetary balance and name of a person for an account object.
    """
    def __init__(self, name: str) -> None:
        """
        Method to set default values for an account object.
        :param name: Persons full name as a string
        """
        self.__account_name = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to increase account balance for an account object if amount is greater than 0.
        :rtype: object
        :param amount: Amount of monetary value being deposited to persons account.
        :return: Boolean value , True if deposit successful, False if unsuccessful.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to decrease account balance (withdraw) for an account object if amount is greater than 0 and
        less than or equal to the account balance.
        :param amount: Amount of monetary value being withdrawn from persons account.
        :return: Boolean value , True if deposit successful, False if unsuccessful.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to retrieve current balance of an account object.
        :return: Current value of persons account balance as a float.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to retrieve name of an account object.
        :return: Persons full name as a string.
        """
        return self.__account_name
