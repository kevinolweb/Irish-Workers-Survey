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
    print("Thank you for your interest in taking part in this survey.\n It is a survey of full time workers in Ireland. \n We ask that you answer all questions truthfully.")

    input_data=input("Please enter your salary e.g 5000 \n")
    print(f"Your salary is €{input_data}")

get_survey_data()