f = open("AOC22Day2.txt", "r")

input_data = list(f)
compare_list = []
score_count = 0

lookup_dict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

for element in input_data:
    x = lookup_dict.get(element.strip())
    score_count +=x
    
print(score_count)