print("-" * 50)
print("calculator".center(50))
print("-" * 50)

print("Operation please")
print(" Addtion (1)\n",
      "Substraction(2)\n",
      "Multiplication (3)\n",
      "Division (4)\n")
user_num = input("Enter here: ")

num1 = float(input("Enter you 1st number please: "))
num2 = float(input("Enter your 2nd number please: "))

if user_num == "1":
    answer = num2 + num1
elif user_num == "2":
    answer = num1 - num2
elif user_num == "3":
    answer = num1 * num2
elif user_num == "4":
    answer = num1/num2

print(answer)