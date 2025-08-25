#Імпортування модуля datetime
import datetime
#Створення змінної date яку пропонується ввести користувачу
date = input('Введіть дату в форматі YYYY-MM-DD: ')
#Створення функції з параметром date
def get_days_from_today(date):
#Створення блоку try, в якому виконується спроба обрахувати різницю
    try:
 #Визначення сьогоднішньої дати       
        today = datetime.datetime.now().date()
#Перетворення отриманої дати від користувача в об'єкт datetime
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
#Обрахунок різниці між двома датами за модулем
        difference = (given_date-today).days
        return difference
#Якщо користувач вводить дату в неправильному форматі - вилазить помилка ValyeError,
#  яка перехоплюється та виводиться повідомлення для користувача
    except ValueError:
        print('Неправильний формат дати. Задайте дату у вигляді YYYY-MM-DD')
        return None
#Перевірка результатів
difference = get_days_from_today(date)
if difference is not None:
    print(f'Різниця між сьогоднішьою датою та заданою: {difference} днів')
