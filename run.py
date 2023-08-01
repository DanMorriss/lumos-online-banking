
# Google API's for access to the spreadsheets
import gspread
from google.oauth2.service_account import Credentials
# Pyfiglet import for the logo
import pyfiglet
# Pythons time module for the staggered text
from time import sleep
import sys
# Colorama to change the text color
from colorama import Fore, Back
# To clear the termianal
import os
# Random number
import random
# To test if something is a number
from math import isnan
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


def welcome():
    """
    The welcome sequence asking if you would like to login or create an account
    """
    # Display logo
    print_logo()
    # Welcome message
    type('Welcome to Lumos Online Banking')
    type('Would you like to login or create an account?')
    print('1: Login')
    print('2: Create an account')
    while True:
        existing_account = input(Fore.WHITE + '')
        if (existing_account == "1"):
            sleep(0.2)
            login()
            break
        elif (existing_account == "2"):
            sleep(0.2)
            create_account()
            break
        else:
            print('Please enter 1 to Login or 2 to create an account')


class User:
    """
    Creates a user class to store user information.
    """
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin


def login():
    """
    Checks database for username and validates the users PIN
    """
    cust_ws = SHEET.worksheet('customers')

    login_loop = True
    while login_loop:
        type(Fore.GREEN + 'Please enter your username to login')
        submitted_username = input(Fore.WHITE + '')
        # Check if username is in database
        stored_un = cust_ws.find(submitted_username, in_column=1)

        # Check PIN if username in database or ask for valid username
        if stored_un:
            # Get PIN associated with username
            stored_pin = cust_ws.cell(stored_un.row, stored_un.col + 1).value
            # Create user object to store username and pin
            user = User(submitted_username, stored_pin)
            type(Fore.GREEN + f'Welcome {user.username}')
            # Check PIN
            pin_matched = False
            while not pin_matched:
                print('Please enter your PIN: ')
                submitted_pin = input(Fore.WHITE + '')
                if (submitted_pin == user.pin):
                    pin_matched = True
                    type(Fore.GREEN + 'PIN correct, loading account details..')
                    sleep(1)
                    login_loop = False
                    account_home(user.username, user.pin)
                else:
                    print(Fore.GREEN + 'Incorrect PIN, please try again')
        else:
            print(Fore.GREEN + 'User not found, please try again.')


def create_account():
    """
    Create an account with a user generated username between 5 and 15
    characters long with no white space and
    A randomly generated 4 digit PIN and adds the information to the database.
    """
    print(Fore.GREEN + 'Select a username between 5 and 15 characters long.')
    customer_database = SHEET.worksheet('customers')
    account_loop = True
    while account_loop:
        username = input(Fore.WHITE + '')
        # Don't allow repeat usernames
        if customer_database.find(username, in_column=1) is not None:
            print(Fore.GREEN + 'Username unavalible, try again.')
        # Check for whitespace
        elif (any(char.isspace() for char in username)):
            print(Fore.GREEN + f'{username} not valid, containes whitespace.')
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
            login()
        else:
            print(Fore.GREEN + f'{username} is not valid.')
            print('Select a username between 5 and 10 characters long.')


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
    type(f'Welcome {username}')
    print('Please select one of the following options:')
    print('')
    print('1: Check Account Balance')
    print('2: Deposit Funds')
    print('3: Withdraw Funds')
    print('4: View PIN')
    print('')
    print('0: Exit')


    selection_loop = True
    while selection_loop:
        user_selection = input(Fore.WHITE + '')
        if (user_selection == '1'):
            check_account_balance(username, pin)
            break
        elif (user_selection == '2'):
            deposit_funds(username, pin)
            break
        elif (user_selection == '3'):
            print('withdraw funds')
            break
        elif (user_selection == '4'):
            print('View PIN')
            break
        elif (user_selection == '0'):
            selection_loop = False
            break
        else:
            print('Not a valid selection')


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
    print(Fore.GREEN + '')
    print('press 0 to go back to account home')
    user_home = input(Fore.WHITE + '')
    if (user_home == '0'):
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

    type('How much would you like to deposit?')
    print('Enter 0 to exit')

    while True:
        deposit_ammount = input(Fore.WHITE + '£')
        
        # Give the option to exit
        if deposit_ammount == '0':
            # account_home(username, pin)
            break

        # Deposit into account
        try:
            currency = turn_to_currency(deposit_ammount)
            deposit = [currency, 0, last_balance + currency]
            user_sheet.append_row(deposit)
            break

        # Tell user to enetr a valid number.
        except ValueError:
            print(f'{deposit_ammount} is not a valid ammount, please try again.')
            print('Or enter 0 to exit')

    type(Fore.GREEN + f'Depositing £{currency}')
    sleep(1.5)
    account_home(username, pin)


def turn_to_currency(ammount):
    """
    Turns a number into a float with 2 decimal places.
    """
    currency = round(float(ammount), 2)
    return currency

def main():
    welcome()


main()