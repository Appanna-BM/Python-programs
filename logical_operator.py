temp=int(input("Enter the temperature outside ?:"))
if not(temp>=0 and temp<=30):
    print("The temp is bad outside")
    print("stay inside")
elif not(temp<0 or temp>30):
    print("The temp is Good outside")
    print("Go outside")
