countrydatabase = {}
while True:
    print("1 - add the data")
    print("2 - display all countries")
    print("3 - display all capitals")
    print("4 - get capital")
    print("5 - delete")
    print("6 - exit")
    choice = int(input("which option would you like to choose? "))
    if choice == 1:
        country = input("add the country ")
        capital = input("enter the capital ")
        countrydatabase[country] = capital
        print(countrydatabase, " - this is all the countries now added to the database.")
    elif choice == 2:
        print(countrydatabase.keys())
    elif choice == 3:
        print(countrydatabase.values())
    elif choice == 4:
        countrychoice = input("which country would you like the capital of? ")
        print(countrydatabase.get(countrychoice))
    elif choice == 5:
        countrydelete = input("which country would you like to delete? ")
        del countrydatabase[countrydelete]
        print(countrydelete, "has been removed from", countrydatabase)
    elif choice == 6:
        break
    else:
        print("this is not a value, please try again. ")
