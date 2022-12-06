f = open("AOC22.txt", "r")

input_data = list(f)

output_list = []

calorie_count =[]

for element in input_data:
    if element == '\n':
        calorie_count.append(sum(output_list))
        output_list.clear()
        continue
    value = int(element)
    output_list.append(value)
    
calorie_count.sort()
print("The calorie count for the highest carrying elf is: " + str(calorie_count[-1]))