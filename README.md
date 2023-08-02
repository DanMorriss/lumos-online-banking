[Live Site](https://lumos-online-banking-698c21a030ae.herokuapp.com/)


- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

# Lumos Online Banking

![Responsive mockup]()

## Contents

* [**User Experience (UX)**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
        * [First Time Visitor Goals](<#first-time-visitor-goals>)
        * [Returning Visitor Goals](<#returning-visitor-goals>)
        * [Frequent Visitor Goals](<#frequent-visitor-goals>)
    * [Wireframes](<#wireframes>)
        * [Home](<#home>)
        * [Game Screen](<#game-screen>)
        * [Difficulty](<#difficulty>)
        * [High Scores](<#high-scores>)
* [**Design**](<#design>)
    * [Color Scheme](<#color-scheme>)
    * [Typography](<#typography>)
* [**Features**](#features)
    * [Existing Features](<#existing-features>)
        * [Homepage](<#homepage>)
        * [The Rules](<#the-rules>)
        * [Enter a Username](<#enter-a-username>)
        * [Choose a Difficulty](<#choose-a-difficlty>)
        * [Answer the Questions](<#answer-the-questions>)
        * [High Scores](<#high-scores>)
        * [Sound](<#sound>)
        * [Close the game](<#close-the-game>)
    * [Accesibility](<#accesibility>)
    * [Future Features](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
* [**Testing**](<#testing>)
    * [Code Validation](<>)
        * [W3C HTML Checker](<#w3c-html-checker>)
        * [W3C CSS Checker](<#w3c-css-checker>)
        * [Lighthouse](<#lighthouse>)
    * [Responsiveness Test](<#responsiveness-test>)
    * [Browser Compatibility](<#browser-compatibility>)
    * [Peer Testing](<#peer-testing>)
* [**Bugs**](<#bugs>)
    * [Solved Bugs](<#solved-bugs>)
    * [Unsolved Bugs](<#unsolved-bugs>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [Resources](<#resources>)
    * [Content](<#content>)
    * [Media](<#media>)
* [**Acknowledgements**](<#acknowledgements>)


## Features
### Existing Features

#### Homepage

#### The Rules

#### Enter a Username

#### Choose a Difficlty

#### Answer the Questions

#### High Scores

#### Sound

#### Close the Game

[Back to top](<#contents>)
### Future Features

- Transfer funds to another user.

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

[Back to top](<#contents>)

## Deployment
Git and GitHUb were used for version control. As Python is a backend language and can't be displayed with GitHub I used Heroku for the live preview.

### To Deploy the project on Heroku
1. Login to Heroku

### To Fork the project
To make a copy of the GitHub Repository you can fork a copy to edit it without changing the root file. This can then be used to update the original repository. To fork take the following steps:
1. Login to GitHub
2. Go to the repository [DanMorriss/jazz-platform](https://github.com/DanMorriss/lumos-online-banking)
3. On the top right-hand side of the page click the `fork` button and save a copy of the original repository to your GitHub account.

### To Clone the project
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
- [Tabulate](https://pypi.org/project/tabulate/) to put data in a table.

### Code Used

[Back to top](<#contents>)

## Acknowledgements

- [Precious Ijege](<https://github.com/precious-ijege>), my Code Institute Mentor.
- [Kent Yates](<https://github.com/Jelly-man>).

[Back to top](<#contents>)