first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second and first == third:
    print("Все числа равны!")
elif first == second or  second == third or third == first:
    print("Равны два из трех чисел!")
# elif first != second or  second != third or third != first:
else:
    print("Равных чисел нет!")
