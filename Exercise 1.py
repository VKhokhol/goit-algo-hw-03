import datetime
def date_diff(date):
    today = datetime.datetime.now().date()
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    difference = abs((today - given_date)).days
    return difference
print(date_diff('2025-08-25'))
