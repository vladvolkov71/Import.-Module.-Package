from application.db.people import get_employees
from application.salary import calculate_salary
from application.star.star_svg import star

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    star()
