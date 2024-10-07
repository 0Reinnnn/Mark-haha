user = int(input("what number you want to append ? "))

storage_number = []

for i in range(user):
    number = int(input("Enter a number : "))
    storage_number.append(number)

for get_number in storage_number:
    print(get_number , end= " ")

