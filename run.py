
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
    
def welcome():
    """
    The welcome sequence asking if you would like to login or create an account.
    """
    LOGO = pyfiglet.figlet_format('Lumos Online Banking')
    print(Fore.GREEN + LOGO)
    sleep(0.5)
    type('Welcome to Lumos Online Banking')
    type('Would you like to login or create an account?')
    print('1: Login')
    print('2: Create an account')
    while True:
        existing_account = input('')
        if (existing_account == "1"):
            type("Loading Login Page...")
            sleep(1)
            login()
            break
        elif (existing_account == "2"):
            type('Loading Account Setup...')
            sleep(1)
            create_account()
            break
        else:
            print('Please enter 1 to Login or 2 to create an account')
class User:
        def __init__(self, username, pin):
            self.username = username
            self.pin = pin
            
def login():
    """
    Checks database for username and validates the users PIN
    """
    customers_worksheet = SHEET.worksheet('customers')
    
    type('Please enter your username to login')
    submitted_username = input('')
    # Check if eneter username is in database
    stored_username = customers_worksheet.find(submitted_username, in_column=1)
    
    # Check PIN if username in database or ask for valid username
    if stored_username:
        # Get PIN associated with username
        stored_pin = customers_worksheet.cell(stored_username.row, stored_username.col + 1).value
        # Create user object to store username and pin
        user = User(submitted_username, stored_pin)
        type(f'Welcome {user.username}')
        # Check PIN
        pin_matched = False
        while not pin_matched:
            submitted_pin = input('Please enter your PIN: ')
            if (submitted_pin == user.pin):
                pin_matched = True
                type('PIN correct, loading account details...')
            else:
                type('Incorrect PIN, please try again')
    else:
        type('User not found, pleasse try again.')  
    
    while True:
        user_entered_pin = input('')
        database_pin = SHEET.worksheet('customers')
        if user_entered_pin == database_pin:
            type('Correct PIN, loading account details.')
            return
        elif (user_entered_pin == 0):
            return False
        else:
            type('Incorrect PIN, please try again')
    
def create_account():
    """
    Create an account with a user generate username between 5 and 15 characters long,
    A randomly generated 4 digit PIN and add the information to the database.
    """
    print('Please select a username between 5 and 15 characters long.')
    customer_database = SHEET.worksheet('customers')
    while True:
        username = input('')
        if (len(username) < 16) and (len(username) > 4):
            print('Username valid')
            type('Creating account...')
            pin = generate_pin()
            created_user = User(username, pin)
            user_information = [created_user.username, created_user.pin]
            customer_database.append_row(user_information)
            print('Account created.')
            print(f'Your PIN is: {created_user.pin}')
            # Run login function
            login()
        else:
            print('Invalid username. Please select a username between 5 and 10 characters long.')

def generate_pin():
    pin = random.randint(1000,9999)
    return pin

def main():
    clear()
    welcome()
    
main()
