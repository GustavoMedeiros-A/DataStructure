class Queue:
    def __init__(self, iterable=None):
        self.__items = []
        if iterable:
            for element in iterable:
                self.enqueue(element)

    def clear(self):
        self.__items = []

    def copy(self):
        return Queue(self)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.__items.append(item)

    def offer(self, item):  # == enqueue
        self.enqueue(item)

    def dequeue(self):
        return self.__items.pop(0)

    def poll(self):  # == dequeue
        return self.dequeue()

    def peek(self):
        return self.__items[0]

    def front(self):  # == peek
        return self.peek()

    def size(self):
        return len(self.__items)

    def extend(self, iterable):
        for element in iterable:
            self.enqueue(element)

    def replace(self, value, new_value):
        index = self.__items.index(value)
        self.__items[index] = new_value

    def __contains__(self, value):
        return value in self.__items

    def __len__(self):
        return self.size()

    def __repr__(self):
        return '[' + ', '.join([str(v) for v in self.__items]) + ']'

    def __str__(self):
        return repr(self)

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current >= self.size():
            raise StopIteration
        else:
            self.__current += 1
            return self.__items[self.__current - 1]


if __name__ == '__main__':

    q = Queue()
    q.enqueue(10)
    q.offer(20)
    q.enqueue(30)
    q  # call __repr__
    print(q)  # call __str__
    print('20 in queue : ', 20 in q)  # call __contains__
    print('size ', len(q))  # call __len__

    print('peek : ', q.peek())
    print('front : ', q.front())

    print('dequeue : ', q.dequeue())
    print('peek : ', q.peek())
    print('poll : ', q.poll())

    print('size ', q.size())
    for e in q:  # call __iter__  __next__
        print(e)