a = input()
b = input()
if '@' not in a and '@' in b:
    print('OK')
elif '@' in a and '@' in b:
    print('Некорректный логин')
elif '@' not in a and '@' not in b:
    print('Некорректный адрес')
elif '@' in a and '@'  not in b:
    print('Некорректный логин')
elif '@'  in a and '@' not in b:
    print('Некорректный адрес')