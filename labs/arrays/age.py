#############################################################################################################################################################################################################################################################################################################################################################################
#############################################################################################################################################################################################################################################################################################################################################################################
#Prints ages and manipulates it.
ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
length = len(ages)
print(length)
#Display all of the numbers in the list line by line using some form of loop
for age in ages: 
    print(age)
print("##################################")
#Looping through the list, increase the value of each age by 1
for i in range(len(ages)):
    ages[i] += 1
print(ages)
print("##################################")
# Create a new list which only contains the ages in the age range of 16 – 65, display the new list and confirm it only contains 16 – 65 year olds
new_list = [age for age in ages if age >= 16 and age <= 65]
print(new_list)
print("##################################")
# 5)	Display the count of 16 – 25 year olds in the new list
count = 0
for age in new_list:
    if age >= 16 and age <= 25:
        count += 1
print(count)
print("##################################")
# Sort the ages of the new list 
new_list.sort()
print("##################################")
# proportion of people belong in the 16 – 25 category within the new list
proportion = count / len(new_list)
print(proportion)

