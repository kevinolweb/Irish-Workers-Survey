# Irish Salary Survey 
![Project Preview](/assets/images/cover-image-1.png)

The application aims to collate financial information from users to help them access their financial situation. It takes various inputs from users in order to rank their financial situation effectively. It compares their average salary to the Irish national average salary for 2021. It also allows them to access this visually by providing an option for them to view average salaries by Industry.

The tool also is an effective way of gathering full time worker salary information. To find out how your average salary ranks, you must first enter your name, age and salary information. This data is stored in a Google spreadsheet which can then be used at a later point by the surveyor to compare salary by age.

The tool is deployed here [https://irish-salary-survey.herokuapp.com/]

## How it Works

* A user must enter their name
* A user must enter their age which cannot be under 18 or over 65 (pension age). 
* A user must enter their salary which cannot be below €10000 and over €100000 to allow the data to not be swayed by outliers.
* A user is then displayed how their salary compares with the national average salary for the previous year (2021).
* The user is then asked if they want to see average salary figures by Industry to provide them with added context.
* Salary information from 2021 is stored in a Google Spreadsheet which the app connects to
* The users inputs of name, age and salary is stored in the Google Spreadsheet

## Features

### Advanced Error Checking
![Age error display](/assets/images/age-error-display.png)
* The tool checks that the user cannot be under or over a certain age in order to submit their salary data. And that it is a number.
![Salary error display](/assets/images/number-error.png)
* The tool checks that the user inputted a number and the salary is between a certain reasonable range of €10,000 - €100,000.

### Salary Information Collection Storage
* The tool stores data inputted by the user such as name, age and salary in a Google Worksheet for future data interrogation.

### Salary Comparison
![Salary Comparison](/assets/images/comparison.png)
* The tool takes your salary and checks it against the cumulative average salary across all industries stored in the Google Worksheet.
* The tool tells you how much more/less you earn compared to the national average salary in the year previous.


### Display Salary Data from Worksheet
![Display Industry Salaries](/assets/images/data-display.png)
* The tool displays average salaries across all industries which is stored in a Google Spreadsheet
* The user has the option of viewing this if they want by selecting 'y' or ending the survey by selecting 'n'.

## Testing
1. I have put the code for the app through the pep8 editor and no major errors were uncovered.
2. Minor whitespacing issues and similar were discovered and will be addressed later as they do not affect code functionality.

## Deployment
* The code was deployed through Heroku and can be viewed here[[https://irish-salary-survey.herokuapp.com/].
* The Google Spreadsheet raw data is stored on a seperate private file.

## Credits 
* The Code Institute Love Sandwiches project was used to assist my learning of getting data from a spreadsheet and making calculations.

