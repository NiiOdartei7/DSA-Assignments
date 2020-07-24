import numpy


'''
Because the question asked for a defined maximum size I am assuming it means
that I should define the size and not the user

'''
class Deque:
    MaxArraySize = 20

    '''
    
    Because it is a circular array two indices are being tracked
    The front of the array and the immediate back of the array
    '''
    def __init__(self):
        self.items = [None] * self.MaxArraySize
        self.nItems = 0
        self.front = 0
        self.rear = -1

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def isFull(self):
        if self.nItems == self.MaxArraySize:
            return True
        else:
            return False

    def add_to_front(self, x):
        if Deque().isFull():
            print("The deque is full")

        else:
            self.front = (self.front - 1) % len(self.items) #Changes the front when a value is added
            self.items[self.front] = x
            self.nItems += 1

    def add_to_back(self, x):
        if Deque().isFull():
            print("The deque is empty")

        else:
            self.rear = (self.rear + 1)% len(self.items) #Changes the rear when a value is added
            self.items[self.rear] = x
            self.nItems += 1

    def remove_front(self):
        if Deque().isEmpty():
            print("Deque is empty")

        else:
            answer = self.items[self.front] #contains the value to be removed before it is removed
            self.items[self.front] = None   #changes the value of front to None
            self.front = (self.front + 1)% len(self.items)
            self.nItems -= 1
            print("Removing " , answer , " from the front of the deque")

    def remove_rear(self):
        if Deque().isEmpty():
            print("The deque is empty")

        else:
            answer = self.items[self.rear]
            self.items[self.rear] = None
            self.rear = (self.rear-1)% len(self.items)
            self.nItems -=1
            print("Removing " , answer , " from the back of the deque")

    def printlist(self):
        print(self.items)

    def checkSize(self):
        print("The number of elements in the deque is ", self.nItems)

'''
This is a driver method to test the basic functions of the deque

'''
def main():
    d = Deque()
    d.add_to_front(5)
    d.add_to_front(56)
    d.add_to_back(10)
    d.add_to_back(11)
    d.add_to_front(20)
    d.add_to_back(23)
    d.add_to_back(15)
    d.checkSize()
    d.add_to_front(30)
    d.add_to_back(75)
    d.add_to_back(15)
    d.add_to_back(135)


    d.printlist()

    d.remove_rear()
    d.printlist()

'''
This function returns a value between 0 and 1 to be used by the simulation
'''

def simprob():
    rand = numpy.random.uniform(0, 1)
    return rand

'''
This function adds 5 random numbers to the front and back of the deque
It then uses the simprob() function from above to determine which case should run depending on the
value of rand

'''
def sim():

    b = Deque()


    print('***Adding 5 random members to the front***\n ')
    for i in range(5):
        b.add_to_front(numpy.random.randint(1, 100))
        #b.printlist()
    b.printlist()
    print('\n')
    print('***Adding 5 random members to the back***\n ')
    for i in range(5):
        b.add_to_back(numpy.random.randint(1, 100))
        #b.printlist()
    b.printlist()
    print('\n')

    for i in range(10):
        a = simprob()
        ran_num = numpy.random.randint(1, 100)
        print("The probability is", a)

        if a >= 0.0 and a <= 0.1:
            b.add_to_front(ran_num)
            print("Adding ", ran_num, " to the front of the deque")
            b.checkSize()
            b.printlist()
            print("\n")

        elif a > 0.1 and a <= 0.3:
            b.remove_front()
            b.printlist()
            b.checkSize()
            print("\n")

        elif a > 0.3 and a <= 0.4:
            b.add_to_back(ran_num)
            print("Adding ", ran_num, " to the end of the deque")
            b.printlist()
            b.checkSize()
            print("\n")

        elif a > 0.4 and a <= 1.0:
            b.remove_rear()
            b.printlist()
            b.checkSize()
            print("\n")

    print("The final deque is \n")
    b.printlist()
    print("\n")


def sim2():
    b = Deque()


    print('***Adding 5 random members to the front***\n ')
    for i in range(5):
        b.add_to_front(numpy.random.randint(1, 100))
        #b.printlist()
    b.printlist()
    print('\n')
    print('***Adding 5 random members to the back***\n ')
    for i in range(5):
        b.add_to_back(numpy.random.randint(1, 100))
        #b.printlist()
    b.printlist()
    print('\n')



    for i in range(10):
       a = simprob()
       ran_num = numpy.random.randint(1,100)
       print("The probability is", a)
       if a >= 0.0 and a <= 0.1:

           b.add_to_front(ran_num)
           print("Adding " , ran_num , " to the front of the deque")
           b.checkSize()
           b.printlist()
           print("\n")

       elif a > 0.1 and a <= 0.7:
           b.remove_front()
           b.printlist()
           b.checkSize()
           print("\n")

       elif a > 0.7 and a <= 0.8:
           b.add_to_back(ran_num)
           print("Adding " , ran_num , " to the end of the deque")
           b.printlist()
           b.checkSize()
           print("\n")

       elif a > 0.8 and a <= 1.0:
           b.remove_rear()
           b.printlist()
           b.checkSize()
           print("\n")

    print("The final deque is \n")
    b.printlist()
    print("\n")

#sim()
#sim2()
#main()





