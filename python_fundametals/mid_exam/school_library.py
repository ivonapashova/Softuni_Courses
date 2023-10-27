books = input().split("&")

while True:
    command = input().split(" | ")
    if command[0] == "Add Book":
        book = command[1]
        if book not in books:
            books.insert(0, book)
    elif command[0] == "Take Book":
        book = command[1]
        if book in books:
            books.remove(book)
    elif command[0] == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in books and book2 in books:
            index1 = books.index(book1)
            index2 = books.index(book2)
            books[index1], books[index2] = books[index2], books[index1]
    elif command[0] == "Insert Book":
        book = command[1]
        if book not in books:
            books.append(book)
    elif command[0] == "Check Book":
        index = int(command[1])
        if 0 <= index < len(books):
            print(books[index])
    elif command[0] == "Done":
        break

print(", ".join(books))
