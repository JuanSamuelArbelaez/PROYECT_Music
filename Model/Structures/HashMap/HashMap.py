from typing import TypeVar, Generic

from Model.Structures.ComparableValue.ComparableValue import ComparableValue

T = TypeVar('T', bound=ComparableValue)


class Node(Generic[T]):
    def __init__(self, key, value: T, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


class HashMap(Generic[T]):
    DEFAULT_CAPACITY = 16
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity=DEFAULT_CAPACITY, load_factor=DEFAULT_LOAD_FACTOR):
        self.size = 0
        self.capacity = capacity
        self.load_factor = load_factor
        self.table = [None] * capacity

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def contains_value(self, value: T):
        for node in self.table:
            while node is not None:
                if node.value == value:
                    return True
                node = node.next
        return False

    def contains_key(self, key):
        index = self.hash_of(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False

    def put_in(self, key, value: T):
        index = self.hash_of(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node[T](key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        if self.size > self.capacity * self.load_factor:
            self.resize()

    def get(self, key):
        index = self.hash_of(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self.hash_of(key)
        prev_node = None
        node = self.table[index]
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[index] = node.next
                else:
                    prev_node.next = node.next
                self.size -= 1
                return node.value
            prev_node = node
            node = node.next
        return None

    def hash_of(self, key):
        return hash(key) % self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        for node in self.table:
            while node is not None:
                index = hash(node.key) % new_capacity
                new_node = Node(node.key, node.value)
                new_node.next = new_table[index]
                new_table[index] = new_node
                node = node.next
        self.capacity = new_capacity
        self.table = new_table

    def add_all(self, other):
        for key in other:
            self.put(key, other[key])

    def clear(self):
        self.size = 0
        self.table = [None] * self.capacity

    def remove_all(self, other):
        for key in other:
            self.remove(key)

    def __iter__(self):
        for node in self.table:
            while node is not None:
                yield node.key
                node = node.next
