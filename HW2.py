#Task1
word = input("Введите слово: ").strip()
while not word:
    print("Слово не введено. Необходимо ввести слово")
    word = input("Введите слово: ").strip()
length = len(word)
if length %2 == 0:
    fm = word[(length//2) - 1]
    sm = word[length//2]
    middle_chetn = fm+sm

    print(middle_chetn)

else:
    middle_nechetn = word[(length//2)]
    print(middle_nechetn)
#Task2
total_number = []
while True:
    number = float(input("Введите число "))
    if number == 0:
        break
    total_number.append(number)
result = sum(total_number)
print(f"Результат: {result:.2f}")

#Task3
def sort_of_matches(boys_list, girls_list):
    sorted_boys = sorted(boys_list)
    sorted_girls = sorted(girls_list)
    if len(sorted_boys)!=len(sorted_girls):
        return "Внимание, кто-то может остаться без пары!"
    matches = list(zip(sorted_boys, sorted_girls))
    return matches
boys_list = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls_list = ["Kate", "Liza", "Kira", "Emma", "Trisha"]
print(sort_of_matches(boys_list, girls_list))

#Task4
from statistics import mean
countries_temperature = [
["Таиланд", [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
["Германия", [57.2, 55.4, 59, 59, 53.6]],
["Россия", [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
["Польша", [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
average = {}
for country, temps in countries_temperature:
    avg_temp = mean((t - 32)*5 / 9 for t in temps)
    average[country] = round(avg_temp,1)
print(average)
    
    

    
