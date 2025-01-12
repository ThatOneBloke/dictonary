books = {"harry potter, the philosophers stone":4, "jurasic park, the lost world": 3, "goosebumps 2": 1, "goosebumps 7": 2, "the famous five 4": 4, "the famous five 5": 5, "the famous 5 9": 0}

print("select book", books)
what_book = input("what book would you like? ")

if what_book in books:
    print("we have the book")
    book_details = books[what_book]
    print("the cost of the book is ", book_details)

else:
    print("the book does not exist, try again")

