import json

file_name = "library.json"
library = []

def load_library():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return "Упс...не найдено"
    except json.decoder.JSONDecodeError:
        print("Оишбка чтения JSON-файла")
        return []


def save_library(library): #Функция сохрания изменений в файле
    with open(file_name, "w") as file:
        json.dump(library, file, indent=3)
    print(library)


def display_library(library): #Отображение всех книг библеотеки
    if not library:
        print("В библиотеке пусто..")
    else:
        for book in library:
            print(f"id: {book['id']}, title: {book['title']}, author: {book['author']}, "
                  f"year: {book['year']}, status: {book['status']}")

def add_book(library): #Добавление книги
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")

    new_book = {
        "id": len(library) + 1,
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии"
    }


    library.append(new_book)
    save_library(library)
    print("Книга добавлена!")



def delete_book(library): #Удаление книги по ID
    try:
        books_id = int(input("Введите ID книги которую хотите: "))
        for book in library:
            if book['id'] == books_id:
                library.remove(book)
                save_library(library)
                print("Книга успешно удалена!")
            else:
                print("Книга не найдена :(")

    except ValueError:
        print("Неккоректный ID!")


def search_book(library): #Поиск книги по названию и всему что указано в book_search
    book_search = input("Для посика введите название, автора или год книги: ").lower()
    results = [book for book in library if book_search in book["title"].lower() or
               book_search in book["author"].lower() or
               book_search in book["year"]]
    if results:
        for book in results:
            print(f"ID: {book['id']}, title: {book['title']}, author: {book['author']},\n"
                  f"Year: {book['year']}, status: {book['status']}")
    else:
        print("Книга не найдена.")


def change_status(library): #изменение статуса книги
    try:
        book_id = int(input("Введите ID книги: "))
        new_status = input("Введите новый статус книги(в наличиии/выдана): ").lower()
        if new_status not in["в наличии", "выдана"]:
            print("Неккоректный ввод")
            return []
        for book in library:
            if book['id'] == book_id:
                book['status'] = new_status
                save_library(library)
                print("Статус обновлен!")
                return []
        print("Книга с таким ID не найдено!")
    except ValueError:
        print("Неккоректный ввод ID")


def main(): #Главная станица библеотеки
    library = load_library()
    while True:
        print("-------Добро пожаловать в Библиотеку-------")
        print("-1. Показать все книги-")
        print("--2. Добавить книгу--")
        print("---3. Удалить книгу---")
        print("----4. Найти книгу----")
        print("-----5. Изменить статус книги-----")
        print("------6. Выход------")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_library(library)
        elif choice == "2":
            add_book(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            change_status(library)
        elif choice == "6":
            print("Приходите ещё!")
            break
        else:
            print("А такого нет,давай ещё раз")

if __name__ == "__main__":
    main()




