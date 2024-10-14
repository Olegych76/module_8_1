def add_everything_up(a, b):
    try:
        return f'Всё прошло штатно: {a + b}'
    except TypeError:
        return f'Пришлось делать преобразование типов: {str(a) + str(b)}'


# Варианты использования:
print(add_everything_up(123.456, 'строка'))  # float + string
print(add_everything_up('яблоко', 4215))  # string + int
print(add_everything_up(123.456, 7))  # float + int
