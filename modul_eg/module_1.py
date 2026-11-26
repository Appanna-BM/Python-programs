'''
if __name__ == '__main__':
    print("Running this module directly")
else:
    print("Running other module indirectly")
'''
def hello():
    print("This is module 1")

if __name__=='__main__':
    hello()