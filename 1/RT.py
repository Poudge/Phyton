password = input("Введите пароль:")

lowerCase = False
upperCase = False
specialChars = False
digits = False
length = False

for letter in password:
    if letter == letter.lower():
        lowerCase = True

    if letter ==letter.upper():
        upperCase = True

    if 48 <=ord(letter) <= 57:
        digits = True

    if 33 <=ord(letter) <= 47:
        digits = True

if len(password) >= 10:
    len = True

score = 0
errors = ""

array = [lowerCase, upperCase, specialChars, digits, length]

for i in range(5):
    if array[i] == True:
        score += 1
    else:
        if i == 0:
            errors += "некоректный пароль: нет прописных букв\n"
        elif i == 1:
            errors += "некоректный пароль: нет прописных букв\n"
        elif i == 2:
            errors += "некоректный пароль: нет цифр\n"
        elif i == 3:
            errors += "некоректный пароль: нет знаков пунктуации\n"
        elif i == 4:
            errors += "некоректный пароль: некоректная длина пароля\n"

print(f"f Надёжность пароля = {score}, ошибки = {errors}")
