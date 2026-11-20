#break: used  to terminate loop entirely
#continue: skips to the next iteration of the loop
#pass: does nothing, acts as a placeholder

#while True:
    #name=input("Enter your name :")
    #if name != "_":
        #break

ph_no="+91-96000000000"
for i in ph_no:
    if i=="-":
        continue
    print(i, end="")