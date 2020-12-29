myBook = input()
counter = 0
searchBook = ""

while searchBook != myBook:
    currentBook = input()
    if currentBook == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    if currentBook == myBook:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1




