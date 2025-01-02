import ctypes

class meraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.n)
    def __len__(self):
        return self.n    
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
L = meraList()    