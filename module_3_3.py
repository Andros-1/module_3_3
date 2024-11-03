def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Urban', 123, [1, 2, 3]]
values_dict = {'a': [1, 2, 3], 'b': 'Urban', 'c': 123}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['qwerty', [9, 8, 7]]
print_params(*values_list_2, 42)
