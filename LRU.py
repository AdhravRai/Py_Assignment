class Node:
    def __init__(self,k=0,value=0):
        self.k=k
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def add_to_front(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    def get(self,k):
        if k not in self.cache:
            return -1
        node=self.cache[k]
        self.remove(node)
        self.add_to_front(node)
        return node.value
    def put(self,k,value):
        if self.capacity==0:
            return
        if k in self.cache:
            node=self.cache[k]
            node.value=value
            self.remove(node)
            self.add_to_front(node)
            return
        if len(self.cache)==self.capacity:
            lru_node=self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.k]
        new_node=Node(k,value)
        self.cache[k]=new_node
        self.add_to_front(new_node)
if __name__=='__main__':
    lru = LRUCache(2)
    lru.put(1, 10)
    lru.put(2, 20)
    print(lru.get(1))
    lru.put(3, 30)   
    print(lru.get(2))
    print(lru.get(3))
    lru.put(1, 15)   
    print(lru.get(1))