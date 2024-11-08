import python
from bank import Account
#testing the functions and not the active user input

def test_initial_balance():
    account1 = Account("Inna")
    assert account1.get_balance == 0

def test_deposit():
   a2 = Account("Inna")
   a2.deposit(15)
   assert a2.amount == 0

def test_withdarw():
    a3 = Account("Inna")
    a3.withdarw(15)
    assert a3.amount == 15 

#testing exeption handling for the deposit and withdraw methods

def test_negative_amount():

def test_withdraw_more_than_balance():

def test_withdraw_negative_amount():

