squares=[i+1 for i in range(1,11)]
print(squares)

stds=[100,90,80,70,60,50,40,30,0]
#passes_std=[i for i in stds if i>=60]
passes_std=[i if i>=60 else "Fail" for i in stds if i>=60]  
print(passes_std)                                                