#это был мой вариант
#def is_year_leap(x):
#    if x % 4 == 0:
#        return True
#    else:
#        return False

#year = is_year_leap(2020)
#print("год", "2020", ":", year) 

#это вариант после просмотра разбора
year = int(input("Введите год: "))
def is_year_leap(year):
    if year % 4 == 0:
       return True
    else:
        return False
result = is_year_leap(year)
print("год", year , result)

