menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter your name: ")
print(menu)
selection = input().upper()
while selection != "Q":
    if selection == "H":
        print("Hello", name)
    elif selection == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(menu)
    selection = input().upper()
print("Finished.")
