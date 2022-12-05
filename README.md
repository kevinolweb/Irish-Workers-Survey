# Irish Salary Survey 
![Project Preview](/assets/images/cover-image-1.png)

The application aims to collate financial information from users to help them access their financial situation. It takes various inputs from users in order to rank their financial situation effectively. It compares their average salary to the Irish national average salary for 2021. It also allows them to access this visually by providing an option for them to view average salaries by Industry.

The tool also is an effective way of gathering full time worker salary information. To find out how your average salary ranks, you must first enter your name, age and salary information. This data is stored in a Google spreadsheet which can then be used at a later point by the surveyor to compare salary by age.

The tool is deployed here[https://irish-salary-survey.herokuapp.com/]

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!