class node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.pre = None
class  link:
    def __init__(self):
        self.head = None
    def insert(self,v):
        new = node(v)
        if self.head is None:
            self.head = new
            new.next = self.head
            new.pre = None
        else:
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = new
            new.pre = temp
            new.next = self.head
    def show(self):
        lst = []
        temp = self.head
        v = self.head.data
        while temp.next!=self.head:
            lst.append(temp.data)
            temp = temp.next
        lst.append(temp.data)
        print(lst)
    def rshow(self):
        lst = []
        temp = self.head
        v = self.head.data
        while temp.next!=self.head:
            lst.append(temp.data)
            temp = temp.next
        lst.append(temp.data)
        lst.reverse()
        print(lst)
    def hinsert(self,v):
        new = node(v)
        if self.head is None:
            self.head = new
            new.next = self.head
            new.pre = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            p = temp
            p.next = new
            new.pre = p
            new.next = self.head
            self.head.pre = new
            self.head = new
    def d(self, v):
        temp = self.head
        if self.head.data == v:
            while temp.next.data != v:
                temp = temp.next
            p = temp
            n = self.head.next
            p.next = n
            n.pre = p
            self.head = n

        else:
            temp = self.head
            while temp.next.data != v:
                temp = temp.next
            p = temp
            t = self.head
            while t.pre.data != v:
                t = t.next
            n = t
            p.next = n
            n.pre = p



print()
print("Circular Linked List Created")
n = link()
print()
print("Insert node 10 at end of Circular Linked List ")
n.insert(10)
n.show()
print()
print("Insert node 20 at end of Circular Linked List ")
n.insert(20)
n.show()
print()
print("Insert node 30 at end of Circular Linked List ")
n.insert(30)
n.show()
print()
print("Insert node 40 at end of Circular Linked List ")
n.insert(40)
n.show()
print()
print("Reverse Circular Linked List ")
n.rshow()
print()
print("Insert node 60 at beginning of Circular Linked List ")
n.hinsert(60)
n.show()
print()
print("Insert node 70 at beginning of Circular Linked List ")
n.hinsert(70)
n.show()
print()
print("Insert node 80 at beginning of Circular Linked List ")
n.hinsert(80)
n.show()
print()
print("Deleted Node 30 from Circular Linked List")
n.d(30)
n.show()
print()
print("Deleted Node 40 from Circular Linked List")
n.d(40)
n.show()
print()
print("Deleted Node 80 from Circular Linked List")
n.d(80)
n.show()
print()
print("Deleted Node 70 from Circular Linked List")
n.d(70)
n.show()
print()
print("Deleted Node 20 from Circular Linked List")
n.d(20)
n.show()






