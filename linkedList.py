class EmptyLinkedList(Exception):
    pass


class LinkedList:

    class Node:
        def __init__(self, element, next_data=None):
            self.__element__ = element
            self.__next__ = next_data 

    def __init__(self):
        self.__head__ = None
        self.__tail__ = None
        self.__size__ = 0

    def __len__(self):
        return self.__size__

    def __iter__(self):
        cur = self.__head__
        return cur.__next__

    def head(self):
        return self.__head__.__element__

    def tail(self):
        return self.__tail__.__element__

    def print_list(self):
        cur = self.__head__
        while cur.__next__:
            print(cur.__element__)
            cur = cur.__next__
        print(cur.__element__, '<- last')
        print(cur.__next__)

    def is_empty(self):
        return self.__head__ is None

    def add_first(self, data):
        m_data = self.Node(data)
        if self.is_empty():
            self.__tail__ = m_data
            self.__head__ = m_data
        else:
            m_data.__next__ = self.__head__
            self.__head__ = m_data
        self.__size__ += 1

    def add_last(self, data):
        m_data = self.Node(data)
        if self.is_empty():
            self.__head__ = m_data
            self.__tail__ = m_data
        else:
            self.__tail__.__next__ = m_data
            self.__tail__ = m_data
        self.__size__ += 1
