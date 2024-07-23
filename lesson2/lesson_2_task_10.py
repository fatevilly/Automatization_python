def bank(x,y):
    percent = 0.10
    sum_after_year = x * (1 + percent) ** y
    return sum_after_year

x = float(input("сумма вклада: "))
y = int(input("на сколько лет вклад: "))

result = bank(x,y)
print("Итоговая сумма для получения через" , y, "лет", "составляет", result)