class Myclass:
    def __del__(self):
        print("DELETED!!")


import sys
b1 = Myclass()  
b2 = b1
print("ref to b2",sys.getrefcount(b2)) # no. of ref to b2 + 1 
del b2 # deduce ref by 1
print("did __del__ got called ?") # object doesn't delete as ref not equal to 0
print("ref to b1",sys.getrefcount(b1)) 
del b1 # ref equal to zero hence __del__ is called 
# program ends so all existing objects get deleted. automatically __del__ is called even if above line not there.
