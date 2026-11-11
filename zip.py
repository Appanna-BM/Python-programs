from itertools import zip_longest
color = ["red","green"]
items=["apple","grapes","pineapple"]
for c , i in zip_longest(color, items, fillvalue="unknown"):
    print(f"{c}:{i}")