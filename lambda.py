people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)

say_to_all(lambda a: print(f'Здравствуй, {a}!' if a[0] == 'С' else f'Привет, {a}!') ,people)