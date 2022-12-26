
inputFilename = "example.txt"


def run():
    puzzle = List([1,2,-3,3,-2,0,4])
    original = List([1,2,-3,3,-2,0,4])
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
        for item in lst: self.lst.append(item)

    def mix(self, val):
        #print(self)
        itemIndex = self.lst.index(val)
        
        newIndex = (itemIndex + val) % len(self)

        print("{0} moves from {1} ".format(val, itemIndex), end="" )

        if (newIndex > itemIndex):
            print("forward", end="")                
            newTest = List([])
            newTest.append(self.lst[:itemIndex])
            #print(newTest)
            newTest.append(self.lst[itemIndex+1:newIndex+1])
            #print(newTest)
            newTest.append([val])
            #print(newTest)
            newTest.append(self.lst[newIndex+1:])      
            #print(newTest)
            self.lst = newTest.lst
        elif (newIndex < itemIndex):
            print("backward", end="")
            newTest = List([])
            newTest.append(self.lst[:itemIndex])
            newTest.append([val])
            newTest.append(self.lst[itemIndex-1:newIndex])
            newTest.append(self.lst[newIndex:])      
            self.lst = newTest.lst
        else:
            print("not at all", end="")
        print(" to between {0} and {1} at {2}".format(self.lst[newIndex-1], self.lst[newIndex+1], newIndex))
        print(self)
        print()
        

if __name__ == '__main__':

    #test = List([1,2,3,4,5])

    #test.mix(1)
    #print(test)

    if (False) :    
        # move to to between 4, 5
        oldIndex = 1
        newIndex = 4
        print(test[:oldIndex])
        print(test[oldIndex+1:newIndex])
        print(2)
        print(test[newIndex:])
    
        newTest = List([])
        newTest.append(test[:oldIndex])
        newTest.append(test[oldIndex+1:newIndex])
        newTest.append([2])
        newTest.append(test[newIndex:])
        print(newTest)
    
    run()
