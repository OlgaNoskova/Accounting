from art import *
from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    tprint("hello",font="block",chr_ignore=True)