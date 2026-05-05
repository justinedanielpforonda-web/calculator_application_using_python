def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

loop = True

while loop:
    print("-" * 50)
    print("calculator".center(50))
    print("-" * 50)

    print("Operation please")
    print(" Addtion        (1)\n",
        "Substraction   (2)\n",
        "Multiplication (3)\n",
        "Division       (4)\n",
        "Exit           (5)\n")
    
    user_num = input("Enter here: ")
    if user_num == "5":
            print("Goodbye!")
            break

    clear()
    try:
        num1 = float(input("Enter you 1st number please: "))
        num2 = float(input("Enter your 2nd number please: "))
    except ValueError:
        print("Please Enter number that 1-5")
        break

    answer = None

    if user_num == "1":
        answer = num2 + num1
    elif user_num == "2":
        answer = num1 - num2
    elif user_num == "3":
        answer = num1 * num2
    elif user_num == "4":
        answer = None
        try:
            answer = num1 / num2
        except ZeroDivisionError:
            choice = input("\nDo you want to continue? (y/n): ").lower()

        if choice != 'y':
            running = False
            print("Goodbye!")
            continue
    else:
        print("invalid operation\n")
        continue
    
    print("Answer: ",answer)
    input("Press enter to Continue")

    clear()
