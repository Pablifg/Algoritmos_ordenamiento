import random 
import sys

def selection_sort(array):

    for i in range(len(array)):

        idxDes = i
        for j in range(i + 1, len(array)):
            if array[idxDes] > array[j]:
                idxDes = j

        print(array)
        
        array[i], array[idxDes] = array[idxDes], array[i]
    


def run():
    n = 5
    my_list = [random.randint(0,100) for _ in range(n)]
    selection_sort(my_list)
    print('Sorted array: ')
    for i in range(len(my_list)):
        print('%d' %my_list[i])



if __name__ == '__main__':
    print('S e l e c t - S o r t')
    run()
