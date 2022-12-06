f = open("AOC22Day2.txt", "r")

input_data = list(f)
compare_list = []
score_count = 0

lookup_dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

for element in input_data:
    x = lookup_dict.get(element.strip())
    score_count +=x
    
print(score_count)