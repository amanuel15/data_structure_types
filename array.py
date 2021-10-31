class Array():
    def __init__(self,size,data_type):
        self.size=size
        self.data_type = data_type
        self.cur_array = [None]*size
        self.last_index = 0
       
    
    def insert(self,value,position=None):
        assert isinstance(value,self.data_type)
        position = self.last_index if position == None else position
        if self.last_index != position:
            final_position = self.last_index if position != self.size-1 else self.last_index-1
            self.__shift__(position,final_position)

        self.last_index += 1
        self.cur_array[position] = value

    def delete(self,position):
        assert position < self.size
        for i in range(position,self.last_index):
            self.cur_array[i] = self.cur_array[i+1]
        self.last_index-=1
        self.cur_array[self.last_index] = None
        
      
    def __shift__(self,pos_i,pos_j,shift_right=True):
        for i in range(pos_j,pos_i-1,-1):
            self.cur_array[i+1] = self.cur_array[i]

    def __iter__(self):
        for i in self.cur_array:
            yield i

    def __str__(self):
        return str(self.cur_array)


def __test__():
    a = Array(5,int)
    a.insert(5)
    a.insert(3)
    print(a)
    a.insert(34,2)
    a.insert(1,2)
   
    print(a)
    a.delete(2)
    print(a)
    

if __name__ == '__main__':
    __test__()
