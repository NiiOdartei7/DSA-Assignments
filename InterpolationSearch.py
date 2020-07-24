import numpy

import time

def interpolationSearch(x,high,low,e):
    if high >= low:

        numerator = (high - low) * (e - x[low])
        denominator = (x[high] - x[low])
        POS = low + (numerator//denominator)

        if x[POS] == e:
            return x[POS]

        elif x[POS] > e:
            return binarySearch(x, POS - 1, low, e)

        else:
            return binarySearch(x, high, POS + 1, e)

    else:
        return -1



def binarySearch(x,high,low,e):

    if high >= low:

        POS = (high + low) // 2

        if x[POS] == e:

            return x[POS]



        elif x[POS] > e:
            return binarySearch(x,POS-1,low,e)

        else:
            return binarySearch(x,high,POS+1, e)

    else:
        return -1
        


def main():

    #This run is for the binary search
    n = eval(input("Enter the size of the array: "))
    array = numpy.random.randint(1, 32767, n)
    a = sorted(array) #sorts the array

    target = numpy.random.choice(array)

    start_time = time.time()
    binarySearch(a,len(a)-1,0,target)
    end_time = time.time()
    print("Time taken for Binary Search: ",end_time - start_time)


    #This run is for the interpolation search
    arr = numpy.random.randint(1, 32767, n)
    b = sorted(array)

    value = numpy.random.choice(b)

    s_time = time.time()
    interpolationSearch(b,len(b)-1,0,value)
    e_time = time.time()
    print("Time taken for Interpolation Search : ",e_time- s_time)








main()





