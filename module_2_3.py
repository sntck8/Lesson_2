my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    numbers = my_list[index]
    if numbers < 0:
        break
    if numbers > 0:
        print("Положительное число: ", numbers)
    index = index + 1