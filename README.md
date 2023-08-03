[Live Site](https://lumos-online-banking-698c21a030ae.herokuapp.com/)

# Lumos Online Banking

![Responsive mockup]()

## Contents

* [**Features**](#features)
    * [Existing Features](<#existing-features>)
        * [Login](<#login>)
        * [Create Account](<#create-account>)
            * [Generate PIN](<#generate-pin>)
            * [Add User to Database](<#add-user-to-database>)
        * [Check Account Balance](<#Check-Account-Balance>)
        * [Deposit Funds](<#Deposit-Funds>)
        * [Withdraw Funds](<#Withdraw-Funds>)
        * [View PIN](<#View-PIN>)
        * [Logout](<#Logout>)
    * [Future Features](<#future-features>)
* [**Data Model**](<#data-model>)
* [**Flowchart**](<#flowchart>)
* [**Testing**](<#testing>)
    * [Bugs](<#bugs>)
        * [Solved Bugs](<#solved-bugs>)
        * [Unsolved Bugs](<#unsolved-bugs>)
    * [Validator Testing](<#validator-testing>)
    * [Peer Testing](<#peer-testing>)
* [**Deployment**](<#deployment>)
    * [Heroku Deployment](<#heroku-deployment>)
    * [To Fork the Project](<#to-fork-the-project>)
    * [To Clone the Project](<#to-clone-the-project>)
* [**Credits**](<#credits>)
    * [Resources](<#resources>)
    * [Languages](<#languages>)
    * [Libraries](<#libraries>)
    * [Code Used](<#code-used>)
* [**Acknowledgements**](<#acknowledgements>)


## Features
### Existing Features

Upon starting the programme the banks logo is displayed and the user is given the option to:
1. Login
2. Create an account
0. Exit

#### Login

When the user selects 'login' they are asked for their username.
They will be show an appropiate error message if thier entry:
- contains any whitespace
- is below 5 characters long
- is longer than 15 characters
- not in the database

If their username is in the database they will be prompted to enter their PIN. They will be shown an appropiate error message if thier PIN:
- not 4 numeric characters 
If their PIN matches the one associated with their account in the databse they are sent to their account homepage.

They can exit the programme at any time by entering '0' or create an account by entering '2'.

#### Create Account

To create an account the user is asked for a username. They are shown an apporpiate error message if their username:
- contains any whitespace
- is below 5 characters long
- is longer than 15 characters
- is already in the database, belonging to another user



##### Generate PIN

##### Add User to Database

#### Check Account Balance

#### Deposit Funds

#### Withdraw Funds

#### View PIN

#### Logout

[Back to top](<#contents>)
### Future Features

- Transfer funds to another user.
- Show only the 10 most recent transactions on account balance.
- Allow users to change PIN.
- Add an admin feature to view all customers and corresponding account information, search for a user and delete a users profile.
- Allow user to delete their account.
- Don't allow usernames to begin with numbers. Must begin with a letter.

[Back to top](<#contents>)

## Data Model

- Google sheets was used to store and access user data.

## Flowchart

![Flow Chart](/assets/lumos_flowchat.png)

## Testing

### Bugs

#### Solved Bugs

- In the welcome function the while loop was not ending after a user had selected a valid option. I needed to add a break statement and calling the next function.
- In the create_account function an infinate loop was created due to the user inout being before the loop.
- I needed to return the pin after it was being crreated for it to be sent to the databse.
- Can create multiple usernames of the same value. Created an if statement inside the create_account function.
- If incorrect username eneterd in login, on second attempt it responds 'Incorect PIN'. Removed unnessisary code after function that was causing part of the function to run again.
- Whitespace can be used in username. Added in an extra elif statement to the create_account function.
- Gspread was showing a error message when I tried to push data to a new spreadsheet insid the generate_worksheet function, using append.rows fixed it.
- The loop in account_home as not ending to I added break to end it when user selects 0. I needed to add a break to the loop in account_home as it was still running from the first time so needed to be closed twice.
- After creating an account and loggin in, the user has to press any selection twice. To fix this I ran the account_home function instead of the login function.
- Deposit function won’t exit on 0, ‘currency’ was referenced before being defined. The type function containing the currency variable was moved into the try statement.
- Deposit not working currency referenced before assignment. Moved the turn_to_currrency function before the type statement.
- Could eneter a negative ammount to deposit. Added in an if statement disallowing it.


#### Unsolved Bugs

- Add in use PIN for withdraw function.
- Add option to change PIN.
- Allow cancel create accont and login with 0.

[Back to top](<#contents>)

### Validator Testing

- PEP8
    - No errors were returned from [PEP8](https://pep8ci.herokuapp.com/)
    

### Peer Testing

As well as testing myself, the application was tested by the following external users for bugs and userbility.

- Kent Yates
- Selina Sheerin
- Luke Newman

All testers passed all tests successfully without any issues or bugs found during testing! 
The folloiwng tests were carried out.

| Function              | Test                                           | Result |
|-----------------------|------------------------------------------------|--------|
| Welcome               | Enter incorrent value                          | Given error message and chance to try again. |
|                       | Enter '1'                                      | User is prompted to enter their username |
|                       | Enter '2'                                      | The user is asked to select a username |
|                       | Enter '0'                                      | 'Closing application...' is printed to the terminal then it closes. |
| Login: enter username | Enter username below 5 chracters               | 'User not found, please try again' printed to the termianl and the option to try again. |
|                       | Enter password over 15 characters              | 'User not found, please try again' printed to the termianl and the option to try again. |
|                       | Enter username containing whitespace           | 'User not found, please try again' printed to the termianl and the option to try again. |
|                       | Enter unknown username                         | 'User not found, please try again' printed to the termianl and the option to try again. |
|                       | Enter empty field                              | 'User not found, please try again' printed to the termianl and the option to try again. |
|                       | Enter '0'                                      | 'Closing application...' is printed to the terminal then it closes. |
|                       | Enter '2'                                      | Sends the user to Create Account. |
| Login: enter PIN      | Enter incorrect PIN                            | 'Incorect PIN, please try again' printed to the terminal and the option to try again. |
|                       | Enter empty field                              | 'Incorect PIN, please try again' printed to the terminal and the option to try again. |
|                       | Enter not a number                             | 'Incorect PIN, please try again' printed to the terminal and the option to try again. |
|                       | Enter corect PIN                               | Takes you to Account Home |
|                       | Enter '0'                                      | 'Closing application...' is printed to the terminal then it closes. |
| Account Home          | Enter an invalid selection                     | 'Not a valid selection" printed to the terminal and the option to try again. |
|                       | Enter '1'                                      | The user is taken to account balance screen. |
|                       | Enter '2'                                      | The user is take  to the Deposit Funds screen. |
|                       | Enter '3'                                      | The user is taken to the Withdraw Funds screen |
|                       | Enter '4'                                      | The user is shown their username and PIN |
|                       | Enter '0'                                      | The user is 'logged out' and the terminal window is cleared. |
| Create Account        | Enter a username below 5 chracters             | 'x is not valid. Select a username between 5 & 15 characters." is displayed to the terminal and the user can try again. |
|                       | Enter a username over 15 characters            | 'x is not valid. Select a username between 5 & 15 characters." is displayed to the terminal and the user can try again. |
|                       | Enter username containing whitespace           | 'x is not valid, containes whitespace." is displayed to the terminal and the user can try again. |
|                       | Enter '0'                                      | 'Closing application...' is printed to the terminal, the screen is cleared then the application closes. |
|                       | Enter '1'                                      | The user is asked for the username to login and the login function is run. |
| Check Account Balance | Type any character followed by return          | Takes you to Account Home|
| Deposit Funds         | Enter a non number                             | 'x is not a valid ammount' is printed to the terminal and the option to try again. |
|                       | Enter a negative number                        | 'Withdraw ammount cannot be negative' is printed to the terminal and the option to try again. |
|                       | Enter a number with more than 2 decimal places | The ammount is rounded to 2 decial places, added to the database and the user is taken back to Account Home. |
| Withdraw Funds        | Enter a non number                             | 'x is not a valid ammount' is printed to the terminal and the option to try again. |
|                       | Enter a negative number                        | 'Withdraw ammount cannot be negative' is printed to the terminal and the option to try again. |
|                       | Enter a number higher than the account balance | 'Insufficent funds' is printed to the terminal and the user is given the option to enter a new ammount. |
|                       | Enter the same ammount as the balance          | The full ammount is withdrawn and the user is taken back to the Account Home screen. |
|                       | Enter a number with more than 2 decimal places | The ammount is rounded to 2 decimal places, withdrawn from the databse and the user is taken back to the Account Home screen. |
| View PIN              | Type anything followed by return               | The user is taken to Account Home |

[Back to top](<#contents>)

## Deployment
Git and GitHub were used for version control. As Python is a backend language and can't be displayed with GitHub I used Heroku for the live preview.

### Heroku Deployment
1. Login to Heroku

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

### To Fork the Project
To make a copy of the GitHub Repository you can fork a copy to edit it without changing the root file. This can then be used to update the original repository. To fork take the following steps:
1. Login to GitHub
2. Go to the repository [DanMorriss/jazz-platform](https://github.com/DanMorriss/lumos-online-banking)
3. On the top right-hand side of the page click the `fork` button and save a copy of the original repository to your GitHub account.

### To Clone the Project
To clone the project on GitHub:
1. Click the `code` button  
2. Click the `local` tab
3. Under HTTPS click the clipboard icon to copy the URL
4. In your IDE of choice, open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type `git clone` and then paste the URL copied from GitHub
7. Press enter and the local clone will be created
![Clone walkthrough image](assets/images/clone.png)

[Back to top](<#contents>)

## Credits

### Resources

- [Lucidchart](<https://www.lucidchart.com/pages/>) for the flowchart.
- [Github](<https://github.com/>) to store the code.
- [Heroku](<https://heroku.com/>)
- [VS Code](<https://code.visualstudio.com/>) to write the code.
- [Am I Responsive?](<https://ui.dev/amiresponsive>) for the dislay image across devices.
- [Stack Overflow](<https://stackoverflow.com/>) for general troubleshooting.
- [W3 Schools](<https://www.w3schools.com/>) for general troubleshooting.
- [MDN Web Docs](<https://developer.mozilla.org/en-US/>) for general troubleshooting.
- [Google Sheets](<https://www.google.co.uk/sheets/about/>) for the spreadsheet used to store the customer data.

### Languages

- Python

### Libraries

- [gspread](https://docs.gspread.org/en/v3.7.0/api.html) to link up the Google Sheet.
- [credentials](https://pypi.org/project/credentials/) to link the Google Sheet.
- [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) for the logo.
- [time](https://www.programiz.com/python-programming/time/sleep) for the sleep fuction.
- [colorama](https://pypi.org/project/colorama/) to color the text in the terminal.
- [os](https://www.geeksforgeeks.org/clear-screen-python/) to clear the terminal.
- [random](https://docs.python.org/3/library/random.html) to generate a 4 digit random PIN.
- [Tabulate](https://pypi.org/project/tabulate/) to put data in a table.

### Code Used

[Back to top](<#contents>)

## Acknowledgements

- [Precious Ijege](<https://github.com/precious-ijege>), my Code Institute Mentor.
- [Kent Yates](<https://github.com/Jelly-man>).
- Luke Newman for testing my programme in the most creative ways.
- Selina Sheerin for moral support and userbility testing.

[Back to top](<#contents>)