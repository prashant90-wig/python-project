from datetime import date

def make_space():
    return {f"\n"*2}

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    years  = today.year - birth_year

    if today.month < birth_month:
        years -= 1
    elif today.month == birth_month and today.day < birth_day:
        years -= 1

    if years == (today.year - birth_year):
        last_birthday = date(today.year, birth_month, birth_day)
    else:
        last_birthday = date(today.year - 1, birth_month, birth_day)

    days_since_birthday = (today - last_birthday).days
    return years, days_since_birthday  


def get_birth_date():
    
    print("Enter your birth date: ")
    year = int(input("Year :"))
    month = int(input("Month ( 1- 12) :"))
    day = int(input("Day ( 1- 31) :"))

    return year, month, day

def main():
    print("========= AGE CALCULATOR =========")
    make_space()

    birth_year, birth_month, birth_day = get_birth_date()

    years, days = calculate_age(birth_year, birth_month, birth_day)
    print(f"You are {years} years and {days} days old as of now!!!")
if __name__ == "__main__":
    main()