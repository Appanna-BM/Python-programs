import time
#print(time.ctime(0))             

'''
print(time.ctime(1000))
print(time.time())

time_obj=time.localtime()

time_obj1=time.gmtime()#if you need utc time

print(time_obj)
local_time = time.strftime("%B %d %y %H:%M:%S", time_obj)
print(local_time)
'''

time_tuple=(2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.asctime(time_tuple)
print(time_string)                                                            

time_tuple=(2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.mktime(time_tuple)
print(time_string)  