import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Salary_Survey')

last_years_data = SHEET.worksheet('2021')

data = last_years_data.get_all_values()


def get_survey_data():
    """
    This function gets survey inputs from user
    """
    list_data=[]
    print("Hello, this is a survey of full time workers in Ireland. \n We ask that you answer all questions truthfully.")
    input_name=input("Please enter your name press Enter E.g John\n")
    list_data.append(input_name)
    while True:
        input_age=input("Please enter your age press Enter E.g 21\n")
        if validate_data(input_age):
            list_data.append(input_age)
            break
    while True:
        input_salary=input("Please enter your salary and press Enter E.g 31000\n")
        if validate_salary(input_salary):
            list_data.append(input_salary)
            break
    summary_table(input_name,input_salary)
    return list_data

def validate_data(input_age):
    try:
        if input_age.isdigit():
            if int(input_age) <18 or int(input_age) >65:
                raise ValueError(f"You must be over 18 and under 65 to use this survey."
                    )
        else:
            raise ValueError(f"Please enter a number only."
                    )
    except ValueError as e:
        print(f"Invalid data. {e}")
        return False
    return True

def validate_salary(input_salary):
    try:
        if input_salary.isdigit():
            if int(input_salary) <10000 or int(input_salary) >100000:
                raise ValueError(f"Only salaries between 10000 and less than 100000 are eligible to take this survey to keep data representative."
                    )
        else:
            raise ValueError(f"Please enter a number."
                    )
    except ValueError as e:
        print(f"Invalid data. {e}")
        return False
    return True

def calculate_previous_salary_data(survey_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating last years survey data...\n")
    survey = SHEET.worksheet("2021").get_all_values()
    survey_row=survey[0][0:11]
    survey_salaries=survey[1][0:11]
    x=zip(survey_row,survey_salaries)
    for i,k in x:
        print(i)
        print("€",k)

def update_survey_worksheet(new_data):
    """
    Update survey worksheet with new entries
    """
    print("Updating survey worksheet...\n")
    survey_worksheet = SHEET.worksheet("2022")
    survey_worksheet.append_row(new_data)
    print("2022 Survey worksheet updated successfully.\n")


def summary_table(name,salary):
    print(f"Thanks for taking part {name}.")
    print(f"Your salary is €{salary}")




new_data = get_survey_data()
print(new_data)
update_survey_worksheet(new_data)
newsal=calculate_previous_salary_data(new_data)
print(newsal)

