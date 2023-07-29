
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

def login():
    print('Please enter your username to login')
    submitted_username = input('')
    type('Checking database...')
    sleep(1)
    type(f'Welcome {submitted_username}')
    
def create_account():
    print('Please select a username between 5 and 10 characters long.')
    customer_database = SHEET.worksheet('customers')
    
    while True:
        username = input('')
        if (len(username) < 11) and (len(username) > 4):
            print('Username valid')
            type('Creating account...')
            customer_database.append_row([username])
            type('Account created.')
            print('your PIN numbre is:')
            login()
        else:
            print('Invalid username. Please select a username between 5 and 10 characters long.')

def main():
    clear()
    welcome()
    
main()
create_account()