class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance 
        """Initialize an account with an owner name and an optional starting balance.

        Args:
            owner (str): The name of the account owner.
            balance (float): The initial balance of the account (default is 0).
        """

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount 
        return balance 

        """Deposit a positive amount into the account.

        Args:
            amount (float): The amount to deposit.
        Raises:
            ValueError: If the deposit amount is not positive.

        Returns:
            float: The new balance after the deposit.
        """


    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        self.balance = balance - amount
        return balance
        """Withdraw a positive amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the balance.

        Returns:
            float: The new balance after the withdrawal.
        """


    def get_balance(self):
        return self.balance
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
 

    def transfer(self, amount, to_accoun):
        if amount < 0 or amount > balance:
            raise ValueError
        
        self.withdraw(amount)
        to_account.deposit(amount)
        


        """Transfer a positive amount to another account.

        Args:
            amount (float): The amount to transfer.
            to_account (Account): The account to which the amount is transferred.

        Raises:
            ValueError: If the transfer amount is not positive or exceeds the balance.
        """

```

#### Exercise1: Write Unit Tests for Account (15 minutes)

**Objective:** Write basic unit tests for the `Account` class's functionalities.

1. **Create a new file** named `test_bank.py` and implement basic tests. Include docstrings in your test cases.

   ```python
   import pytest
   from bank import Account

   def test_initial_balance():
       # TODO

   def test_deposit():
       # TODO

   def test_withdraw():
       # TODO
   ```

#### Exercise 2: Add Tests for Error Handling (10 minutes)

**Objective:** Test exception handling for the `deposit` and `withdraw` methods. Feel free to google for examples on how to test for exceptions.

1. **Extend `test_bank.py`** to include tests for wrong inputs. Include docstrings in your test cases.

   ```python
   def test_deposit_negative_amount():
       # TODO

   def test_withdraw_more_than_balance():
       # TODO

   def test_withdraw_negative_amount():
       # TODO
   ```

#### Exercise 3: Using Fixtures (10 minutes)

**Objective:** Use pytest fixtures to create reusable account setups. Create a fixture to produce an account object with a specific balance and use it in other tests in `test_bank.py`.


#### Exercise 4: Parameterization (10 minutes)

**Objective:** Test the `transfer` method using parameterized tests.


#### Exercise 5: Integration Testing (10 minutes)

**Objective:** Test interactions between multiple Account objects in a more complex scenario.

1. **Extend `test_bank.py`** to add integration tests that test transfers between two different customers' accounts.
