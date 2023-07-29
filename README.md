[Live Site](https://lumos-online-banking-698c21a030ae.herokuapp.com/)

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

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

#### Unsolved Bugs

No known bugs.

[Back to top](<#contents>)

### Validator Testing

- PEP8
    - No erors were returned from [PEP8online.com](https://pep8online.com)

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

### Code Used

[Back to top](<#contents>)

## Acknowledgements

- [Precious Ijege](<https://github.com/precious-ijege>), my Code Institute Mentor.
- [Kent Yates](<https://github.com/Jelly-man>).

[Back to top](<#contents>)