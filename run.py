
# Google API's for access to the spreadsheets
import gspread
from google.oauth2.service_account import Credentials

# Pyfiglet import for the logo
import pyfiglet

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

logo = pyfiglet.figlet_format('Lumos Online Banking')
print(logo)