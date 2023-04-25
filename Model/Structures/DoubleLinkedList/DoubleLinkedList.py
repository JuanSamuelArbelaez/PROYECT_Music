class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
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
        node = self.__head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def add(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")

        new_node = Node(value)
        if index == 0:
            new_node.next = self.__head
            if self.__head is not None:
                self.__head.prev = new_node
            self.__head = new_node
        else:
            node = self.__head
            for i in range(index - 1):
                node = node.next
            new_node.next = node.next
            new_node.prev = node
            if node.next is not None:
                node.next.prev = new_node
            node.next = new_node

        self.__size += 1
        self.__sorted = False

    def append(self, value):
        self.add(self.__size, value)

    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")

        if index == 0:
            node = self.__head
            self.__head = node.next
            if self.__head is not None:
                self.__head.prev = None
        else:
            node = self.__head
            for i in range(index):
                node = node.next
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev

        self.__size -= 1

    def remove_value(self, value):
        node = self.__head
        index = 0
        while node is not None:
            if node.value == value:
                self.remove(index)
                return True
            node = node.next
            index += 1
        return False

    def poll(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")

        node = self.__head
        for i in range(index):
            node = node.next

        self.remove(index)

        return node.value

    def sort(self):
        values = []
        node = self.__head
        while node is not None:
            values.append(node.value)
            node = node.next

        values.sort()

        self.clear()

        for value in values:
            self.append(value)

        self.__sorted = True

    def insert(self, value):
        if not self.__sorted:
            raise ValueError("List must be sorted to use insert method")

        node = self.__head
        index = 0
        while node is not None:
            if value <= node.value:
                self.add(index, value)
                return
            node = node.next
            index += 1

        self.append(value)

    def add_all(self, other_list):
        for value in other_list:
            self.append(value)

        self.__sorted = False

    def clear(self):
        self.__head = None
        self.__size = 0

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")

        node = self.__head
        for i in range(index):
            node = node.next

        return node.value

    def index_of(self, value):
        node = self.__head
        index = 0
        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return -1

    def last_index_of(self, value):
        node = self.__head
        index = 0
        last_index = -1
        while node is not None:
            if node.value == value:
                last_index = index
            node = node.next
            index += 1
        return last_index

    def valid_index(self, index):
        return 0 <= index < self.__size

    def sub_list(self, start, end):
        if start < 0 or start >= self.__size:
            raise IndexError("Start index out of range")

        if end < 0 or end > self.__size:
            raise IndexError("End index out of range")

        if start > end:
            raise ValueError("Start index cannot be greater than end index")

        new_list = DoubleLinkedList()
        node = self.__head
        for i in range(start):
            node = node.next
        for i in range(start, end):
            new_list.append(node.value)
            node = node.next
        return new_list

    def remove_all(self, other_list):
        node = other_list._head
        while node is not None:
            self.remove_value(node.value)
            node = node.next

    def append_list(self, other_list):
        node = other_list._head
        while node is not None:
            self.append(node.value)
            node = node.next

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node.value
            node = node.next

