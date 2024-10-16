#1.Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
#вывод функции
print_params()
print_params(5, "Sasha", False)
print_params(a='Urban', b=5)
print_params(b=25)  # результат выводит 1 25 True
print_params(c=[1, 2, 3])  # результат выводит 1 строка [1, 2, 3]

#2.Распаковка параметров
values_list = [1, "Hello", True]
values_dict = {'a': 5.8, 'b': 'Лимонад', 'c': [5, 6]}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры
values_list_2 = [5, "World"]
print_params(*values_list_2, 42) # результат выводит 5 World 42
