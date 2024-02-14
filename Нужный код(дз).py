class LinkedList:
    
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None
    
    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            self.head.value = value
            return
        
        while current.next:
            current = current.next
        
        item = LinkedList.Item(value)
        current.next = item


    def append_by_index(self, value, index):
        item = LinkedList.Item(value)
        current = self.head
        n=0
        while current is not None and n!=index -1:
            current = current.next
            n+=1
        item.next=current.next
        current.next=item
        
        
        
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print() 

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count 
    
    def remove_first(self):
        if self.head is None:
            raise ValueError("Список пуст")
        self.head = self.head.next
    
    def remove_last(self):
        if self.head is None:
            raise ValueError("Список пуст")
        if self.head.next is None:
            self.head = None
            return 
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if self.head is None:
            raise ValueError("Список пуст")
        
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Индекс вне диапазона")

        prev.next = current.next

    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Список пуст")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None

        while current and current.value != value:
            prev = current
            current = current.next

        if current is None:
            raise ValueError("Значение не найдено")

        prev.next = current.next

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("Список пуст")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        last_match = None

        while current:
            if current.value == value:
                last_match = current
            prev = current
            current = current.next

        if last_match is None:
            raise ValueError("Значение не найдено")

        prev.next = last_match.next
    

my_list = LinkedList()
my_list.append_begin(14)
my_list.append_begin(58)
my_list.append_begin(60)
my_list.append_begin(100)
my_list.append_begin(69)

my_list.append_by_index(2, 2)
my_list.append_by_index(7, 1)

my_list.print_list()

print(len(my_list))
my_list.remove_first()
my_list.remove_last()
my_list.remove_at(1)
my_list.remove_first_value(2)
my_list.remove_last_value(7)

my_list.print_list()



