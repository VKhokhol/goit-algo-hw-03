import random
def get_numbers_ticket(min, max, quantity):

    numbers_ticket=set()
    if min < 1 or max > 1000:
        return numbers_ticket
    
    while len(numbers_ticket)< quantity:
        number = random.randint(min, max)
        numbers_ticket.add(number)

    numbers_ticket_set_to_list = list(numbers_ticket)
    sorted_numbers_ticket = sorted(numbers_ticket_set_to_list)
    return sorted_numbers_ticket

print(get_numbers_ticket(1, 1000, 5))
