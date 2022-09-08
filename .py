account_name = ''
account_balance = 0
account_password = ''


def new_account(name, password, balance):
    global account_password, account_balance, account_name
    account_password = password
    account_name = name
    account_balance = balance


def show():
    global account_password, account_balance, account_name
    print(f'Account name {account_name}\nAccount balance {account_balance}\n'
          f'Account Password {account_password}')


def get_balance(password):
    global account_password, account_balance, account_name
    if password == account_password:
        return account_balance
        # print(f'Account balance is {account_balance}')
    else:
        print('Wrong password')
        return None


def deposit(deposit_amount, password):
    global account_password, account_balance, account_name
    if deposit_amount <= 0:
        print('You cannot deposit negative or zero amount!')
        return None
    if password != account_password:
        print('Wrong Password')
        return None
    account_balance += deposit_amount
    return account_balance


def withdraw(withdraw_amount, password):
    global account_password, account_balance, account_name

    if withdraw_amount < 0:
        print('You cannot withdraw Negative or Zero amount')
        return None
    elif withdraw_amount > account_balance:
        print("you cannot withdraw more than your account balance")
        return None
    if password != account_password:
        print("Wrong Passowrd")
        return None
    account_balance -= withdraw_amount
    return account_balance


new_account('Joe', 'soup', 100)

while True:
    print()
    print('Press "b" to get the balance. Press "d" to make a deposit\nPress "w" to make a '
          'withdrawal. Press "s" to show the account\nPress "q" to quit\n')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        user_password = input('Please enter the password: ')
        theBalance = get_balance(user_password)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ')
        new_balance = deposit(user_deposit_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 'w':
        print('Withdraw')
        user_withdraw_amount = int(input('Please enter amount to withdraw: '))
        user_password = input('Please enter the password: ')
        new_balance = withdraw(user_withdraw_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 's':
        print('Show Details')
        user_password = input('Please enter the password: ')
        if user_password == account_password:
            show()
        else:
            print('Wrong password')

    elif action == 'q':
        break

    else:
        print('Wrong Input')
    print()
    print('Done')
