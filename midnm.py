num1 = input("Please enter the first number: \n ")
num2 = input("Please enter the second number: \n ")
num3 = input("Please enter the third number: \n ")

print("In These three numbers The middle number is: \n ")

if num2 < num1 and num1 < num3:
    print(num1)

elif num3 < num1 and num1 < num2:
    print(num1)

elif num3 < num2 and num2 < num1:
    print(num2)

elif num1 < num2 and num2 < num3:
    print(num2)

elif num2 < num3 and num3 < num1:
    print(num3)

elif num1 < num3 and num3 < num2:
    print(num3)

else:
    print("Incorrect value, Error")
