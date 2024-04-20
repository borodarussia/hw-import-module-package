from application import salary
from application.db import people

from datetime import datetime

if __name__ == '__main__':
    print(f'Сегодня - {datetime.today()}')
    salary.calculate_salary()
    people.get_employees()
