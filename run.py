
# Google API's for access to the spreadsheets
import gspread
from google.oauth2.service_account import Credentials
# Pyfiglet import for the logo
import pyfiglet
# Pythons time module for the staggered text
from time import sleep
import sys
# Colorama to change the text color
from colorama import Fore
# To clear the termianal
import os
# Random number
import random
# To create tables
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('lumos_online_banking')

customers = SHEET.worksheet('customers')
data = customers.get_all_values()


def type(text):
    """
    Types out the words letter by letter
    """
    sleep(0.5)
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.05)
    print('')


def clear():
    """
    Clears the terminal
    """
    os.system('clear')


def print_logo():
    """
    Prints to banks logo in green to a blank termianl.
    """
    clear()
    LOGO = pyfiglet.figlet_format('Lumos Online Banking')
    print(Fore.GREEN + LOGO)


def exit():
    """
    Prints the exit statement at the top of each function page.
    """
    print('                                               [Enter 0 to Logout]')
    print('')


def home():
    """
    Prints the account home statement at the top of each function page.
    """
    print('                                   [Enter 0 to go to Account Home]')
    print('')

def invalid_amount():
    print(Fore.GREEN + 'Please select another amount')

def welcome():
    """
    The welcome sequence asking if you would like to login or create an account
    """
    print_logo()
    type('Welcome to Lumos Online Banking')
    print('')
    sleep(0.5)
    print('Would you like to login or create an account?')
    print('')
    print('1: Login')
    print('2: Create an account')
    print('')
    while True:
        existing_account = input(Fore.WHITE + '>')
        if (existing_account == "1"):
            sleep(0.2)
            login()
            break
        elif (existing_account == "2"):
            sleep(0.2)
            create_account()
            break
        else:
            print(Fore.RED + 'Invalid selection')
            print(Fore.GREEN + 'Enter 1 to login or 2 to create an account')


class User:
    """
    Creates a user class to store user information.
    """
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin


def login():
    """
    Validates users username and pin then either loads account home or
    sends the user back to the welcome page.
    """
    print_logo()
    print('')
    print('Please enter your username to login')
    submitted_un = input(Fore.WHITE + '>')

    print(Fore.GREEN + 'Please enter your PIN')
    submitted_pin = input(Fore.WHITE + '>')

    # Get customer details worksheet
    cust_ws = SHEET.worksheet('customers')
    # Find username (returns None if not in database)
    stored_un = cust_ws.find(submitted_un, in_column=1)

    # If username correct
    if stored_un:
        # Find PIN in databse
        stored_pin = cust_ws.cell(stored_un.row, stored_un.col + 1).value
        if stored_pin == submitted_pin:
            type(Fore.GREEN + 'Loading account...')
            sleep(1)
            account_home(submitted_un, submitted_pin)
        else:
            type(Fore.RED + 'Username or PIN incorrect')
            sleep(1)
            welcome()
    # If username incorrect
    else:
        type(Fore.RED + 'Username or PIN incorrect')
        sleep(1)
        welcome()


def create_account():
    """
    Create an account with a user generated username between 5 and 15
    characters long with no white space and
    A randomly generated 4 digit PIN and adds the information to the database.
    """
    print_logo()
    print('                                              [Enter 1 to login]')
    print('')
    print(Fore.GREEN + 'To create an account, please select a username')
    print('between 5 and 15 characters long.')
    print('')
    customer_database = SHEET.worksheet('customers')
    account_loop = True
    while account_loop:
        username = input(Fore.WHITE + '>')

        # Allow user to login
        if username == '1':
            login()
            return

        # Don't allow repeat usernames
        if customer_database.find(username, in_column=1) is not None:
            print(Fore.RED + 'Username unavalible, try again.')
        # Check for whitespace
        elif (any(char.isspace() for char in username)):
            print(Fore.RED + f'{username} not valid, containes whitespace.')
        # Make username between 5 and 15 characters
        elif (len(username) < 16) and (len(username) > 4):
            print(Fore.GREEN + f'{username} is a valid username')
            type('Creating account...')
            # Create a PIN
            pin = generate_pin()
            # Save user information to database
            created_user = User(username, pin)
            user_information = [created_user.username, created_user.pin]
            customer_database.append_row(user_information)
            generate_worksheet(username)
            # Tell user PIN
            print(Fore.BLUE + 'Account created.')
            print(f'Your username is: {created_user.username}')
            print(f'Your PIN is: {created_user.pin}')
            # Run login function
            account_loop = False

            print('Press enter to go to account home')
            input(Fore.WHITE + '>')
            account_home(created_user.username, created_user.pin)
        else:
            print(Fore.RED + f'{username} is not valid.')
            print(Fore.GREEN + 'Select a username between 5 & 10 characters.')


def generate_pin():
    """
    Create a random 4 digit PIN
    """
    pin = random.randint(1000, 9999)
    return pin


def generate_worksheet(username):
    """
    Create a new worksheet using the username and add the headings:
    Deposit, Withdraw and Balance.
    """
    new_sheet = SHEET.add_worksheet(title=username, rows=100, cols=3)
    headings = ['Deposit', 'Withdraw', 'Balance']
    starting_balance = [0, 0, 0]
    new_sheet.append_row(headings)
    new_sheet.append_row(starting_balance)


def account_home(username, pin):
    """
    Access to the accounts functions:
    Check balance, add/withdraw funds and view PIN.
    """
    print_logo()
    exit()
    type(f'Welcome {username}')
    print('Please select one of the following options:')
    print('')
    print('1: Check Account Balance')
    print('2: Deposit Funds')
    print('3: Withdraw Funds')
    print('4: View PIN')
    print('')

    selection_loop = True
    while selection_loop:
        user_selection = input(Fore.WHITE + '>')
        if (user_selection == '1'):
            check_account_balance(username, pin)
            break
        elif (user_selection == '2'):
            deposit_funds(username, pin)
            break
        elif (user_selection == '3'):
            withdraw_funds(username, pin)
            break
        elif (user_selection == '4'):
            view_pin(username, pin)
            break
        elif (user_selection == '0'):
            selection_loop = False
            type(Fore.GREEN + 'Logging out...')
            sleep(1)
            welcome()
            break
        else:
            print(Fore.RED + 'Not a valid selection')


def check_account_balance(username, pin):
    print_logo()
    type('Checking account balance...')
    print('')
    sleep(0.5)

    user_sheet = SHEET.worksheet(username)
    user_data = user_sheet.get_all_values()
    last_balance_info = user_data[-1]
    last_balance = turn_to_currency(last_balance_info[-1])

    print(tabulate(user_data, headers='firstrow', tablefmt='github'))
    print('')
    type(Fore.BLUE + f'Current balance: £{last_balance}')
    print('')
    print(Fore.GREEN + 'Press enter to go to account home.')
    user_home = input(Fore.WHITE + '>')
    account_home(username, pin)


def deposit_funds(username, pin):
    """
    Deposits money into a users account and calculates the new balance.
    """
    print_logo()

    # Get the previous balance
    user_sheet = SHEET.worksheet(username)
    user_data = user_sheet.get_all_values()
    last_balance_info = user_data[-1]
    last_balance = turn_to_currency(last_balance_info[-1])

    home()
    type('How much would you like to deposit?')

    while True:
        deposit_ammount = input(Fore.WHITE + '£')

        # Give the option to exit
        if deposit_ammount == '0':
            break

        # Deposit into account
        try:
            currency = turn_to_currency(deposit_ammount)
            if currency < 0:
                print(Fore.RED + 'Withdraw ammount cannot be negative')
                invalid_amount()
            else:

                type(Fore.GREEN + f'Depositing £{currency}')
                deposit = [currency, 0, last_balance + currency]
                user_sheet.append_row(deposit)
                type('Success, returning to account home...')
                sleep(1)
                break

        # Tell user to enetr a valid number.
        except ValueError:
            print(Fore.RED + f'{deposit_ammount} is not a valid ammount.')

    account_home(username, pin)


def turn_to_currency(ammount):
    """
    Turns a number into a float with 2 decimal places.
    """
    currency = round(float(ammount), 2)
    return currency


def withdraw_funds(username, pin):
    """
    Withdraws money from the users account and calculates the new balance.
    """
    print_logo()
    home()

    # Get the previous balance
    user_sheet = SHEET.worksheet(username)
    user_data = user_sheet.get_all_values()
    last_balance_info = user_data[-1]
    last_balance = turn_to_currency(last_balance_info[-1])

    type(Fore.BLUE + f'Your balance is £{last_balance}')
    print('')
    type(Fore.GREEN + 'How much would you like to withdraw?')
    print('')

    while True:
        withdraw_ammount = input(Fore.WHITE + '£')

        # Give the option to exit
        if withdraw_ammount == '0':
            # account_home(username, pin)
            break

        try:
            currency = turn_to_currency(withdraw_ammount)
            if currency > last_balance:
                print(Fore.RED + 'Insufficent funds')
                invalid_amount()
            elif currency < 0:
                print(Fore.RED + 'Withdraw ammount cannot be negative')
                invalid_amount()
            else:
                deposit = [0, currency, last_balance - currency]
                type(Fore.GREEN + f'Withdrawing £{currency}')
                user_sheet.append_row(deposit)
                type('Success, returning to account home...')
                sleep(1)
                break

        # Tell user to enetr a valid number.
        except ValueError:
            print(Fore.RED + f'{withdraw_ammount} is not a valid ammount.')

    account_home(username, pin)


def view_pin(username, pin):
    """
    Showes the user their PIN
    """
    print_logo()
    print(Fore.BLUE + '')
    data = [['Username', 'PIN'], [username, pin]]
    print(tabulate(data, headers='firstrow', tablefmt='github'))
    print('')
    print(Fore.GREEN + 'Press enter to go to account home')
    input(Fore.WHITE + '>')
    sleep(1)
    account_home(username, pin)


def main():
    welcome()


main()
