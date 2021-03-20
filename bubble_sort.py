#Do comparison of adjacent elements
# Repeat / cicle until without swap
from datetime import datetime

def bubble_sort(array):
    n = len(array)
    changes = 0

    #O(n^2)
    for i in range(n):
        swap = False
        #Print cicle
        #print('Iter BY SIZE OF LIST %d'%i)
        #print(array)


        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                #swap
                swap = True                
                array[j], array[j+1] = array[j+1], array[j]
                changes += 1
                print('ITER FOR VERIFY IF WE NEED SWAP ELEMENT %d'%j)
                print(array)

        if not swap:
            break

    return changes



def run():
    array = [190, 1200, 1, 2, 4, 55, 1000, 6, 800]

    start_time = datetime.now()
    
    result_changes = bubble_sort(array)

    print('The ascending sorted array is: ')
    for i in range(len(array)):
        print('%d'%array[i])

    print('Number of iterations: %d'%result_changes)

    print(datetime.now() - start_time)


if __name__ == '__main__':
    run()
