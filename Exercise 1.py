import datetime
date = input('Введіть дату в форматі YYYY-MM-DD: ')
def date_diff(date):
    today = datetime.datetime.now().date()
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    difference = abs((today - given_date)).days
    return difference
difference = date_diff(date)
print(f'Різниця між сьогоднішьою датою та заданою: {difference} днів')
