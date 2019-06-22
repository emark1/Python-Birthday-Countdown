import datetime

def print_header():
    print('BIRTHDAY APP LOL')

def get_birthday():
    print("When were you born? ")
    year = int(input("Year [yyyy]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday(days):
    if days < 0:
        print('Your birthday was {} days ago this year.'.format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("HAPPY BIRTHDAY SON")

def main():
    print_header()
    bday = get_birthday()
    now = datetime.date.today()
    number_of_days = compute_days(bday, now)
    print_birthday(number_of_days)

main()