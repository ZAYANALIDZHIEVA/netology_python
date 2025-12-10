#Task1
ids = {"user1": [213, 213, 213, 15, 213],
"user2": [54, 54, 119, 119, 119],
"user3": [213, 98, 98, 35]}

list_number = []
for numbers in ids.values():
    list_number.extend(numbers)
unique_numbers = set (list_number)
print(unique_numbers)


#Task2
queries = [
"смотреть сериалы онлайн",
"новости спорта",
"афиша кино",
"курс доллара",
"сериалы этим летом",
"курс по питону",
"cериалы про спорт",
]
word_length = {}
for query in queries:
    word_count = len(query.split())
    if word_count not in word_length:
        word_length[word_count] =1
    else: word_length[word_count] += 1
for key, value in word_length.items():
    print(f"Поисковых запросов, содержащих {key} {value}")

#Task3
results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}
for company in results:
    revenue = results[company]['revenue']
    cost = results[company]['cost']
    roi = round(((revenue/cost)-1)* 100, 2)
    results[company] ['roi'] = roi
print(results)

#Task4
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
for volume in stats:
    max_volume = max(stats, key = stats.get)
print(f'Максимальный объем продаж на рекламном канале:{max_volume}')

#Task5