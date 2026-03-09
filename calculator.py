my_list = []

while True:
    print("\n         MENU         \n")
    print("   1. Show Users","\n   2. Add User", "\n   3. Update User", "\n   4. Delete User", "\n   5. Exit")

    choice = int(input("\n Enter Choice: "))
    if choice == 1:
        print ("\n      Show User      \n", my_list)

    elif choice == 2:
        print("\n      Add User      ")
        add = input("Add User: ")
        my_list.append(add)
        print (my_list)

    elif choice == 3:
        print ("\n      Update User      \n")
        user_index = int(input("User's index to update: "))
        update = input("Update to user: ")
        my_list[user_index] = update
        print (my_list)

    elif choice == 4:
        print("\n      Delete User      \n")
        userDel = input("User to delete: ")
        my_list.remove(userDel)

    elif choice == 5:
        print ("Done")

    else:
        print ("Invalid!")