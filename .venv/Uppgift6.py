toDoList = []
print("1. Se innehållet i din lista")
print("2. Lägga till nya punkter i din lista")
print("3. Markera som klar")
print("4. Avsluta")
userChoice = 0

while userChoice != 3:
    userChoice = input("Välj ett alternativ: ")
    if userChoice == "1":
        if len(toDoList) == 0:
            print("Din lista är tom")
        else:
            for i in range(len(toDoList)):
                print(f"+ " + toDoList[i])

    elif userChoice == "2":
        item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        toDoList.append(item)
        print("Ok, lade till " + item + " i listan.")

    elif userChoice == "3":
        removeIndex = input("Vilken grej är du färdig med? ")
        if 0 < int(removeIndex) <= len(toDoList):
            toDoList.pop(int(removeIndex) - 1)
        else:
            print("Punkten finns inte i listan")

    elif userChoice == "4":
        break
    else:
        print("Fel val, försök igen!")