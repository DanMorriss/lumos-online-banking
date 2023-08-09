
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
CUSTOMERS = SHEET.worksheet('customers')


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

# Create functions for reused print statements
def invalid_amount():
    print(Fore.GREEN + 'Please select another amount')

def invalid_selection():
    print(Fore.RED + 'Invalid selection')

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
        if existing_account == "1":
            sleep(0.2)
            login()
            break
        elif existing_account == "2":
            sleep(0.2)
            create_account()
            break
        else:
            invalid_selection()
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

    # Find username (returns None if not in database)
    stored_un = CUSTOMERS.find(submitted_un, in_column=1)

    # If username correct
    if stored_un:
        # Find PIN in databse
        stored_pin = CUSTOMERS.cell(stored_un.row, stored_un.col + 1).value
        if submitted_un == 'ADMIN' and stored_pin == submitted_pin:
            type(Fore.GREEN + 'Loading account...')
            sleep(1)
            admin_login(submitted_un, submitted_pin)
        elif stored_pin == submitted_pin:
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
    account_loop = True
    while account_loop:
        username = input(Fore.WHITE + '>')

        # Allow user to login
        if username == '1':
            login()
            return

        # Don't allow repeat usernames
        if CUSTOMERS.find(username, in_column=1) is not None:
            print(Fore.RED + 'Username unavalible, try again.')
        # Check for whitespace
        elif any(char.isspace() for char in username):
            print(Fore.RED + f'{username} not valid, containes whitespace.')
        # Make sure first character is a letter
        elif not username[0].isalpha():
            print(Fore.RED + f'{username} is not valid.')
            print(Fore.GREEN + 'First character must be a letter.')
        # Make username between 5 and 15 characters
        elif len(username) < 16 and len(username) > 4:
            print(Fore.GREEN + f'{username} is a valid username')
            type('Creating account...')
            # Create a PIN
            pin = generate_pin()
            # Save user information to database
            created_user = User(username, pin)
            user_information = [created_user.username, created_user.pin]
            CUSTOMERS.append_row(user_information)
            generate_worksheet(username)
            # Tell user PIN
            print(Fore.BLUE + 'Account created.')
            print(f'Your username is: {created_user.username}')
            print(f'Your PIN is: {created_user.pin}')
            # Run login function
            account_loop = False
            print('Press enter to go to login')
            input(Fore.WHITE + '>')
            login()
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
    print('5: Delete Account')
    print('')

    selection_loop = True
    while selection_loop:
        user_selection = input(Fore.WHITE + '>')
        if user_selection == '1':
            check_account_balance(username, pin)
            break
        elif user_selection == '2':
            deposit_funds(username, pin)
            break
        elif user_selection == '3':
            withdraw_funds(username, pin)
            break
        elif user_selection == '4':
            view_pin(username, pin)
            break
        elif user_selection == '5':
            delete_account(username, pin)
            break
        elif user_selection == '0':
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

    # get last balance
    user_sheet = SHEET.worksheet(username)
    user_data = user_sheet.get_all_values()
    last_balance_info = user_data[-1]
    last_balance = turn_to_currency(last_balance_info[-1])

    print(tabulate(user_data, headers='firstrow', tablefmt='github'))
    print('')
    type(Fore.BLUE + f'Current balance: {last_balance}')
    print('')
    print(Fore.GREEN + 'Press enter to go to account home.')
    input(Fore.WHITE + '>')
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
        deposit_amount = input(Fore.WHITE + '£')

        # Give the option to exit
        if deposit_amount == '0':
            break

        # Deposit into account
        try:
            currency = turn_to_currency(deposit_amount)
            if currency < 0:
                print(Fore.RED + 'Deposit amount cannot be negative')
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
            print(Fore.RED + f'{deposit_amount} is not a valid amount.')

    account_home(username, pin)


def turn_to_currency(amount):
    """
    Turns a number into a float with 2 decimal places.
    """
    currency = round(float(amount), 2)
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
        withdraw_amount = input(Fore.WHITE + '£')

        # Give the option to exit
        if withdraw_amount == '0':
            # account_home(username, pin)
            break

        try:
            currency = turn_to_currency(withdraw_amount)
            if currency > last_balance:
                print(Fore.RED + 'Insufficent funds')
                invalid_amount()
            elif currency < 0:
                print(Fore.RED + 'Withdraw amount cannot be negative')
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
            print(Fore.RED + f'{withdraw_amount} is not a valid amount.')

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


def delete_account(username, pin):
    """
    Deletes a user account removing the user information from the database.
    """
    print_logo()
    print('Are you sure you want to delete this account?')
    print('This cannot be undone.')
    print('Y/N')

    delete_loop = True
    while delete_loop:
        user_choice = input(Fore.WHITE + '>')
        if user_choice.lower() == 'n':
            type(Fore.GREEN + 'Going to account home...')
            delete_loop = False
            account_home(username, pin)
        elif user_choice.lower() == 'y':
            pin_attempt = check_pin(pin)
            if pin_attempt:
                type(Fore.RED + 'Deleting account...')
                delete_loop = False
                # Delete users sheet from the database.
                worksheet = SHEET.worksheet(username)
                SHEET.del_worksheet(worksheet)
                # Delete the users details from the customers sheet in database
                list_values = CUSTOMERS.col_values(1)
                row_number = list_values.index(username) + 1
                CUSTOMERS.delete_rows(row_number)
                print(Fore.GREEN + 'Account succesfully deleted')
                type('Logging out...')
            else:
                account_home(username, pin)
                break
        else:
            invalid_selection()
            print(Fore.GREEN + 'Enter Y to delete your account or N to cancel')

    sleep(1)
    welcome()


def admin_delete_account(username):
    """
    Deletes a user account removing the user information from the database.
    """
    print(Fore.GREEN + 'Are you sure you want to delete this account?')
    print('This cannot be undone.')
    print('Y/N')

    delete_loop = True
    while delete_loop:
        user_choice = input(Fore.WHITE + '>')
        if user_choice.lower() == 'n':
            type(Fore.GREEN + 'Canelling...')
            sleep(1)
            delete_loop = False
            admin_login('ADMIN', 'password')
            return
        elif user_choice.lower() == 'y':
            type(Fore.RED + 'Deleting account...')
            delete_loop = False
            # Delete users sheet from the database.
            worksheet = SHEET.worksheet(username)
            SHEET.del_worksheet(worksheet)
            # Delete the users details from the customers sheet in database
            list_values = CUSTOMERS.col_values(1)
            row_number = list_values.index(username) + 1
            CUSTOMERS.delete_rows(row_number)
            print(Fore.GREEN + 'Account succesfully deleted')
            sleep(1)
            admin_login('ADMIN', 'password')
            return
        else:
            invalid_selection()
            print(Fore.GREEN + 'Enter Y to delete your account or N to cancel')

    admin_login('ADMIN', 'password')


def check_pin(pin):
    """
    Checks whether a given PIN is correct.
    """
    print(Fore.GREEN + 'Please enter you PIN')
    user_pin = input(Fore.WHITE + '>')
    if user_pin == pin:
        return True
    else:
        print(Fore.RED + 'Incorrect PIN')
        sleep(1)
        return False


def admin_login(username, pin):
    """
    Opens the admin pannel and gives choices to logout, view all users and
    delete a user.
    """
    print_logo()
    exit()
    type('Welcome Admin')
    print('')

    print('1: View all users')
    print('2: Delete a user')
    print('')

    selection_loop = True
    while selection_loop:
        admin_choice = input(Fore.WHITE + '>')
        if admin_choice == '1':
            selection_loop = False
            user_list(username, pin)
        elif admin_choice == '2':
            print(Fore.GREEN + 'To delete a user, enter the username')
            print('')
            username_input = input(Fore.WHITE + '>')
            stored_username = CUSTOMERS.find(username_input, in_column=1)
            if stored_username:
                admin_delete_account(username_input)
                selection_loop = False
            elif username_input == '0':
                type(Fore.GREEN + 'Logging out...')
                sleep(1)
                welcome()
                break
            else:
                print(Fore.RED + 'User not found')
        elif admin_choice == '0':
            type(Fore.GREEN + 'Logging out...')
            sleep(1)
            welcome()
            break
        else:
            print(Fore.RED + 'Invalid selection.')
            print(Fore.GREEN + 'Please try again')


def user_list(username, pin):
    """
    Give Admin a list of all the users, their PIN and balance.
    """
    print_logo()
    type('Fetching user data...')
    print(Fore.BLUE + '')

    # Create list of uses and pins
    customer_database = SHEET.worksheet('customers')
    user_and_pin = customer_database.get_all_values()
    username_pin = user_and_pin[2:]
    # Create list for all details to go into
    all_users_details = []
    # Loop through list to get balance and add it to full_user_details
    for user in username_pin:
        user_pin_balance = user
        # Get the balance for the user
        user_sheet = SHEET.worksheet(user_pin_balance[0])
        user_data = user_sheet.get_all_values()
        last_balance_info = user_data[-1]
        last_balance = turn_to_currency(last_balance_info[-1])
        last_balance_display = f'£{last_balance}'
        user_pin_balance.append(last_balance_display)
        all_users_details.append(user_pin_balance)

    # Print the result in a table
    print(tabulate(all_users_details, headers=['Username', 'PIN', 'Balance'], tablefmt='github'))
    print(Fore.GREEN + '')
    print('Press enter to return to main menu')
    input(Fore.WHITE + '>')
    admin_login(username, pin)


def main():
    welcome()


main()
