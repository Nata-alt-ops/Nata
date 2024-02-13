
class LinkedList:

    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    def __init__(self):
        self.head = None
    
    def append_begin(self, value):
        item = self.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = self.Item(value)
            return
        
        while current.next:
            current = current.next
        
        item = self.Item(value)
        current.next = item


    def append_by_index(self, value, index):
        if self.head is None:
            self.head = self.Item(value)
            return

        if index <= 0:
            item = self.Item(value)
            item.next = self.head
            self.head = item
            return

        current = self.head
        counter = 0
        while current.next and counter < index - 1:
            current = current.next
            counter += 1
        
        item = self.Item(value)
        item.next = current.next
        current.next = item

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head is None:
            raise ValueError("список пуст")
        
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("список пуст")

        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if self.head is None:
            raise ValueError("удаление невозможно")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        counter = 0
        while current and counter < index:
            current = current.next
            counter += 1
        
        if not current or not current.next:
            raise ValueError("Индекс вне диапазона")

        current.next = current.next.next

    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Значение не найдено")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError("значение не найдено в списке")

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("значение не найдено")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current.next:
            if current.next.value == value:
                prev = current
            current = current.next
        
        if prev:
            prev.next = prev.next.next
            return
        
        raise ValueError("Значение не найдено в списке")
my_list = LinkedList()
my_list.append_begin(4)
my_list.append_begin(5)
my_list.append_begin(6)
my_list.append_begin(56)
my_list.append_begin(59)
my_list.append_begin(23)
my_list.append_begin(100)
print(len(my_list))
my_list.remove_first()
my_list.remove_last()
my_list.remove_at(0)
my_list.remove_first_value(5)
my_list.remove_last_value(10)