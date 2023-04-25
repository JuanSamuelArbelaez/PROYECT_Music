class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularList:
    def __init__(self):
        self.__sorted_by = None
        self.__size = 0
        self.__sorted = False
        self.__head = None

    def size(self):
        return self.__size

    def is_sorted(self):
        return self.__sorted

    def is_empty(self):
        return self.__size == 0

    def get_sort_key(self):
        return self.__sorted_by

    def contains(self, value):
        current = self.__head
        for i in range(self.__size):
            if current.value == value:
                return True
            current = current.next
        return False

    def add(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index == 0:
            if self.__head is None:
                new_node.next = new_node
                self.__head = new_node
            else:
                new_node.next = self.__head
                current = self.__head
                while current.next != self.__head:
                    current = current.next
                current.next = new_node
                self.__head = new_node
        else:
            current = self.__head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.__size += 1
        self.__sorted = False

    def append(self, value):
        self.add(self.__size, value)

    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        if index == 0:
            if self.__size == 1:
                self.__head = None
            else:
                current = self.__head
                while current.next != self.__head:
                    current = current.next
                self.__head = self.__head.next
                current.next = self.__head
        else:
            current = self.__head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.__size -= 1
        self.__sorted = False

    def remove_value(self, value):
        current = self.__head
        for i in range(self.__size):
            if current.value == value:
                self.remove(i)
                return True
            current = current.next
            self.__sorted = False
        return False

    def poll(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        current = self.__head
        for i in range(index - 1):
            current = current.next
        value = current.next.value
        self.remove(index)
        return value

    def sort(self, key=None):
        if self.__sorted and self.__sorted_by == key:
            return

        if key is None:
            key = lambda x: x

        # convert string key to attribute getter function
        if isinstance(key, str):
            key = lambda x: getattr(x, key)
        else:
            raise AttributeError("Attribute {key} not found")

        # convert list to tuple to prevent modification during sorting
        nodes = tuple(self)

        # use key function to sort nodes
        nodes = sorted(nodes, key=key)

        # rebuild list from sorted nodes
        self.__head = None
        for node in nodes:
            self.append(node.value)

        self.__sorted = True
        self.__sorted_by = key if not isinstance(key, str) else None

    def insert(self, value):
        if self.__sorted:
            current = self.__head
            index = 0
            while index < self.__size and current.value <= value:
                current = current.next
                index += 1
            self.add(index, value)
            self.__sorted = False
        else:
            raise Exception("Cannot insert into unsorted list")

    def add_all(self, other):
        for value in other:
            self.append(value)

    def clear(self):
        self.__head = None
        self.__size = 0
        self.__sorted = False
        self.__sorted_by = None

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        current = self.__head
        for i in range(index):
            current = current.next
        return current.value

    def index_of(self, value):
        current = self.__head
        for i in range(self.__size):
            if current.value == value:
                return i
            current = current.next
        return -1

    def last_index_of(self, value):
        current = self.__head
        last_index = -1
        for i in range(self.__size):
            if current.value == value:
                last_index = i
            current = current.next
        return last_index

    def valid_index(self, index):
        return 0 <= index < self.__size

    def sub_list(self, start, end):
        if start < 0 or end > self.__size or start >= end:
            raise ValueError("Invalid start or end index")
        sub_list = CircularList()
        current = self.__head
        for i in range(start):
            current = current.next
        for i in range(start, end):
            sub_list.append(current.value)
            current = current.next
        return sub_list

    def remove_all(self, value):
        current = self.__head
        prev = None
        removed_count = 0
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.__head = current.next
                else:
                    prev.next = current.next
                self.__size -= 1
                removed_count += 1
            else:
                prev = current
            current = current.next
            self.__sorted = False
        return removed_count

    def append_list(self, other):
        if other is None or other.is_empty():
            return
        current = other.__head
        for i in range(other.__size):
            self.append(current.value)
            current = current.next

    def __iter__(self):
        current = self.__head
        while True:
            yield current.value
            current = current.next
            if current == self.__head:
                break
