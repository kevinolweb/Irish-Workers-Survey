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
    salary_comparison(input_salary)
    return list_data


def validate_data(input_age):
    """
    This function validates inputted age ensuring it is a number and conforms to age limits.
    """
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
    """
    This function validates inputted salary ensuring it is a relevant salary figure and a number.
    """
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


def salary_comparison(user_inputted_salary):
    """
    Gets users salary and compare to average for 2021
    """
    salary_survey_data = SHEET.worksheet("2021").get_all_values()
    survey_salaries=salary_survey_data[1][0:11]
    overall_average_salary=avg_salary(survey_salaries)
    survey_salaries_growth=salary_survey_data[2][0:11]
    print("The overall average salary for 2021 was: €",overall_average_salary)
    transformed_salary=int(overall_average_salary)
    transformed_input_salary=int(user_inputted_salary)
    compare=int(transformed_input_salary)-int(transformed_salary)
    if compare >0:
        print("You earn €", compare, "more than the average salary.")
    elif compare <0:
        print("You earn €", compare, "less than the average salary.")
    else:
        print("You earn €", compare, "an average salary.")

def calculate_previous_salary_data(survey_row):
    """
    Gets data from worksheet last year across all sectors
    """
    print("Last years survey results by Industry (2021)\n")
    survey = SHEET.worksheet("2021").get_all_values()
    survey_row=survey[0][0:11]
    survey_salaries=survey[1][0:11]
    survey_salaries_growth=survey[2][0:11]
    salary_info=zip(survey_row,survey_salaries,survey_salaries_growth)
    for i,k,m in salary_info:
        print("---------------")
        print(i)
        print("Avg Salary By Industry: €",k)
        print("Salary Growth/Decline YOY: ",m)


def avg_salary(salary_data):
    """
    This function validates gets the average salary from worksheet.
    """
    total=0
    for salary in salary_data:
        total+=int(salary)
    average=round(total/len(salary_data))
    return average

def update_survey_worksheet(new_data):
    """
    Updates survey worksheet with new entries
    """
    survey_worksheet = SHEET.worksheet("2022")
    survey_worksheet.append_row(new_data)


def summary_table(name,salary):
    """
    This function summaries the persons name and salary for user feedback purposes.
    """
    print(f"Thanks for taking part {name}.")
    print(f"Your salary is €{salary}")


def main():
    """
    This function is the main function which runs the program.
    """
    new_data = get_survey_data()
    update_survey_worksheet(new_data)
    press_to_continue=input("Would you like to know the 2021 average salary breakdown by Industry?Please enter y/n \n")
    if press_to_continue.lower() =="y":
        calculate_previous_salary_data(new_data)
        print("\n***************")
        print("I hope this information was valuable to you. Thanks again for taking part.")
    else:
        print("\n***************")
        print("Ok, you have not selected yes so thanks again for taking part.")


main()
