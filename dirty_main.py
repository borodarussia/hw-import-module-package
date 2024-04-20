from application.salary import *
from application.db.people import *

from datetime import datetime

if __name__ == '__main__':
    print(f'Сегодня - {datetime.today()}')
    calculate_salary()
    get_employees()