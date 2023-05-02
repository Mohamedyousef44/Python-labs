

import random
import math

# program 1

# def similar_elements(list):
#     li = []
#     for l in list:
#         li.append(int(l))
#     return li

# print(similar_elements([10.5, 23.66, 5.001]))


# program 2


# def exchange_str_half(str1, str2):

#     front1 = str1[0:int(len(str1)/2)]
#     back1 = str1[int(len(str1)/2):]

#     front2 = str2[0:math.ceil(len(str2)/2)]
#     back2 = str2[math.ceil(len(str2)/2):]

#     return front1+front2, back1+back2


# print(exchange_str_half('abcd', 'abc'))


# program 3

# li = [1, 2, 5, 5]


# def is_in_sequence(list):
#     end = len(list)
#     for idx in range(0, end-1):

#         if (list[idx+1] <= list[idx]):
#             return False

#     return True


# print(is_in_sequence(li))

# program 4

# def bubble_sort(list):
#     n = len(list)

#     for i in range(n - 1):

#         flag = False
#         for j in range(n - 1 - i):

#             if list[j] > list[j + 1]:
#                 tmp = list[j]
#                 list[j] = list[j + 1]
#                 list[j + 1] = tmp
#                 flag = True

#         if flag == False:
#             break

#     return list


# print(bubble_sort([10, 3, 5, 19, 15]))


# program 5


# tries = 10
# gamenum = math.floor(random.random() * 100)
# print(gamenum)
# # while loop check if tries is == 0 or not
# while (tries > 0):
#     usernum = int(input('please enter a number ?'))

#     if (usernum > 100):
#         print('this number is not allowed \n')

#     elif (usernum > gamenum):
#         tries -= 1
#         print('your number is greater than game number')

#     elif (usernum < gamenum):
#         tries -= 1
#         print('your number is smaller than game number')

#     else:
#         tries -= 1
#         print('congratulation you guessed it')
#         gamenum = math.floor(random.random() * 100)

#     if (tries == 0):
#         print('sorry your trials finished , do you want to continue ? \n')
#         msg = input('hit Y if Yes and N for No \n').lower()
#         if (msg == 'y'):
#             tries = 10
#         else:
#             break

arr = [[1, 2, 3], [1, 2, 3]]


def diagonalDifference(arr):

    l = len(arr)
    leftsum = 0
    rightsum = 0

    if (len(arr[0]) == l):
        for i in range(l):
            leftsum += arr[i][i]
            rightsum += arr[i][l-1]
            l -= 1
        return abs(leftsum - rightsum)
    return -1


print(diagonalDifference(arr))
