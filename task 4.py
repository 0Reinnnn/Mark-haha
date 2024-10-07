storage=["jay","baldo","albert","arvin"]

user = input("user choice either sort the list alphabetically or reverse (sort or reverse) : ").lower()
             
if user == "sort" :
    storage.sort()
    print(storage)
elif user== "reverse" :
    storage.reverse()
    print(storage)
else :
    print("invalid choices")