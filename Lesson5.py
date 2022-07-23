b1 = True
b2 = False
print('b1 =', b1)
print('b2 =', b2)
print('b1 or b2', b1 or b2) # Напечатать если есть True. Перебором ишет True, пока не найдет
print('b2 or b1', b1 or b2) # Снова перебором ишет True до тех пор, пока не найдет
print(' b1 and b2:', b1 and b2) # Печатать True, если оба True. В противном случае - False
print('   not b1:', not b1, '\n   not b2:', not b2) # Поменяет значение на противоположное
print('b1 не равно b2:', b1 != b2) # Если b1 не равно b2, то True. Иначе False
print('b1 равно b2:', b1 == b2) # Если b1 равно b2, то False. Иначе True
print('- - - - - - - ')
# Операторы сравнения:
x = 5
y = 7
print('x =', x)
print('y =', y)
print('x > y:', x > y)
print('x < y:', x < y)
print('x >= y:', x >= y)
print('x <= y:', x <= y)
print('- - - - - - - -')
# Комбинирование:
print('x and b1 or (x > 10):', x and b1 or (x > 10)) # Первым действием выполняются скобки. Результат: False.
# Имеем True and True or False. Далее выполняется and. Т.е. True and True. Результат True. Имеем True or False.
# Результат True
# Приоритеты операций:
# Сначала скобки, потом умножение(деление), потом сложение(вычитание) и только потом 1 - "not"; 2 - "and" и 3 - "or"