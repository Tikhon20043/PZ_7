#Даны строки S и S0. Проверить, содержится ли строка S0 в строке S.
#Если содержится, то вывести TRUE, если не содержится, то вывести FALSE.

def check_string(S, S0):
    return S0 in S

S = "13, 16, 87, 2, 54, 76, 93, 23, 14, 56, 36, 40, 64"  # Задаем строку S
S0 = "13, 16, 87, 2, 54, 76"  # Задаем строку S0

result = check_string(S, S0)  # Проверяем, содержится ли S0 в S

print(result)  # Выводим результат на экран