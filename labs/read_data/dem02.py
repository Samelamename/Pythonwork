file = open("fnew_file.txt", "w")

for x in range(10):
    new_line = f"Line numbe: {x +1 }\n"
    file.write(new_line)

file.close


