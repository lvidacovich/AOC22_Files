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

top_3 = []

top_3.append(calorie_count[-1])
top_3.append(calorie_count[-2])
top_3.append(calorie_count[-3])

top_3_calories = sum(top_3)

print("The calorie count for the highest carrying elf is: " + str(top_3_calories))