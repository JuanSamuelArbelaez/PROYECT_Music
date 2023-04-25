class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def contains(self, value):
        current = self.__head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def push(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = node
        self.__size += 1

    def poll(self):
        if self.__head is None:
            raise IndexError("Queue is empty")
        value = self.__head.value
        self.__head = self.__head.next
        self.__size -= 1
        return value

    def remove(self, value):
        if self.__head is None:
            raise ValueError("Value not found")
        if self.__head.value == value:
            self.__head = self.__head.next
            self.__size -= 1
            return
        current = self.__head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.__size -= 1
                return
            current = current.next
        raise ValueError("Value not found")

    def peek(self):
        if self.__head is None:
            raise IndexError("Queue is empty")
        return self.__head.value

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        if index == 0:
            node = Node(value)
            node.next = self.__head
            self.__head = node
            self.__size += 1
            return
        current = self.__head
        for i in range(index - 1):
            current = current.next
        node = Node(value)
        node.next = current.next
        current.next = node
        self.__size += 1

    def add_all(self, values):
        for value in values:
            self.push(value)

    def clear(self):
        self.__size = 0
        self.__head = None

    def index_of(self, value):
        current = self.__head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise ValueError("Value not found")

    def last_index_of(self, value):
        current = self.__head
        index = -1
        i = 0
        while current:
            if current.value == value:
                index = i
            current = current.next
            i += 1
        if index == -1:
            raise ValueError("Value not found")
        return index

    def valid_index(self, index):
        return 0 <= index < self.__size

    def sub_queue(self, start_index, end_index):
        if start_index < 0 or end_index > self.__size or start_index > end_index:
            raise IndexError("Index out of range")
        current = self.__head
        for i in range(start_index):
            current = current.next
        result = Queue()
        for i in range(start_index, end_index):
            result.push(current.value)
            current = current.next
        return result

    def remove_all(self, values):
        current = self.__head
        previous = None
        count = 0
        while current:
            if current.value in values:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                count += 1
                self.__size -= 1
            else:
                previous = current
            current = current.next
        return count

    def append_queue(self, other):
        for value in other:
            self.push(value)

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
