# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class List_1:
#     def __init__(self, data):
#         new_node = Node(data)
#         self.start_node = new_node

#     def print_l(self):
#         if self.start_node is None:
#             print("Список пуст")
#             return
            
#         n = self.start_node
#         while n is not None:
#             print(n.data, end = " ")
#             n = n.next
#         print()
    
#     def insert_start(self, data):
#         new_node = Node(data)
#         new_node.next = self.start_node
#         self.start_node = new_node

#     def insert_end(self, data):
#         new_node = Node(data)
#         n = self.start_node
#         while n.next:
#             n = n.next
#         n.next = new_node

#     def delete_start(self):
#         if self.start_node is None:
#             print("Список пуст")
#             return
        
#         self.start_node = self.start_node.next

#     def delete_end(self):
#         if self.start_node is None:
#             print("Список пуст")
#             return

#         n = self.start_node
#         if n.next:
#             while n.next.next:
#                 n = n.next
#             n.next = None
#         else:
#             self.start_node = self.start_node.next
         
#     def search(self, x):
#         n = self.start_node
#         while n is not None:
#             if n.data == x:
#                 return True
#             n = n.next
#         return False

# l1 = List_1(4)
# l1.insert_start(3)
# l1.insert_start(2)
# l1.insert_end(5)
# l1.print_l()
# l1.delete_start()
# l1.print_l()
# l1.delete_end()
# l1.print_l()
# print(l1.search(3))
# print(l1.search(10))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List_2:
    def __init__(self):
        self.start_node = None

    def print_l(self):
        if self.start_node is None:
            print("Список пуст")
            return   
        n = self.start_node
        while n is not None:
            print(n.data, end = " ")
            n = n.next
        print()
    
    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def delete_start(self):
        if self.start_node is None:
            print("Список пуст")
            return
        
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_end(self):
        if self.start_node is None:
            print("Список пуст")
            return

        n = self.start_node
        if n.next:
            while n.next.next:
                n = n.next
            n.next = None
        else:
            self.start_node = self.start_node.next
            self.start_node.prev = None
         
    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False
    
    def reverse_l(self):
        l = List_2()
        n = self.start_node
        while n is not None:
            l.insert_start(n.data)
            n = n.next
        return l   

    def sort(self):
        if self.start_node is None:
            print("Список пуст")
            return
        n = self.start_node
        n1 = self.start_node.next
        while n.next:
            while n1 is not None:
                if n.data < n1.data:
                    n.data, n1.data = n1.data, n.data
                n1 = n1.next
            n = n.next
            n1 = n.next

l2 = List_2()
l2.insert_start(1)
l2.insert_start(7)
l2.insert_end(8)
l2.insert_end(6)
l2.insert_start(5)
l2.insert_start(9)
l2.insert_end(3)
l2.insert_end(2)
l2.print_l()
l2.sort()
l2.print_l()
l2 = l2.reverse_l()
l2.print_l()
