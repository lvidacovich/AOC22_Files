import difflib
import pandas as pd

f = open("AOC22Day3.txt", "r")

input_data = list(f)
matching_items = []
priority_count = 0

column_names=["Index","Matching Letter","comp1", "comp2","Whole String"]
df=pd.DataFrame(data=None,columns=column_names)

splits = [input_data[i:i+3] for i in range(0,len(input_data),3)]

for i in splits:
    print(i)
    
for element in input_data:
    comp1 = (element[0:half])
    comp2 = (element[half:])
    seq = difflib.SequenceMatcher(None, comp1, comp2)
    for block in seq.get_matching_blocks():        
        if block[2] == 1:
            end = (block[0]+1)
            matching_items.append(comp1[block[0]:end])
            new_row = [input_data.index(element), (comp1[block[0]:end]), comp1, comp2, element]
            df.loc[len(df)] = new_row
            continue
        if block[2] == 2:
            end = (block[0]+1)
            matching_items.append(comp1[block[0]:end])
            new_row = [input_data.index(element), (comp1[block[0]:end]), comp1, comp2, element]
            df.loc[len(df)] = new_row
            continue
        if block[2] == 3:
            end = (block[0]+1)
            matching_items.append(comp1[block[0]:end])
            new_row = [input_data.index(element), (comp1[block[0]:end]), comp1, comp2, element]
            df.loc[len(df)] = new_row
            continue
        else:
            continue

df = df.drop_duplicates(subset=['Whole String'])

col_list = df["Matching Letter"].values.tolist()

for i in col_list:
    if i.isupper():
        priority_count += (ord(i) - 38)
    else:
        priority_count += (ord(i) - 96)