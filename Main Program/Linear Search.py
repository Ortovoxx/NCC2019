def linearsearch(item,shoppingList): #defines the shopping list function
    position = 0
    found = False
    while position < len(shoppingList) and not found:
        if shoppingList[position] == item:
            found = True
        position = position + 1
    return found


shoppingList = ["eggs", "bacon", "bread"] #defines shopping list

searches = 0
looping = True #loops the search
while looping == True:
    item = input(str("Search for an item: "))
    listFound = linearsearch(item,shoppingList)
    if listFound == True: 
        print("Found", searches)
        displayList = input("Do you want to print the list?")
        if displayList == "yes" or "yup" or "of course":
            print(shoppingList)
    else:
        print("Not found", searches)
        addToList = input("Do you want to add that item to the list?") 
        if addToList == "yes" or "yup" or "of course": #if the user wants to add to the list it adds to list
            shoppingList.append(item)
            '''
            addMoreToList = input("Do you want to add anything else?")
            if addMoreToList == "yes" or "yup" or "of course":
                whatToAdd = input("What do you want to add?")
                shoppingList.append(whatToAdd)
            '''
        searches = searches + 1 # incraments the searches
