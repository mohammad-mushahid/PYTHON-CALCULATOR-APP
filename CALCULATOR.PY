print("====SIMPLE CALCULATOR ====")
print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.divide")

choice = input("Enter the choice: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second numbert: "))

if choice == "1":
    print("Result =",a + b)

elif choice == "2":
    print( a - b)

elif choice == "3":
    print(a * b)
else:
    print("invalid choice")