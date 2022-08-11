# import pytest
# from .. import calculations as cal


# print(__package__)


# print(cal.__name__)
# @pytest.fixture
# def zero_bank_account():
#     return cal.BankAccount()

# @pytest.fixture
# def default_bank_account():
#         return cal.BankAccount(50)

# @pytest.mark.parametrize("in1, in2, out", [
#     (5,5,10),
#     (2,2,4),
#     (10,1,11)
# ])
# def test_add(in1, in2, out):
#     sum = cal.add(in1, in2)
#     assert sum == out


# def test_subtract():
#     assert cal.subtract(10,5) == 5


# def test_multiply():
#     assert cal.multiply(10,2) == 20


# def test_divide():
#     assert cal.divide(10,2) == 5


# def test_bank_account(default_bank_account):
#     assert default_bank_account.balance == 50

# def test_bank_default_amount(zero_bank_account):
#     assert zero_bank_account.balance == 0
        

# def test_bank_withdraw(default_bank_account):
#     default_bank_account.withdraw(30)
#     assert default_bank_account.balance == 20

# def test_bank_deposit(default_bank_account):
#     default_bank_account.deposit(10)
#     assert default_bank_account.balance == 60


# def test_bank_interest(default_bank_account):
#     default_bank_account.collect_interest()
#     assert round(default_bank_account.balance, 6) == 55





# @pytest.mark.parametrize("dep, withd, bal", [
#     (200, 100, 100),
#     (10, 1, 9),
#     (30, 3, 27)
# ])
# def test_bank_transaction(zero_bank_account, dep, withd, bal):
#     zero_bank_account.deposit(dep)
#     zero_bank_account.withdraw(withd)
#     assert zero_bank_account.balance == bal


# def test_insufficient_funds(default_bank_account):
#     with pytest.raises(cal.InsufficientFunds):
#         default_bank_account.withdraw(100)

