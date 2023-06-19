def display_hello_world():
    print("Hello world!")


def say_greetings(name: str):
    print(f"Hello {name}")


display_hello_world()
say_greetings("John")

def count(a: int, b: int):
    print(a + b)


count(13,37)


# Exercice OpenClassRoom
def monthly_bill(annual_bill: int):
    monthly_income = annual_bill / 12
    return monthly_income

def weekly_bill(monthly_bill: int):
    weekly_income = monthly_bill / 4
    return weekly_income

def hourly_bill(weekly_bill: int, working_hours: int):
    hours_income = weekly_bill / working_hours
    return print(f"Vous percevez un salaire de {hours_income}€ par heures.")

user_annual_salary: int = int(input("Quelle est votre salaire annuel? "))
user_weekly_hours: int = int(input("Combien d'heures travaillez-vous par semaine? "))

user_monthly_salary:int = monthly_bill(user_annual_salary)
user_weekly_bill: int = weekly_bill(user_monthly_salary)
hourly_bill(user_weekly_bill, user_weekly_hours)