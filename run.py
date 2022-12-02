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
    input_salary=input("Please enter your salary press Enter E.g 21\n")
    list_data.append(input_salary)
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

def summary_table():
    print(f"Thanks for taking part {input_name}.")
    input_data=input("Please enter your salary e.g 5000 \n")
    print(f"Your salary is €{input_data}")

def update_survey_worksheet(new_data):
    """
    Update survey worksheet, add new row with the list data provided
    """
    print("Updating survey worksheet...\n")
    survey_worksheet = SHEET.worksheet("2022")
    survey_worksheet.append_row(new_data)
    print("2022 Survey worksheet updated successfully.\n")


new_data = get_survey_data()
print(new_data)
update_survey_worksheet(new_data)