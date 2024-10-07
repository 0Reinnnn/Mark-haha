array_number = [10,20,30,40,50]

user = input("Do you want to clear the list (yes or no) ? ").lower()

if user == "yes":
    array_number.clear()
elif user == "no":
    print("Unchange the array_number")
else:
    print("Invalid Choices")

print("the Result : " + str(array_number))