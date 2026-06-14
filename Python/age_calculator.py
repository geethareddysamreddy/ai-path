from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def get_dob():
    while True:
        try:
            dob = input("Enter date of birth (dd-mm-yyyy): ")
            return datetime.strptime(dob, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid format! Please enter as dd-mm-yyyy (e.g. 15-06-2000)")

def get_next_birthday(dob, today):
    try:
        next_birthday = dob.replace(year=today.year)
    except ValueError:
        next_birthday = date(today.year, 3, 1)  # Feb 29 edge case

    if next_birthday < today:
        try:
            next_birthday = date(today.year + 1, dob.month, dob.day)
        except ValueError:
            next_birthday = date(today.year + 1, 3, 1)
    
    return next_birthday

def main():
    dob = get_dob()
    today = date.today()
    age = relativedelta(today, dob)
    print(f"\nAge: {age.years} years, {age.months} months, {age.days} days")

    next_birthday = get_next_birthday(dob, today)
    days_left = (next_birthday - today).days
    print(f"Next Birthday: {next_birthday.strftime('%d %B %Y')}")
    print(f"Days Left: {days_left} days")

main()