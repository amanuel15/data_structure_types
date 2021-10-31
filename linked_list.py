class Node():
    def __init__(self,data,nxt=None):
        self.data = data
        self.nxt = nxt

    

class LinkedList():
    def __init__(self):
        self.head = Node('Head',None)
    
    def push_front(self,key):
        node = Node(key)
        node.nxt = self.head.nxt
        self.head.nxt = node
        
    
    def top_front(self):
        return self.head.nxt 

    
    def push_back(self,key):
        node = Node(key)
        for n in self:
            if n.nxt == None:
                n.nxt = node
                node.nxt = None

    

    def empty(self):
        return self.head == None
                      
    def find(self,key):
        for a in self:
            if a.data == key:
                return True
        return False


    def erase(self,key):
        prv = self.head
        for a in self:
            if a.data == key:
                prv.nxt = a.nxt
            prv = prv.nxt

    def __iter__(self):
        cur_node = self.head.nxt
        while(cur_node != None):
            yield cur_node
            cur_node = cur_node.nxt
    


def __test__():
    link = LinkedList()
    link.push_front('A')
    link.push_front('B')
    link.push_back('D')
    link.push_front('C')
    link.erase('B')
    print(link.find('B'))
    for a in link:
        print(a.data)




if __name__ == '__main__':
    __test__()
