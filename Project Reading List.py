
def delete_book(books: list[dict]):
    book_list: list[dict] = get_all_books()

    for book in book_list:
        if books[0]["title"] == book['title']:
            print("-" * 55)
            print(f"{books[0]['title']} have been remove from the library!")
            print("-" * 55)
            print('')
            book_list.remove(book)

    with open("data_files/books.csv", "w") as reading_list:
        for book in book_list:
            title, author, year, status = book.values()
            reading_list.write(f"{title}, {author}, {year}, {status}\n")


def mark_book(books: list[dict]):
    book_list: list[dict] = get_all_books()

    for book in book_list:
        if books[0]["title"] == book["title"] and book["status"] == "not read":
            book["status"] = "read"
            print("-" * 55)
            print("Status Updated")
            print("-" * 55)
            print('')
            break

    else:
        print("-" * 55)
        print("The book is already have been read!")
        print("-" * 55)
        print('')

    with open("data_files/books.csv", "w") as reading_list:
        for book in book_list:
            title, author, year, status = book.values()
            reading_list.write(f"{title}, {author}, {year}, {status}\n")


def search_book() -> list[dict]:
    book_list: list[dict] = get_all_books()
    matching_books: list[dict] = []

    print("-" * 55)
    search_title: str = input("Enter the book title: ").strip().title()

    for book in book_list:
        if search_title == book["title"]:
            matching_books.append(book)

    return matching_books


def list_book(books: list[dict]):

    print("-" * 55)

    for book in books:
        print(f"{book['title']} ({book['year']}) by {book['author']}. Status: {book['status']}")

    print("-" * 55)
    print('')


def add_book():
    book_list: list[dict] = get_all_books()

    print("-" * 55)
    title: str = input("Enter a book title: ").strip().title()
    author: str = input("Enter the author of the book: ").strip().title()
    year: str = input("Enter the book Publication year: ")

    for book in book_list:
        if title == book["title"]:
            print("-" * 55)
            print("The Book is already in your library")
            print("-" * 55)
            print('')
            break

    else:
        print("-" * 55)
        print("library updated")
        print("-" * 55)
        print('')

        with open("data_files/books.csv", "a") as reading_list:
            reading_list.write(f"{title}, {author}, {year}, not read\n")


def get_all_books() -> list[dict]:
    books: list[dict] = []

    with open("data_files/books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, status = book.strip().split(", ")

            books.append({
                "title": title,
                "author": author,
                "year": year,
                "status": status
            })

    return books


def check_csv_file():  # check if the files exist if not create
    try:
        with open("data_files/books.csv", "x", encoding="UTF-8") as book_list:
            book_list.write("")

    except FileExistsError:
        pass


def main():
    menu_choices: str = """Please Select the Following Options:
    
    - 'a' to add a book
    - 'l' to list a book
    - 's' to search for a book
    - 'm' to mark the book as read
    - 'd' to delete a book
    - 'q' to quit the system
    
what is your choice: """
    print('')

    while (user_prompt := input(menu_choices).strip().lower()) != 'q':

        check_csv_file()

        if user_prompt == "a":
            add_book()

        elif user_prompt == "l":
            book_list: list[dict] = get_all_books()

            if book_list:
                list_book(book_list)
            else:
                print("Your Library is Empty")
                print("-" * 55)
                print('')

        elif user_prompt == "s":
            search: list[dict] = search_book()

            if search:
                list_book(search)

            else:
                print("Can't find the book you are searching for!")
                print("-" * 55)
                print('')

        elif user_prompt == "m":
            upd_search: list[dict] = search_book()

            if upd_search:
                mark_book(upd_search)
            else:
                print("-" * 55)
                print("Can't find the book in your library!")
                print("-" * 55)
                print('')

        elif user_prompt == 'd':
            del_search: list[dict] = search_book()

            if del_search:
                delete_book(del_search)
            else:
                print("-" * 55)
                print("Can't delete the book not in your library!")
                print("-" * 55)
                print('')

        else:
            print("-" * 55)
            print("Invalid Choices")
            print("-" * 55)
            print('')

    else:
        print("-" * 55)
        print("quitting the system")
        print("-" * 55)
        print('')


if __name__ == '__main__':
    main()
    