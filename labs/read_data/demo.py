animal_list = open("fav_animals.txt")

data = animal_list.readlines()
print(data)
# string = "\n".join(data)
# new_data = string.split("\n")
# print(new_data)
for animal in data:
    print(animal.replace("\n", ""))
   
animal_list.close
