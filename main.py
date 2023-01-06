FILENAME = "input.txt"

WRONG = [11621]


def test1():
    numbers = dict()
    count = 0
    for i, line in enumerate(open("input.txt")):
        number = int(line.strip())
        if number in numbers:
            #print("Duplicate number:", number, number, numbers[number], i)
            numbers[number] += 1
        else:
            numbers[number] = 1

        #print(number
        count += 1
        pass
    print(len(numbers), count)


class CircularLinkedList:

    def mix(self, node):
       # print("mix", node.number)
        #print(self)
        if node.number > 0 :
            self.skipNForward(node, node.number)
        elif node.number < 0:
            self.skipNBackward(node, node.number)
        #print(self)

    def findNForward(self, node, n):
        n = n % self.length
        place = node
        for _ in range(n):
            place = place.next
        return place

    def skipNForward(self, node, n):
        if 0 == n: return
        n = n % self.length
        # first remove the node, remembering the next node
        place = node.next
        #self.removeNode(node)
        # count N places forward, wrapping if needed
        for i in range(n-1):
            place = place.next
        self.removeNode(node)
        # re-insert the node
        self.insertAfter(node, place)
    
    def skipNBackward(self, node, n):
        if 0 == n: return
        n = abs(n) % self.length

        # first remove the node, remembering the prev node
        place = node
        #self.removeNode(node)
        # count N places backwards, wrapping if needed
        for i in range(n):
            place = place.prev
        # re-insert the node
        self.removeNode(node)
        self.insertBefore(node, place)

    def insertAfter(self, node, target):
        target.next.prev = node
        node.next = target.next
        
        target.next = node
        node.prev = target
        self.length += 1 

    def insertBefore(self, node, target):
        target.prev.next = node
        node.prev = target.prev
        
        target.prev = node
        node.next = target
        self.length += 1 
    
    def __init__(self, values = []):
        self.head = None
        self.tail = None
        self.length = 0

        for value in values:
            self.insert(value)
        

    def insert(self, number):
        node = DoublyLinkedListNode(number)
        if self.head is None:
            self.head = node
            node.next = node
            node.prev = node
            
        else:
            left = self.head.prev
            right = self.head
            left.next = node
            node.prev = left
            right.prev = node
            node.next = right
            
        self.length += 1
        return node

    def find(self, number):
        current = self.head
        for _ in range(self.length):
            if current.number == number:
                return current
            current = current.next
        return None

    def removeNode(self, node):
        # if only node
        if self.length == 1:
            self.head = None

        
        else:
            # if head, move head to next, then continue
            if (node == self.head):
                self.head = node.next
            
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = None
        
        self.length -= 1
        return True

    def __str__(self):
        string = ""
        current = self.head
        for _ in range(self.length):
            string += str(current.number) + " "
            current = current.next
        return string







class DoublyLinkedList:

    def mix2(self, node):
        print("mix", node.number)

        for i in range(node.number):
            print("skip", i, ":", self)
            if node.number >= 1:
                self.skipForward(node)
            else:
                self.skipBackward(node)
            print("now ", i, ":", self)

        print(self)

    def mix(self, node):
        print("mix", node.number)
        print(self)
        if node.number > 0 :
            self.skipNForward(node, node.number)
        elif node.number < 0:
            self.skipNBackward(node, node.number)
        print(self)

    def strReverse(self):
        string = ""
        current = self.tail
        while current is not None:
            string += str(current.number) + " "
            current = current.prev
        return string

    def skipNForward(self, node, n):
        if 0 == n: return
        n = n % self.length
        # first remove the node, remembering the next node
        place = node.next
        if None == place:
            place = self.head
        self.removeNode(node)
        # count N places forward, wrapping if needed
        for i in range(n-1):
            if place == None: 
                place = self.head
                i -= 1
            else:
                place = place.next
        # re-insert the node
        self.insertAfter(node, place)
    
    def skipNBackward(self, node, n):
        if 0 == n: return
        n = abs(n) % self.length

        # first remove the node, remembering the prev node
        place = node.prev
        if None == place:
            place = self.tail
        self.removeNode(node)
        # count N places backwards, wrapping if needed
        for i in range(n):
            if place == None: 
                place = self.tail
            else:
                place = place.prev
        if place == None:
            place = self.tail
        # re-insert the node
        self.insertAfter(node, place)

    def insertAfter(self, node, target):
        # if target is tail, become the tail
        if target is self.tail:
            target.next = node
            node.prev = target
            
            self.tail = node
            
        # else insert after target
        else:
            target.next.prev = node
            node.next = target.next
            
            target.next = node
            node.prev = target
            
    def skipForward(self, node):
        
        # if head, special case
        if node == self.head:
            a = node.prev
            b = node.next
            c = node.next.next

            # update a and b to link to eachother
            #a.next = b # don't do because head
            b.prev = a
            
            # update b and node to link to eachother
            b.next = node
            node.prev = b

            # update c and node to link to eachother
            node.next = c
            c.prev = node

            # update the head
            self.head = b

        # if tail, special case, move tail, jump past head
        elif node == self.tail:
            # first, remove node and fix the tail
            self.tail = node.prev
            node.prev.next = None

            # now "head" update between head and first node
            b = self.head
            c = self.head.next
            
            # update b and node to link to eachother
            b.next = node
            node.prev = b

            # update c and node to link to eachother
            node.next = c
            c.prev = node       
            
        # if next is tail, special case. become the tail
        elif node.next == self.tail:
            
            a = node.prev
            b = node.next
            c = node.next.next

            # update a and b to link to eachother
            a.next = b
            b.prev = a
            
            # update b and node to link to eachother
            b.next = node
            node.prev = b

            # update c and node to link to eachother
            node.next = c
            # c.prev = node # don't do because tail
            
            self.tail = node
        
        # else regular update
        else:
            a = node.prev
            b = node.next
            c = node.next.next

            # update a and b to link to eachother
            a.next = b
            b.prev = a
            
            # update b and node to link to eachother
            b.next = node
            node.prev = b

            # update c and node to link to eachother
            node.next = c
            c.prev = node

    
    def __init__(self, values = []):
        self.head = None
        self.tail = None
        self.length = 0

        for value in values:
            self.insert(value)
        

    def insert(self, number):
        node = DoublyLinkedListNode(number)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length += 1
        else:
            current = self.tail
            current.next = node
            self.tail = current.next
            current.next.prev = current
            self.length += 1
        return node

    def find(self, number):
        current = self.head
        while current is not None:
            if current.number == number:
                return current
            current = current.next
        return None

    def removeNode(self, node):
        # if only node
        if self.length == 1:
            self.head = None
            self.tail = None

        # if head
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
        
        # if tail
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None

        # somewhere in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = None
        
        self.length -= 1
        return True

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += str(current.number) + " "
            current = current.next
        return string


class DoublyLinkedListNode:

    def __init__(self, number):
        self.number = number
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

#    def __eq__(self, other):
#        return self.number == other.number

#    def __ne__(self, other):
#        return self.number != other.number

def runTest():

    # cases to test
    # 1) node is head going forward
    # 2) node is tail going forward
    # 3) node is head going backwards
    # 4) node is tail going backwards

    # test 1 - good!
    print("\nTEST 1- node is head going forward")
    dll = CircularLinkedList([1,2,3,4,5])
    print(dll)
    node = dll.find(1)
    dll.mix(node)
    print(dll)


    # test 2 - ?
    print("\nTEST 2 - node is tail going forward")
    dll = CircularLinkedList([5,2,3,4,1])
    print(dll)
    node = dll.find(1)
    dll.mix(node)
    print(dll)    
    
    # test 3 - good!
    print("\nTEST 3 - node is head going backwards")
    dll = CircularLinkedList([-3,2,3,4,5])
    print(dll)
    node = dll.find(-3)
    dll.mix(node)
    print(dll)


    # test 4 - ?
    print("\nTEST 4 - node is tail going backwards")
    dll = CircularLinkedList([5,2,3,4,-1])
    print(dll)
    node = dll.find(-1)
    dll.mix(node)
    print(dll)    


    # test 5 - ?
    print("\nTEST 5 - node is near head going back")
    dll = CircularLinkedList([1,2,-2,0,-3,3,4])
    print(dll)
    node = dll.find(-2)
    dll.mix(node)
    print(dll)    


    print("\nTEST 6")
    n=4
    dll = CircularLinkedList([n,7,8,9])
    print(dll)
    node = dll.find(n)
    dll.mix(node)
    print(dll) 

    #return
    
    puzzle = []
    for line in open(FILENAME):
        number = int(line.strip())
        puzzle.append(number)

    
    puzzleList = CircularLinkedList()
    puzzleArray = []
    for number in puzzle:
        node = puzzleList.insert(number)
        puzzleArray.append(node)

    for node in puzzleArray:
        #print()
        #print(node.number)
        puzzleList.mix(node)

    sum = 0
    set = [1000,2000,3000]
    zeroNode = puzzleList.find(0)
    for number in set:
        #print(zeroNode.number)
        node = puzzleList.findNForward(zeroNode, number)
        print(node.number)
        sum += node.number
    print(sum)

    #print(puzzleList.findNForward(zeroNode,2000).number)

    #print(puzzleList.findNForward(zeroNode,3000).number)
    

def runTest2():

    # cases to test
    # 1) node is head going forward
    # 2) node is tail going forward
    # 3) node is head going backwards
    # 4) node is tail going backwards

    # test 1 - good!
    print("\nTEST 1- node is head going forward")
    dll = DoublyLinkedList([1,2,3,4,5])
    print(dll)
    node = dll.find(1)
    dll.mix(node)
    print(dll)


    # test 2 - ?
    print("\nTEST 2 - node is tail going forward")
    dll = DoublyLinkedList([5,2,3,4,1])
    print(dll)
    node = dll.find(1)
    dll.mix(node)
    print(dll)    
    
    # test 3 - good!
    print("\nTEST 3 - node is head going backwards")
    dll = DoublyLinkedList([-3,2,3,4,5])
    print(dll)
    node = dll.find(-3)
    dll.mix(node)
    print(dll)


    # test 4 - ?
    print("\nTEST 4 - node is tail going backwards")
    dll = DoublyLinkedList([5,2,3,4,-1])
    print(dll)
    node = dll.find(-1)
    dll.mix(node)
    print(dll)    


    # test 5 - ?
    print("\nTEST 5 - node is near head going back")
    dll = DoublyLinkedList([1,2,-2,0,-3,3,4])
    print(dll)
    node = dll.find(-2)
    dll.mix(node)
    print(dll)    
    
    #return
    puzzle = [1, 2, -3, 3, -2, 0, 4]

    #print(puzzle)

    puzzle = []
    for line in open(FILENAME):
        number = int(line.strip())
        puzzle.append(number)

    
    puzzleList = DoublyLinkedList()
    puzzleArray = []
    for number in puzzle:
        node = puzzleList.insert(number)
        puzzleArray.append(node)

    for node in puzzleArray:
        print()
        #print(node.number)
        puzzleList.mix(node)


runTest()


def run():
    return
    puzzle = List([1, 2, -3, 3, -2, 0, 4])
    original = List([1, 2, -3, 3, -2, 0, 4])
    puzLen = len(puzzle)
    #puzzleInput = processInput(inputFilename)
    #print(puzzleInput)

    print("Initial arrangement:")
    print(puzzle)
    print()

    for i in original:
        #val = puzzle[i]

        #offset = (i + val) % puzLen

        #puzzle = puzzle[:offset] + [puzzle[offset] + val] + puzzle[offset + 1:]
        puzzle.mix(i)

    pass


class List:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self.lst)

    def __getitem__(self, i):
        return self.lst[i]

    def __setitem__(self, i, val):
        self.lst[i] = val

    def __len__(self):
        return len(self.lst)

    def append(self, lst):
        for item in lst:
            self.lst.append(item)

    def mix(self, val):
        #print(self)
        itemIndex = self.lst.index(val)

        newIndex = (itemIndex + val) % len(self)

        print("{0} moves from {1} ".format(val, itemIndex), end="")

        if (newIndex > itemIndex):
            print("forward", end="")
            newTest = List([])
            newTest.append(self.lst[:itemIndex])
            #print(newTest)
            newTest.append(self.lst[itemIndex + 1:newIndex + 1])
            #print(newTest)
            newTest.append([val])
            #print(newTest)
            newTest.append(self.lst[newIndex + 1:])
            #print(newTest)
            self.lst = newTest.lst
        elif (newIndex < itemIndex):
            print("backward", end="")
            newTest = List([])
            newTest.append(self.lst[:itemIndex])
            newTest.append([val])
            newTest.append(self.lst[itemIndex - 1:newIndex])
            newTest.append(self.lst[newIndex:])
            self.lst = newTest.lst
        else:
            print("not at all", end="")
        print(" to between {0} and {1} at {2}".format(self.lst[newIndex - 1],
                                                      self.lst[newIndex + 1],
                                                      newIndex))
        print(self)
        print()


if __name__ == '__main__':

    #test = List([1,2,3,4,5])

    #test.mix(1)
    #print(test)

    if (False):
        # move to to between 4, 5
        oldIndex = 1
        newIndex = 4
        print(test[:oldIndex])
        print(test[oldIndex + 1:newIndex])
        print(2)
        print(test[newIndex:])

        newTest = List([])
        newTest.append(test[:oldIndex])
        newTest.append(test[oldIndex + 1:newIndex])
        newTest.append([2])
        newTest.append(test[newIndex:])
        print(newTest)

    #run()
