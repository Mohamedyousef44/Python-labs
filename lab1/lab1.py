# lab 1

# program 1

# def rev_string(word):
#     return word[::-1]


# firstname = input('please enter your first name > \n')
# lastname = input('please enter your last name > \n')

# print(rev_string(lastname)+' '+rev_string(firstname))


# program 2

# def sum_num(num):
#     return int(num) + int(num + num) + int(num + num + num)


# num = input('please enter your number?')

# print(sum_num(num))


# program 3

# example = """ sample string:
#     a string that you "don't" have to escape
#     This is
#     a ....... multi-line """
# print(example)


# program 4
# import math


# def sphere_volume(radius):
#     return 4/3 * (math.pi) * radius**3


# radius = int(input('please enter sphere radius ?'))

# print(sphere_volume(3))


# program 5
# def triangle_area(base, height):

#     if (type(base) == int and type(height) == int):
#         return 0.5 * base * height
#     return -1


# print(triangle_area(6, 6))

# program 6

# n = int(input('enter number from 1 to 10 ?'))


# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# for i in range(n-1, 0, -1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# program 7

# word = input('enter any word ?')

# print(rev_string(word))

# program 8

# for x in range(0, 6):
#     if (x == 3 or x == 6):
#         continue
#     print(x)


# program 9

# def fibonacci(length):
#     nums = [0, 1]
#     n = 0
#     while (len(nums) < length):
#         nums.append(sum(nums[n:]))
#         n += 1

#     print(nums)


# fibonacci(10)

# program 10

# def count_digits_and_letters(str):
#     digits = 0
#     letters = 0
#     for char in str:
#         if char.isdigit():
#             digits += 1
#         elif char.isalpha():
#             letters += 1
#     return digits, letters


# print('number of digits is %i and number of letters is %i' % (
#     count_digits_and_letters('mo123456')))
