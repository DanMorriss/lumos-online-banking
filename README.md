# Lumos Online Banking

Lumos Online Banking is a Python based banking app where users can create an account, login, deposit & withdraw funds and delete their account. Admins have access to view all the users on the platform and delete their accounts. The programme uses an external database to store all the user information.

[Live Site](https://lumos-online-banking-698c21a030ae.herokuapp.com/)

![Responsive mockup](/assets/responsive_mockup.png)

## Contents

* [**Project**](#project)
    * [User Stories](#user-stories)
        * [First Time Visitor](#first-time-visitor)
        * [Return Visitor](#return-visitor)
    * [Site Owner Goals](#site-owner-goals)
* [**User Experience (UX)**](#user-experience-ux)
    * [Site Structure](#site-structure)
    * [Flowchart](#flowchart)
    * [Data Model](#data-model)
    * [Design Choices](#design-choices)
        * [Logo](#logo)
        * [Color Scheme](#color-scheme)
        * [Tables](#tables)
        * [Slow Typing](#slow-typing)
* [**Features**](#features)
    * [Existing Features](<#existing-features>)
        * [Login](<#login>)
        * [Create Account](<#create-account>)
        * [Account Home](<#account-home>)
        * [Check Account Balance](<#Check-Account-Balance>)
        * [Deposit Funds](<#Deposit-Funds>)
        * [Withdraw Funds](<#Withdraw-Funds>)
        * [View PIN](<#View-PIN>)
        * [Logout](<#Logout>)
        * [Delete Account](<#delete-account>)
        * [Admin Panel](<#admin-panel>)
        * [Admin: View all users](<#admin-view-all-users>)
        * [Admin: Delete a User](<#admin-delete-a-user>)
    * [Future Features](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Libraries](<#libraries>)
    * [Resources](<#resources>)
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
    * [Content](<#content>)
    * [Technical](<#technical>)
* [**Acknowledgements**](<#acknowledgements>)

## Project

### User Stories

#### First Time Visitor

A user visiting the site for the first time will want to:
- Create an account
- View their PIN
- Deposit some funds
- Logout

#### Return Visitor

A returning visitor will want to:
- Login to their account
- View their balance
- Withdraw or deposit funds
- Close their account

### Site Owner Goals

As a site owner you may want to:
- Have access to an admin pannel
- View all the users and their details in the database
- Delete a user

[Back to top](<#contents>)

## User Experience (UX)

### Site Structure

The site starts with a welcome page giving you the option to:
- Login
- Create an account

After logging in you are taken to account home where you have the options:
- Check Account Balance
- Deposit Funds
- Withdraw Funds
- View PIN
- Delete Account
- Logout

If an admin logsin they are taken to the admin panel with the options:
- View all users
- Delete a user
- Logout

### Flowchart

![Flow Chart](/assets/lumos_flowchat.png)

### Data Model

Google sheets was used to store and access user data. 
There are separate sheets for:
- The customer list
- Each individual users balance

The customer list sheet contains:
- Username
- PIN

The balance sheets contain columns for:
- Deposit
- Withdraw
- Balance

[Back to top](<#contents>)

### Design Choices

Within the confines of the terminal a few modifications have been made to improve the UX.

#### Logo

The banks logo is displayed at the top of each page. The pyfiglet library was used for this.

![Logo](assets/lumos-logo.png)

#### Color Scheme

The colorama library was used to change the text color in the terminal.
The following colors were used to help the users understand the data and site structure.
- Green: Main site color
- Red: Error messages
- White: User input
- Blue: Account information

![colors](assets/lumos-colors.png)

#### Tables

The Tabulate was used to display data in tables. Data is displayed in tables for easier understanding by the user. The following data is displayed in tables:
- Username & PIN
- Account Balance
- All users

![Table example](assets/lumos-table.png)

#### Slow Typing

The sleep library was used to delay the speed of displaying some text. This was to allow the user time to process the information. There are two uses of this:
- Delay before displaying a while line of text or information.
- A staggered 'typing' effect when the text is displayed at reading speed.

[Back to top](<#contents>)

## Features
### Existing Features

Upon starting the programme the banks logo is displayed and the user is given the option to:
1. Login
2. Create an account

![Welcome screen](assets/lumos-welcome.png)

#### Login

When the user selects 'login' they are asked for their username.
They will be show an appropriate error message if their entry:
- contains any whitespace
- is below 5 characters long
- is longer than 15 characters
- not in the database.

If their username is in the database they will be prompted to enter their PIN. They will be shown an appropriate error message if their PIN:
- is not 4 numeric characters.

If their PIN matches the one associated with their account in the databse they are sent to their account homepage.

They can exit the programme at any time by entering '0' or create an account by entering '2'.

![Login page](assets/lumos-incorrect-login.png)

#### Create Account

To create an account the user is asked for a username. They are shown an appropriate error message if their username:
- contains any whitespace
- is below 5 characters long
- is longer than 15 characters
- is already in the database, belonging to another user.

If their username is valid: 
- a 4 digit random PIN is generated and displayed to the user
- their username and PIN is added to the customers sheet in the database
- a worksheet titled with their username ia created and populate with 3 columns:
    - Deposit
    - Withdraw
    - Balance

![Create account](assets/lumos-create-account.png)

#### Account Home

When a user logs in they are taken to the account home with the options to:
- 0: Logout
- 1: Check Account Balance
- 2: Deposit Funds
- 3: Withdraw Funds
- 4: View PIN
- 5: Delete Account

![Account home](assets/lumos-account-home.png)

#### Check Account Balance

A user can check their account balance and will be shown a table containing all past transactions. Then below the table a final account balance is displayed. To return to the account home the user has to press the return key.

![View account balance](assets/lumon-balance2.png)

#### Deposit Funds

A user can choose to deposit funds into their account. They will be prompted for the amount and that will be added to the database. The user is then shown a confirmation message and sent back to the account home.
The user input is validated and an appropriate error message will be shown if:
- The amount entered is not numeric
- The amount entered is a negative number.

If the user enters a float with more than 2 decimal places, it is rounded to 2 before being added to the database.

![Deposit funds](assets/lumos-deposit-funds.png)

#### Withdraw Funds

The user can withdraw funds from their account. They are shown their current balance and then asked how much they would like to withdraw. The user input is validated and an appropriate message is displayed if:
- The amount entered is not numeric
- The amount entered is a negative number
- The amount entered exceeds the current balance of that customer's account.

If the user enters a float with more than 2 decimal places, it is rounded to 2 before being added to the database.

![Withdraw funds](assets/lumos-withdraw-funds.png)

#### View PIN

As the user needs their PIN to login and delete their account and they may not have noted it down upon creating their account, they can view it from the account home.

![view pin](assets/lumos-view-pin.png)

#### Logout

To keep the users account safe, they can logout which will clear the terminal and send them back to the login page.

#### Delete Account

A user can delete their account, but as this cannot be undone they need to confirm be clicking 'y' and entering their PIN. Once they have done both those things, all the user information is deleted from the database. Both valid responses to this are valid for both capital letters and lower case.

![delete account](assets/lumos-delete-account.png)

#### Admin Pannel

There is an admin account that can view all the current users and delete user accounts. This is accessible from the login page by entering 'ADMIN' as the username and 'password' as the PIN. From the admin panel there are two options other than logout. - View all users.
- Delete a user.

![admin panel](assets/lumos-admin.png)

##### Admin: View all users

The admin has the option to view all the users in the database. The data is displayed in a table with:

- Username
- PIN
- Balance

![view all users](assets/lumos-all-users.png)

##### Admin: Delete a user

To delete a the admin is asked for the username of the user they wish to delete then asked to conform they want to delete the account.
If that is confiremd all the user information is removed from the database.

![Admin delete a user](assets/lumos-admin-delete-user.png)

[Back to top](<#contents>)

### Future Features

- Transfer funds to another user.
- Show only the 10 most recent transactions on account balance.
- Allow users to change PIN.

[Back to top](<#contents>)

## Technologies Used

### Languages

- Python was used for the functunality of the programme.

### Libraries

- [gspread](https://docs.gspread.org/en/v3.7.0/api.html) to link up the Google Sheet.
- [credentials](https://pypi.org/project/credentials/) to link the Google Sheet.
- [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) for the logo.
- [time](https://www.programiz.com/python-programming/time/sleep) for the sleep fuction.
- [colorama](https://pypi.org/project/colorama/) to color the text in the terminal.
- [os](https://www.geeksforgeeks.org/clear-screen-python/) to clear the terminal.
- [random](https://docs.python.org/3/library/random.html) to generate a 4 digit random PIN.
- [Tabulate](https://pypi.org/project/tabulate/) to put data in a table.

### Resources

- [Lucidchart](<https://www.lucidchart.com/pages/>) for the flowchart.
- [Github](<https://github.com/>) to store the code.
- [Heroku](<https://heroku.com/>)
- [VS Code](<https://code.visualstudio.com/>) to write the code.
- [Am I Responsive?](<https://ui.dev/amiresponsive>) for the display image across devices.
- [Stack Overflow](<https://stackoverflow.com/>) for general troubleshooting.
- [W3 Schools](<https://www.w3schools.com/>) for general troubleshooting.
- [MDN Web Docs](<https://developer.mozilla.org/en-US/>) for general troubleshooting.
- [Google Sheets](<https://www.google.co.uk/sheets/about/>) for the spreadsheet used to store the customer data.

[Back to top](<#contents>)

## Testing

### Bugs

#### Solved Bugs

- In the welcome function the while loop was not ending after a user had selected a valid option. I needed to add a break statement and call the next function.
- In the create_account function an infinite loop was created due to the user input being before the loop.
- I needed to return the pin after it was being crreated for it to be sent to the databse.
- Can create multiple usernames of the same value. Created an if statement inside the create_account function to disallow this.
- If incorrect username was entered in login, on the second attempt it responds 'Incorrect PIN'. Removed unnecessary code after function that was causing part of the function to run again.
- Whitespace can be used in username. Added in an extra elif statement to the create_account function.
- Gspread was showing a error message when I tried to push data to a new spreadsheet inside the generate_worksheet function, fixed it by using append.rows instead of append.row.
- The loop in account_home as not ending to I added break to end it when user selects 0. I needed to add a break to the loop in account_home as it was still running from the first time so needed to be closed twice.
- After creating an account and login in, the user has to press any selection twice. To fix this I ran the account_home function instead of the login function.
- Deposit function won’t exit on 0, ‘currency’ was referenced before being defined. The type function containing the currency variable was moved into the try statement.
- Deposit not working currency referenced before assignment. Moved the turn_to_currrency function before the type statement.
- Could enter a negative ammount to deposit. Added in an if statement disallowing it.
- A user could create an account using numbers so I added an elif statement to check the first letter is not a number.
- If you create an account you cannot delete it without logging out and then login back in. To fix this I made the user login after creating an account.
- Once the user selected 'create an account' they had to complete it, I allowed them to press 1 at any point and go to the login page.


#### Unsolved Bugs

No known bugs.

[Back to top](<#contents>)

### Validator Testing

- PEP8
    - A single error was found bythe [PEP8](https://pep8ci.herokuapp.com/)
![Python Validation](<assets/python-validation.png>) validator, but it was for a line of code being too long. As this won't affect the terminal view I decided to leave it to make the code easier to understand.
    

### Peer Testing

As well as testing myself, the application was tested by the following external users for bugs and usability.

- Kent Yates
- Selina Sheerin
- Luke Newman

All testers passed all tests successfully without any issues or bugs found during testing! 
The folloiwng tests were carried out.

| Function                    | Test                                           | Result |
|-----------------------------|------------------------------------------------|--------|
| Welcome                     | Enter incorrect value                          | Given error message and chance to try again. |
|                             | Enter '1'                                      | User is prompted to enter their username |
|                             | Enter '2'                                      | The user is asked to select a username |
| Login: enter username       | Enter invalid username or PIN                  | 'Username or PIN incorrect' printed to the terminal and the user is sent back to the welcome screen. |
|                             | Enter invalid username and PIN                 | 'Username or PIN incorrect' printed to the terminal and the user is sent back to the welcome screen. |
|                             | Enter valid username and  incorrect PIN        | 'Username or PIN incorrect' printed to the terminal and the user is sent back to the welcome screen. |
|                             | Enter valid username and correct PIN           | 'Loading account...' is printed to the terminal and the user is taken to the account home screen. |
| Account Home                | Enter an invalid selection                     | 'Not a valid selection" printed to the terminal and the option to try again. |
|                             | Enter '1'                                      | The user is taken to account balance screen. |
|                             | Enter '2'                                      | The user is take  to the Deposit Funds screen. |
|                             | Enter '3'                                      | The user is taken to the Withdraw Funds screen |
|                             | Enter '4'                                      | The user is shown their username and PIN |
|                             | Enter '0'                                      | The user is 'logged out' and the terminal window is cleared. |
| Create Account              | Enter a username below 5 chracters             | '{username} is not valid. Select a username between 5 & 15 characters." is displayed to the terminal and the user can try again. |
|                             | Enter a username over 15 characters            | '{username} is not valid. Select a username between 5 & 15 characters." is displayed to the terminal and the user can try again. |
|                             | Enter username containing whitespace           | '{username} is not valid, contains whitespace." is displayed to the terminal and the user can try again. |
|                             | Enter a username beginning with a non letter   | '{username} is not valid. First character must be a letter.' Is displayed and the user is given another chance to enter a username. |
|                             | Enter '1'                                      | The user is asked for the username to login and the login function is run. |
|                             | A valid username is entered                    | The users username and PIN is displayed, then they are taken to the login screen once they press enter. |
| Check Account Balance       | Type any character followed by return          | Takes you to Account Home|
| Deposit Funds               | Enter a non number                             | '{deposit} is not a valid amount' is printed to the terminal and the option to try again. |
|                             | Enter a negative number                        | 'Withdraw amount cannot be negative' is printed to the terminal and the option to try again. |
|                             | Enter a number with more than 2 decimal places | The amount is rounded to 2 decimal places, added to the database and the user is taken back to Account Home. |
| Withdraw Funds              | Enter a non number                             | '{withdraw} is not a valid ammount' is printed to the terminal and the option to try again. |
|                             | Enter a negative number                        | 'Withdraw amount cannot be negative' is printed to the terminal and the option to try again. |
|                             | Enter a number higher than the account balance | 'Insufficient funds' is printed to the terminal and the user is given the option to enter a new amount. |
|                             | Enter the same amount as the balance          | The full amount is withdrawn and the user is taken back to the Account Home screen. |
|                             | Enter a number with more than 2 decimal places | The amount is rounded to 2 decimal places, withdrawn from the database and the user is taken back to the Account Home screen. |
| View PIN                    | Type anything followed by return               | The user is taken to Account Home |
| Delete account              | 'n' entered                                    | 'Going to account home...' is displayed and the account home panned is loaded.|
|                             | 'N' entered                                    | 'Going to account home...' is displayed and the account home panned is loaded.|
|                             | 'y' entered                                    | User is prompted for their PIN |
|                             | 'y' entered                                    | User is prompted for their PIN |
|                             | Anything else entered                          | 'Invalid selection. Enter Y to delete your account or N to cancel' displayed and the user is given the chance to enter a valid response. |
| Delete account PIN entry   | Incorrect pin entered                          | The user is taken back to account home. |
|                             | Correct PIN entered                            | 'Deleting account... Account successfully deleted. Logging out...' is displayed and the user is taken to the login page. |
| Admin Panel                | Type '0'                                       | 'Login out...' is displayed then the login page is loaded. |
|                             | Type '1'                 | The user data page is displayed containing a table with all the users in the database along with their PIN and balance. |
|                             | Type '2'                                       | The admin is prompted for a username. |
|                             | Type an invalid selection | 'Invalid selection. Please try again.' is displayed and the user is allowed another chance to enter a valid selection. |
| Admin view all users        | Press any key                                  | Admin panel is displayed. |
| Admin delete a user         | Enter a username not in the database           | 'User not found' displayed and the option to try again. |
|                             | Enter a username in the database                | The user is prompted to enter y/n to confirm |
|                             | '0' selected                                   |  'Login out...' is displayed then the login page is loaded. |
|                             | '1' selected                                   | The user data screen is loaded. |
| Admin confirm delete a user | 'y' entered | 'Deleting account... Account successfully deleted' is shown and the admin panel is loaded. |
|                             | 'Y' entered | 'Deleting account... Account successfully deleted' is shown and the admin panel is loaded. |
|                             | 'n' entered | 'cancelling...' is typed and the admin panel is loaded. |
|                             | 'N' entered | 'cancelling...' is typed and the admin panel is loaded. |
|                             | an invalid selection entered | 'Invalid selection' is displayed and the user is prompted to try again.|

[Back to top](<#contents>)

## Deployment
Git and GitHub were used for version control. As Python is a backend language and can't be displayed with GitHub I used Heroku for the live preview.

### Heroku Deployment
1. Login to [Heroku](https://id.heroku.com/login)
2. Click 'New' in the top right and 'Create new app'.
3. Enter a unique application name, select your region and click 'Create app'.
4. Click the 'settings' tab 
![Heroku settings tab](assets/heroku-settings.png)
5. Under 'Config Vars' click 'Reveal Config Vars'
![Heroku reveal cinfig vars](assets/heroko-reveal-config-vars.png)
6. Add the JSPN CREDS file
7. Add PORT 8000
![Add Heroku cofig vars](assets/heroko-cofig-vars.png)
8. Add 'heroku/python' and 'heroku/node.js' to the 'Buildpacks'
![Heroku buildpacks](assets/heroko-buildpacks.png)
9. Click the 'Deploy' tab.
![Heroku deploy tab](assets/heroku-deploy.png)
10. In the 'Deployment method' section select 'GitHub'
11. Search for the repo name and click 'connect'
![Herokou deployment method](assets/heroku-deployment-method.png)
12. Under 'Automatic deploys' click 'Enable Automatic Deploys'
![Heroku automatic deployment](assets/heroku-automatic-deployment.png)

### To Fork the Project
To make a copy of the GitHub Repository you can fork a copy to edit it without changing the root file. This can then be used to update the original repository. To fork take the following steps:
1. Login to GitHub
2. Go to the repository [DanMorriss/lumos-online-banking](https://github.com/DanMorriss/lumos-online-banking)
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
![Clone walkthrough image](assets/images/clone.jpg)

[Back to top](<#contents>)

## Credits

### Content

All content was created by Daniel Morriss.
The template for the readme was supplied by Code Institute with additional changes suggested by my mentor Precious Ijege from  [World of Marcus](<https://github.com/worldofmarcus/project-portfolio-3>).

### Technical

The Code Institute walkthrough project Love Sandwiches was used as insporation for the project and how to link up google sheets with Python.

## Acknowledgements

- [Precious Ijege](<https://github.com/precious-ijege>), my Code Institute Mentor.
- [Kent Yates](<https://github.com/Jelly-man>).
- [Luke Newman](<https://github.com/CrunkV5>) for testing my programme in the most creative ways.
- Selina Sheerin for moral support and usability testing.
- Stack overflow for continues trouble shooting.
- The Code Institute slack channel for inspiration on features to add.
- Chris SV via slack for testing the programme.

[Back to top](<#contents>)
