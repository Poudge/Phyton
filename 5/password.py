# passwod > 10
#'a-z', 'A-Z', '*/-+&3#@', 1-9 0

import string

upper_case = False
lower_case = False
special_chars = False
digits = False
lenght = False

password = input("Введите пароль для проверки : ")

for letter in password:
    if letter in string.ascii_lowercase:
        lower_case = True

    if letter in string.ascii_uppercase:
        upper_case = True

    if letter in string.digits:
        digits = True

    if letter in string.punctuation:
        special_chars = True

if len(password) > 10:
    lenght = True

characters = [upper_case, lower_case, digits, special_chars, lenght]

#print(characters)

score = 0
error = ""

for i in range(0, len(characters)):
    if characters[i] == True:
        score += 1
    else:
        if i == 0:
            error += " Нет заглавных символов, "
        elif i == 1:
            error += " Нет строчных символов, "
        elif i == 2:
            error += "Цет цифр, "
        elif i == 3:
            error += " Нет спец символов, "
        elif i == 4:
            error += " Длина должна быть больше 10 символов, "


print(f"Надежность пароля {score} из 5, ошибки: {error}")

