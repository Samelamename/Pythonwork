data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

new_data = data.split(",")

print(new_data)


int_data = []

for num in new_data:
    int_data.append(int(num))



minimum = min(int_data)
maximum = max(int_data)

print("Minimum:",minimum)
print("Maximum:",maximum)