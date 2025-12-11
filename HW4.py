documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}
# Функция для нахождения владельца документа по его номеру
def get_owner_by_number(document_number):
    for document in documents:
        if document['number'] == document_number:
            return document['name']
    return None

# Функция для поиска полки по номеру документа
def get_shelf_by_number(doc_num):
    for shelf, numbers in directories.items():
        if doc_num in numbers:
            return shelf
    return None

# Функция для вывода полной информации о всех документах
def show_all_documents():
    for doc in documents:
        doc_number = doc['number']
        shelf = get_shelf_by_number(doc_number)
        print(f"№: {doc_number}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {shelf}")

# Функция для добавления новой полки
def add_new_shelf(shelf_number):
    if shelf_number in directories:
        print(f"Такая полка уже существует. Текущий перечень полок: {list(directories.keys())}.")
    else:
        directories[shelf_number] = []
        print(f"Полка добавлена. Текущий перечень полок: {list(directories.keys())}.")

# Функция для удаления пустой полки
def remove_empty_shelf(shelf_number):
    if shelf_number in directories:
        if len(directories[shelf_number]) > 0:
            print(f"Полка {shelf_number} не пуста. Уберите документы перед удалением.")
        else:
            del directories[shelf_number]
            print(f"Произведено удаление полки {shelf_number}. Текущие полки: {list(directories.keys())}.")
    else:
        print(f"Такой полки ({shelf_number}) не существует.")

if __name__ == "__main__":
    while True:
        user_input = input("Введите команду ('q' для завершения): ").strip().lower()
        
        if user_input == 'q':
            break
        
        elif user_input == 'p':  # Узнать владельца документа
            doc_num = input("Введите номер документа: ")
            owner = get_owner_by_number(doc_num)
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден в базе.")
        
        elif user_input == 's':  # Узнать полку по номеру документа
            doc_num = input("Введите номер документа: ")
            shelf = get_shelf_by_number(doc_num)
            if shelf:
                print(f"Документ хранится на полке: {shelf}")
            else:
                print("Документ не найден в базе.")
        
        elif user_input == 'l':  # Просмотреть информацию обо всех документах
            show_all_documents()
        
        elif user_input == 'ads':  # Добавить новую полку
            shelf_num = input("Введите номер полки: ")
            add_new_shelf(shelf_num)
        
        elif user_input == 'ds':  # Удалить полку
            shelf_num = input("Введите номер полки: ")
            remove_empty_shelf(shelf_num)
        
        else:
            print("Ошибка. Неправильно указана команда.")