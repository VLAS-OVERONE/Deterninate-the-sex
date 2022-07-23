age = 25 #integer
# print('Возраст: ' + age) do not work
print('Возраст: ' + 'age') #print word 'age'
print('Возраст: ' + str(age))
print('Возраст:', age)

temp = 5.9 #float
print('Температура:', temp, 'градусов')

username = "Alex" #string
print('Имя пользователя', username)
print('Имя пользователя', username); print('Имя пользователя', username) #для написания в одну строку нужна ';'

isexists = True #boolean
isexists1 = False
print('Существует:', isexists)
print('Не существует:', isexists1) # а также можно переприсваивать значение переменной:

isexists = True #boolean
print('Существует:', isexists)
isexists = False  # boolean
print('Не существует:', isexists)

# Определение типа переменной:
print('Тип переменной:', type(age))
print('Тип переменной:', type(temp))
print('Тип переменной:', type(isexists))
print('Тип переменной:', type(age))

# Для вывода строки на новый абзац используется тройная ковычка:
print('''Первая строка
Вторая строка
Третья строка''')