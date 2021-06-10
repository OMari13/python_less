# *** переменные ***
my_var_1 = 100
myVar2 = 200

c = my_var_1 + myVar2

# комментирование - ctrl + /
# print(c)

# заглавными буквами пишутся названия констант 
PI = 3.14

# *** типы данных ***
_int = 100000
_float = 500.001 

my_str = "Привет 'мир' !"

# print(my_str)
# print(_float)

# булевы типы данных (boolean, bool)
# True/False
my_bool = True # Истина, логическая 1, False - лог 0

# *** способ форматирования под названием "f-строка" ***
# старейший способ формат-я - конкатенация 
z = "Hello"
r = ' '
q = ", World!"

s = z + r + q 

# print(s)

res = f"1 слово: {z} 2 слово: {r} 3 строка = {q}"

# print(res)


# *** арифметические операции ***

var_1 = 5
var_2 = 2

# операция сложения 
print(var_1 + var_2)

# операция вычитания 
print(var_1 - var_2)

# операция умножения 
print(var_1 * var_2)

# операция простого деления
# возвращает всегда тип float
print(var_1 / var_2)

# операция целочисленного деления
# возвращает всегда тип int
# при этом без округления
print(var_1 // var_2)