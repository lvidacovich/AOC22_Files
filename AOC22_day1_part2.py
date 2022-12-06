def compare(compare_list_element, score_count):
    for element in compare_list_element:
        if element.str == 'X':
            score_count +=1
        if element.str == 'Y':
            score_count +=2
        if element.str == 'Z':
            score_count +=3
        


f = open("AOC22Day2.txt", "r")

input_data = list(f)
compare_list = []
score_count = 0

for element in input_data:
    compare_list.append(element.split(" "))
    
for element in compare_list:
    compare(element)
    

# output_list = []

# calorie_count =[]

# for element in input_data:
#     if element == '\n':
#         calorie_count.append(sum(output_list))
#         output_list.clear()
#         continue
#     value = int(element)
#     output_list.append(value)
    
# calorie_count.sort()

# top_3 = []

# top_3.append(calorie_count[-1])
# top_3.append(calorie_count[-2])
# top_3.append(calorie_count[-3])

# top_3_calories = sum(top_3)

# print("The calorie count for the highest carrying 3 elves is: " + str(top_3_calories))