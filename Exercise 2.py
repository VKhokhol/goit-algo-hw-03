#Імпортування модуля random
import random
#Створення функції з трьома параметрами
def get_numbers_ticket(min, max, quantity):

#Створення пустої множини
    numbers_ticket=set()
#Перевірка умови про діапазони значень min, max
    if min < 1 or max > 1000:
        return list()
#Перевірка умови, щоб число max було більше числа min
    elif max<min:
        return list()
#Перевірка умови, щоб в діапазоні між мінімальним і максимальним
#  можна було обрати необхідну кількість випадкових чисел
    elif max-min+1<quantity:
        return list()
#Створення циклу, в якому перевіряється довжина множини і якщо вона менше quantity, 
#то генерується випадкове число і додається до множини
    while len(numbers_ticket)< quantity:
        number = random.randint(min, max)
        numbers_ticket.add(number)
#Перетворенням множини в список, сортування його та повернення із функції
    numbers_ticket_set_to_list = list(numbers_ticket)
    sorted_numbers_ticket = sorted(numbers_ticket_set_to_list)
    return sorted_numbers_ticket
#Перевірка результату роботи
print(get_numbers_ticket(6, 5, 6))
