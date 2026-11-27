import threading
import time

#below 3 methods are io bound because they are waiting for time to expire to execute the task
#we are doing it sequentially not concurrently
#now we have 1 thread that is handling all these 3 methods/tasks.
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink Coffee")

def study():
    time.sleep(5)
    print("You finish studying")

#creating additinal thread so that main  thread can handel own set of instruction that it has to execute and not responsible for executing the methods.
#we pass in tup for args , no we have no args no nothing passed
# now x thread handles the eat_breakfast() method
#after this well have 4 threads running concurrently..
x=threading.Thread(target=eat_breakfast, args=())
x.start() 

y=threading.Thread(target=drink_coffee, args=())
y.start()

z=threading.Thread(target=study, args=())
z.start()

#thread synch  ronization
#x.join()
#y.join()
#z.join()

#sequential execution with below calling methods as only one thread handles execution of everything.
#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())#shows count of active thread..
print(threading.enumerate()) #list of all running thread..
print(time.perf_counter()) #shows how long will the main thread took to execute the set of instructions..
