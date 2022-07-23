# По введённому имени с помощью функции определяем пол человека.

dict = {
    'Andrey': 'male',
    'Sergey': 'male',
    'Alexandr': 'male',
    'Sveta': 'female',
    'Tanya': 'female',
    'Katya': 'female',
}

def sex(key, dict):
    for k, v in dict.items():
        if k == key: return v
    return "There is no such name in the list"

print(sex(input("Введите Имя: \n"), dict))

