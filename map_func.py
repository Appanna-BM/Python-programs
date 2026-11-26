#converting cost of prod to euros 
store=[("shirts",9.00),
       ("Pants",12.00),
       ("Jacket", 13.00)]
to_euros=lambda data:(data[0], data[1]*0.82)
store_euros=list(map(to_euros, store))
for i in store_euros:
    print(i)