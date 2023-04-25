from typing import Generic, TypeVar, Union


T = TypeVar('T')
S = TypeVar('S', bound=Union['BinaryTree', 'CircularList', 'DoubleLinkedList', 'HashMap', 'LinkedList'])


class Node(Generic[T]):
    def __init__(self, value: T, next=None):
        self.value = value
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self):
        self._size = 0
        self._sorted = False
        self._head = None

    def size(self):
        return self._size

    def sorted(self):
        return self._sorted

    def isEmpty(self):
        return self._size == 0

    def contains(self, value: T):
        current = self._head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def add(self, index: int, value: T):
        if not self.validIndex(index):
            raise IndexError("Invalid index")
        if index == 0:
            self._head = Node(value, self._head)
        else:
            current = self._head
            for _ in range(index - 1):
                current = current.next
            current.next = Node(value, current.next)
        self._size += 1
        self._sorted = False

    def append(self, value: T):
        if self.isEmpty():
            self._head = Node(value)
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = Node(value)
        self._size += 1
        self._sorted = False

    def remove(self, index: int):
        if not self.validIndex(index):
            raise IndexError("Invalid index")
        if index == 0:
            self._head = self._head.next
        else:
            current = self._head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._size -= 1

    def remove_by_value(self, value: T):
        if self.isEmpty():
            return
        if self._head.value == value:
            self._head = self._head.next
            self._size -= 1
            return
        current = self._head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

    def poll(self, index: int):
        if not self.validIndex(index):
            raise IndexError("Invalid index")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def sort(self):
        if self.isEmpty():
            return
        self._head = self._merge_sort(self._head)
        self._sorted = True

    def _merge_sort(self, head: Node):
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
        return self._sorted_merge(left, right)

    def _sorted_merge(self, a: Node, b: Node):
        if not a:
            return b
        if not b:
            return a
        if a.value <= b.value:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    def _get_middle(self, head: Node):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def insert(self, value: T):
        if not self._sorted:
            raise ValueError("List is not sorted")
        if self.isEmpty() or self._head.value >= value:
            self._head = Node(value, self._head)
            self._size += 1
            return
        current = self._head
        while current.next and current.next.value < value:
            current = current.next
        current.next = Node(value, current.next)
        self._size += 1

    def addAll(self, other: S):
        for value in other:
            self.append(value)

    def clear(self):
        self._head = None
        self._size = 0
        self._sorted = False

    def get(self, index: int):
        return self.poll(index)

    def indexOf(self, value: T):
        index = 0
        current = self._head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def lastIndexOf(self, value: T):
        index = 0
        last_index = -1
        current = self._head
        while current:
            if current.value == value:
                last_index = index
            current = current.next
            index += 1
        return last_index

    def validIndex(self, index: int):
        return 0 <= index <= self._size

    def subList(self, start: int, end: int):
        if not self.validIndex(start) or not self.validIndex(end) or start > end:
            raise IndexError("Invalid index")
        sub_list = LinkedList()
        current = self._head
        for i in range(start):
            current = current.next
        for _ in range(end - start):
            sub_list.append(current.value)
            current = current.next
        return sub_list

    def removeAll(self, other: S):
        for value in other:
            while self.contains(value):
                self.remove_by_value(value)

    def appendList(self, other: S):
        self.addAll(other)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next
