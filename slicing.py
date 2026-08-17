#slicing: creating a substring by extracting elements from another string

name = "Shahin Appanna"
f=name[0]
print(f)
f1=name[0:3]
print(f1)
f2=name[:3]
print(f2)
f3=name[7:]
print(f3)
f4=name[0:14:2]
print(f4)
f5=name[::-1]
print(f5)

website="http://google.com"
website2="http://wikipedia.com"
slice=slice(7,-4)
print(website[slice])
print(website2[slice])