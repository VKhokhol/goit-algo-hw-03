#Імпортування модуля datetime
import datetime
#Створення змінної date яку пропонується ввести користувачу
date = input('Введіть дату в форматі YYYY-MM-DD: ')
#Створення функції з параметром date
def date_diff(date):
#Визначення сьогоднішньої дати
    today = datetime.datetime.now().date()
#Перетворення отриманої дати від користувача в об'єкт datetime
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
#Обрахунок різниці між двома датами за модулем
    difference = abs((today - given_date)).days
    return difference
#Перевірка результатів
difference = date_diff(date)
print(f'Різниця між сьогоднішьою датою та заданою: {difference} днів')
