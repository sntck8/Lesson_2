num = int(input("Введите число от 3 до 20: "))
if num <= 20 and num >= 3:
    pairs = " "
    for i in range(1,20):
        for j in range(i+1, 20):
            if num % (i + j) == 0:
                pairs += str(i) + str(j)
print("Пароль:", pairs)