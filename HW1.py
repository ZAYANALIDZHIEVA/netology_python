##Task1
phrase_1 = len("погодапогодапогода")
phrase_2 = len("лес")
if phrase_1 > phrase_2:
     print("Фраза 1 длиннее фразы 2")
elif phrase_1 < phrase_2:
     print("Фраза 2 длиннее фразы 1")
else:
     print("Фразы равной длины")
###Task2
year = 2019
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print ("Високосный год")
else:
     print ("Обычный год")
###Task3
day = int(input("Введите дату рождения "))
month = str(input("Введите месяц рождения "))
if ((month == "Март" or month == "март") and 21 <= day <= 31) or ((month == "Апрель" or month == "апрель") and 1 <= day <= 19):
     print ("Овен")
elif((month == "Апрель" or month == "апрель")and 20 <= day <= 30) or ((month == "Май" or month == "Май") and 1 <= day <= 20):
    print ("Телец") 
elif ((month == "Май" or month == "май") and 21 <= day <= 31) or ((month == "Июнь" or month == "июнь") and 1<= day <= 20):
     print ("Близнецы")
elif ((month == "Июнь" or month == "июнь") and 21 <= day <= 30) or ((month == "Июль" or month == "июль") and 1 <= day <= 22):
     print ("Рак")
elif ((month == "Июль" or month == "июль")and 23 <= day <= 31) or ((month == "Август" or month == "август")  and 1 <= day <= 22):
     print ("Лев")
elif ((month == "Август" or month == "август") and 23 <= day <= 31) or ((month == "Сентябрь" or month == "сентябрь") and 1 <= day <= 22):
     print ("Дева")
elif ((month == "Сентябрь" or month == "сентябрь") and 23 <= day <= 30) or ((month == "Октябрь" or month == "октябрь") and 1 <= day <= 22):
     print ("Весы")
elif ((month == "Октябрь" or month == "октябрь") and 23 <= day <= 31) or ((month == "Ноябрь" or month == "ноябрь") and 1 <= day <= 21):
     print ("Скорпион")
elif ((month == "Ноябрь" or month == "ноябрь") and 22 <= day <= 30) or ((month == "Декабрь"  or month == "декабрь") and 1 <= day <= 21):
     print ("Стрелец")
elif ((month == "Декабрь" or month == "декабрь") and 22 <= day <= 31) or ((month == "Январь"  or month == "январь") and 1 <= day <= 19):
     print ("Козерог")
elif ((month == "Январь" or month == "январь") and 20 <= day <= 31) or ((month == "Февраль" or month == "февраль") and 1 <= day <= 18):
     print ("Водолей")
elif ((month == "Февраль" or month == "февраль") and 19 <= day <= 29) or ((month == "Март" or month == "март") and 1 <= day <= 20):
     print ("Рыбы")
###Task4
width = int(input("Введите ширину в см "))
length = int(input("Введите длину в см "))
height = int(input("Введите высоту в см "))

if width <= 15 and length <= 15 and height <= 15:
     print("Коробка №1")
elif width > 200 or length >200 or height > 200:
     print("Упаковка для лыж")
elif (15 < width < 50) or (15 < length < 50) or (15 < height <50):
     print("Коробка №2")
else:
     print("Коробка №3")
###Task5
tickets_number = int(input("Введите номер билета "))
if tickets_number >= 100000 and tickets_number <= 999999:
     a = int(tickets_number/100000)
     b = int(tickets_number/10000%10)
     c = int(tickets_number/1000%10)
     d = int(tickets_number/100%10)
     e = int(tickets_number/10%10)
     f = int(tickets_number%10)
     if ((a+b+c) == (d+e+f)):
          print("Счастливый билет") 
     else:
          print("Несчастливый билет")
else:
     print("Введены некорректные данные")
#Task6
import math
type_of_figures = input("Введите тип фигуры")
if type_of_figures.strip().lower() in ["круг"]:
     radius =float(input ("Введите радиус круга:  "))
     ploshad_kruga =  math.pi * radius ** 2
     print(f"Площадь круга: {ploshad_kruga:.2f}")
elif type_of_figures.strip().lower in ["треугольник"] :
     input ("Введите длины сторон треугольника")
     a = float(input("Введите длину стороны а "))
     b = float(input("Введите длину стороны b "))
     c = float(input("Введите длину стороны с "))
     pp = (a+b+c)/2
     triangle_sq = pp * (pp - a) * (pp - b) * (pp - c)
     triangle_ploshad = triangle_sq ** 0.5
     print(f"Площадь треугольника: {triangle_ploshad:.2f}")
elif type_of_figures.strip().lower() in ["прямоугольник"]:
     d = float(input ("Введите длину прямоугольника "))
     e = float(input("Введите ширину прямоугольника "))
     rectangle_sq = d * e
     print(f"Площадь прямоугольника: {rectangle_sq:.2f}")
else: 
     print("Вы ввели недоступный тип фигуры")



