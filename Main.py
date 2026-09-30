po = 0
items = ["pen", "pencil", "eraser", "sharpener", "notebook", "ruler", "marker", "highlighter", "stapler", "tape", "glue", "scissors", "calculator", "folder", "binder", "paper clips", "rubber bands", "push pins", "sticky notes", "index cards"]

for po in range(4):

    print("press 1 to add an item")
    print("press 2 to view and lend an item")
    print("press 9 to search for an item")
    command = input("what do you want to do: (press 999 to exit) ")
    command1 = int(command)
    
    if command1 == 1:
            yap = input("enter the item you want to add: ")
            items.append(yap)
            print(f"you have added {yap} to your list")
    elif command1 == 2:
            print(items)
            yap1 = input("press 3 to lend an item and press 4 to exit: ")
            if yap1 == "4":
                print("thank you for using our service")
                break 
            elif yap1 == "3":
                lend = input("enter the item you want to lend: ")
                if lend in items:
                    items.remove(lend)
                    print(f"you have lent {lend}")
                else:
                    print(f"{lend} is not available")

    elif command1 == 999:
            print("thank you for using our service")
            break           
    elif command1 == 9:
            search = input("enter the item you want to search for: ")
            if search in items:
                print(f"{search} is available")
            else:
                print(f"{search} is not available")