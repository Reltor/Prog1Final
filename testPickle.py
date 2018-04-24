import pickle

class Test(object):
    def __init__(self,var,var2,var3):
        self.var1 = var
        self.var2 = var2
        self.var3 = var3

class Obj(object):
    def __init__(self,var,var2,var3):
        self.var1 = var
        self.var2 = var2
        self.var3 = var3
myList = []
for num in range(1,10):
    myList.append(Obj(Test(1,2,3),Test(1,2,3),Test(1,2,3)))
pickle_out = open("testfile.xyz","wb")
pickle.dump(myList,pickle_out)
pickle_out.close()


pickle_in = open("testfile.xyz","rb")
myList = pickle.load(pickle_in)
print(myList[0].var1.var1)
if myList[0] isinstance(Test):
    print("2")
