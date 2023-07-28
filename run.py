
# Google API's for access to the spreadsheets
import gspread
from google.oauth2.service_account import Credentials

# Pyfiglet import for the logo
import pyfiglet
# Pythons time module for the staggered text
from time import sleep
import sys

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


logo = pyfiglet.figlet_format('Lumos Online Banking')
print(logo)
sleep(0.5)
type('Welcome to Lumos Online Banking')
type('Please enter your unsername to login')