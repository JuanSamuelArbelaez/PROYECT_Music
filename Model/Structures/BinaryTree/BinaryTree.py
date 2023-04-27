from typing import TypeVar, Generic

from Model.Structures.ComparableValue.ComparableValue import ComparableValue
T = TypeVar('T', bound=ComparableValue)


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(Generic[T]):

    def __init__(self):
        self.__height = 0
        self.__root = None

    def __check_type(self, value: T):
        if not all(hasattr(value, attr) for attr in ('__lt__', '__gt__', '__eq__', '__le__', '__ge__')):
            raise TypeError("BinaryTree can only store objects that implement comparison operators.")

    def height(self):
        return self.__height

    def is_empty(self):
        return self.__root is None

    def contains(self, value: T):
        return self.__contains_helper(self.__root, value)

    def __contains_helper(self, node: 'Node[T]', value: T):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self.__contains_helper(node.left, value)
        else:
            return self.__contains_helper(node.right, value)

    def add(self, value: T):
        self.__check_type(value)
        if self.__root is None:
            self.__root = Node[T](value)
        else:
            self.__add_helper(self.__root, value)

    def __add_helper(self, node: 'Node[T]', value: T):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__add_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__add_helper(node.right, value)

    def balance(self):
        values = self.in_order_traversal()
        self.clear()
        self.__balance_helper(values, 0, len(values) - 1)

    def __balance_helper(self, values: [T], start: int, end: int):
        if start > end:
            return None
        mid = (start + end) // 2
        self.add(values[mid])
        self.__balance_helper(values, start, mid - 1)
        self.__balance_helper(values, mid + 1, end)

    def remove(self, value: T):
        self.__root = self.__remove_helper(self.__root, value)

    def __remove_helper(self, node: 'Node[T]', value: T):
        if node is None:
            return None
        elif value < node.value:
            node.left = self.__remove_helper(node.left, value)
        elif value > node.value:
            node.right = self.__remove_helper(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.__find_min(node.right)
                node.value = successor.value
                node.right = self.__remove_helper(node.right, successor.value)
        return node

    def __find_min(self, node: 'Node[T]'):
        while node.left is not None:
            node = node.left
        return node

    def clear(self):
        self.__root = None

    def in_order_traversal(self):
        values = []
        self.__in_order_traversal_helper(self.__root, values)
        return values

    def __in_order_traversal_helper(self, node: 'Node[T]', values: [ComparableValue]):
        if node is not None:
            self.__in_order_traversal_helper(node.left, values)
            values.append(node.value)
            self.__in_order_traversal_helper(node.right, values)

    def post_order_traversal(self):
        values = []
        self.__post_order_traversal_helper(self.__root, values)
        return values

    def __post_order_traversal_helper(self, node: 'Node[T]', values: [ComparableValue]):
        if node is not None:
            self.__post_order_traversal_helper(node.left, values)
            self.__post_order_traversal_helper(node.right, values)
            values.append(node.value)
