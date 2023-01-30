car_file = open("cars.csv")
months = car_file.readline() # Moving the cursor past the months
car_data = car_file.readlines()

for line in car_data:
    row = line.strip().split(',')
    if row[0] == 'Ford Motor Company':
        cars = []
        for i in row[1:]:
            cars.append(int(i.strip('"')))  
        sum_of_cars = sum(cars)
        break

car_file.close()
print(sum_of_cars)
