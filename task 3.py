storage_user = [20,30,40,50,]
user = input(f"choose what to remove to delete one value of array (storage_user) (index or name) ? ").lower()

if user == "index":
    index = int(input("Enter a index number for remove the value of array : "))
    storage_user.pop(index)
elif user == "name": 
    name = input("Enter a name to remove the value")
    storage_user.remove(name)
else:
    print("there no choices")

print(storage_user)