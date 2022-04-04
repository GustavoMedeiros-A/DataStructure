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


fluxo1 = Queue()
fluxo2 = Queue()
fluxo3 = Queue()
canal = Queue()


def initFluxo(id, alist):  # id : 1,2,3

    if id == 1:
        fluxo1.enqueue(alist)
    if id == 2:
        fluxo2.enqueue(alist)
    if id == 3:
        fluxo3.enqueue(alist)

    showFluxo()


def showFluxo():
    print(f'O fluxo 1 é {fluxo1}')
    print(f'O fluxo 2 é {fluxo2}')
    print(f'O fluxo 3 é {fluxo3}')


def initCanal():
    maior_len = len(fluxo1)
    if maior_len < len(fluxo2):
        maior_len = len(fluxo2)
    if maior_len < len(fluxo3):
        maior_len = len(fluxo3)

    for i in range(maior_len):
        if len(fluxo1)  > 0:
            canal.enqueue([1, fluxo1.peek()])
            fluxo1.dequeue()
        if len(fluxo2) > 0:
            canal.enqueue([2, fluxo2.peek()])
            fluxo2.dequeue()
        if len(fluxo3) > 0:
            canal.enqueue([3, fluxo3.peek()])
            fluxo3.dequeue()

        print(canal)



def showCanal():
    print(canal)


def run():
    op = 0
    while op != 9:
        print("1. inicializa fluxo ")
        print("2. imprime fluxo")
        print("3. inicializa canal ")
        print("4. imprime canal ")
        print("9. exit ")
        op = int(input("digite a opção: "))
        if op == 1:
            i = int(input("digite o identificador do fluxo (1, 2, 3): "))
            lista = eval(input("Digite apenas um número: "))
            initFluxo(i, lista)
            print(fluxo1)

        if op == 2:
            print(fluxo1)
        if op == 3:
            initCanal()
        if op == 4:
            showCanal()
        if op == 9:
            exit()


run()
