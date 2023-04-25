class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.__size = 0
        self.__top = None

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def contains(self, value):
        current = self.__top
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.__top
        self.__top = new_node
        self.__size += 1

    def poll(self):
        if self.__top is None:
            return None
        value = self.__top.value
        self.__top = self.__top.next
        self.__size -= 1
        return value

    def remove(self, value):
        prev = None
        current = self.__top
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.__top = current.next
                else:
                    prev.next = current.next
                self.__size -= 1
                return True
            prev = current
            current = current.next
        return False

    def peek(self):
        if self.__top is None:
            return None
        return self.__top.value

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.__top
            self.__top = new_node
        else:
            current = self.__top
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.__size += 1

    def add_all(self, iterable):
        for value in iterable:
            self.push(value)

    def clear(self):
        self.__size = 0
        self.__top = None

    def index_of(self, value):
        current = self.__top
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def last_index_of(self, value):
        current = self.__top
        index = -1
        last_index = -1
        while current is not None:
            if current.value == value:
                last_index = index
            current = current.next
            index += 1
        return last_index

    def valid_index(self, index):
        return 0 <= index < self.__size

    def sub_list(self, start, end=None):
        if start < 0 or start >= self.__size:
            raise IndexError("Start index out of range")
        if end is None:
            end = self.__size
        if end < 0 or end > self.__size:
            raise IndexError("End index out of range")
        if start > end:
            raise IndexError("Start index greater than end index")
        result = Stack()
        current = self.__top
        for i in range(end):
            if i >= start:
                result.push(current.value)
            current = current.next
        return result

    def remove_all(self, iterable):
        count = 0
        for value in iterable:
            while self.remove(value):
                count += 1
        return count

    def append_list(self, iterable):
        for value in iterable:
            self.push(value)

    def __iter__(self):
        current = self.__top
        while current is not None:
            yield current.value
            current = current.next
