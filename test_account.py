from account import *
import pytest


class Test:
    def setup_method(self):
        self.person1 = Account("Ryan")
        self.person2 = Account("Molly")

    def teardown_method(self):
        del self.person1
        del self.person2

    def test_init(self):
        # Testing default values
        assert self.person1.get_name() == "Ryan"
        assert self.person2.get_name() == "Molly"
        assert self.person1.get_balance() == pytest.approx(0)
        assert self.person2.get_balance() == pytest.approx(0)

    def test_deposit(self):
        # Testing whether deposit occurred (True = yes, False = no)
        assert self.person1.deposit(-500) is False
        assert self.person1.get_balance() == pytest.approx(0)
        assert self.person2.deposit(0) is False
        assert self.person2.get_balance() == pytest.approx(0)

        assert self.person1.deposit(100) is True
        assert self.person1.get_balance() == pytest.approx(100)
        assert self.person2.deposit(25.50) is True
        assert self.person2.get_balance() == pytest.approx(25.50)

    def test_withdraw(self):
        # Testing whether withdraw occurred (True = yes, False = no)
        assert self.person1.withdraw(-500) is False
        assert self.person1.get_balance() == pytest.approx(0)
        assert self.person2.withdraw(0) is False
        assert self.person2.get_balance() == pytest.approx(0)

        # Testing acceptable withdrawal ranges
        self.person1.deposit(100)
        assert self.person1.get_balance() == pytest.approx(100)
        assert self.person1.withdraw(100.01) is False
        assert self.person1.get_balance() == pytest.approx(100)
        assert self.person1.withdraw(-10) is False
        assert self.person1.get_balance() == pytest.approx(100)
        assert self.person1.withdraw(50) is True
        assert self.person1.get_balance() == pytest.approx(50)

        self.person2.deposit(55.25)
        assert self.person2.withdraw(0) is False
        assert self.person2.get_balance() == pytest.approx(55.25)
        assert self.person2.withdraw(55.24) is True
        assert self.person2.get_balance() == pytest.approx(0.01)

    def test_get_balance(self):
        # Testing initial balances
        assert self.person1.get_balance() == pytest.approx(0)
        assert self.person2.get_balance() == pytest.approx(0)

        # Testing balances after deposit
        self.person1.deposit(10)
        assert self.person1.get_balance() == pytest.approx(10)

        self.person2.deposit(-500)
        assert self.person2.get_balance() == pytest.approx(0)

    def test_get_name(self):
        # Testing names on initial object creation
        assert self.person1.get_name() == "Ryan"
        assert self.person2.get_name() == "Molly"
