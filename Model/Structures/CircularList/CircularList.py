class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.__size = 0
        self.__sorted = False
        self.__head = None

    def size(self):
        return self.__size

    def is_sorted(self):
        return self.__sorted

    def is_empty(self):
        return self.__size == 0

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

    def remove_value(self, value):
        current = self.__head
        for i in range(self.__size):
            if current.value == value:
                self.remove(i)
                return True
            current = current.next
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

    def sort(self):
        if not self.__sorted:
            node_list = []
            current = self.__head
            for i in range(self.__size):
                node_list.append(current)
                current = current.next
            node_list.sort(key=lambda x: x.value)
            self.__head = node_list[0]
            current = self.__head
            for i in range(self.__size - 1):
                current.next = node_list[i + 1]
                current = current.next
            current.next = self.__head
            self.__sorted = True

    def insert(self, value):
        if self.__sorted:
            current = self.__head
            index = 0
            while index < self.__size and current.value <= value:
                current = current.next
                index += 1
            self.add(index, value)
        else:
            raise Exception("Cannot insert into unsorted list")

    def add_all(self, other):
        for value in other:
            self.append(value)

    def clear(self):
        self.__head = None
        self.__size = 0
        self.__sorted = False

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
        sub_list = CircularLinkedList()
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
        return removed_count

    def append_list(self, other):
        if other is None or other.is_empty():
            return
        current = other.__head
        for i in range(other.__size):
            self.append(current.value)
            current = current.next

    def iterator(self):
        current = self.__head
        while True:
            yield current.value
            current = current.next
            if current == self.__head:
                break
