import time
import ctypes
import numpy as np

def bubblesort(nums: list):
    sorted = True
    for _ in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                sorted = False
                key = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = key
        if sorted:
            break

def sum_list(nums: list):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    return sum

def printIntegerList(IntegerList: ctypes.POINTER(ctypes.c_int)):
    result = []

    for i in range(len(IntegerList)):
        result.append(IntegerList[i])

    return result

"""Bubblesort"""

# Normal Bubblesort

total_t = 0
result = []

nums = [
        100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
        90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
        80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
        70, 69, 68, 67, 66, 65, 64, 63, 62, 61,
        60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
        50, 49, 48, 47, 46, 45, 44, 43, 42, 41,
        40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
        30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        ]

for i in range(100):
    temp_nums = nums.copy()
    
    start_t = time.time()
    bubblesort(temp_nums)
    exe_t = time.time() - start_t
    
    total_t += exe_t

    result = temp_nums

avg_t = round(total_t * 10 ** 6 / 100, 3)

print("Bubblesort")
print("----------")
print(str(avg_t) + "us")
print(result)
print("")

lib = ctypes.CDLL("./lib.so")

# Bubblesort with C

lib.bubblesort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

total_t = 0

for i in range(100):
    IntegerList = ctypes.c_int * len(nums)
    arr = IntegerList(*nums.copy())

    start_t = time.time()
    lib.bubblesort(arr, len(arr))
    exe_t = time.time() - start_t
    
    total_t += exe_t

    result = arr

result_str = "["

avg_t = round(total_t * 10 ** 6 / 100, 3)

print("Bubblesort with C")
print("-----------------")
print(str(avg_t) + "us")
print(printIntegerList(result))
print("")

"""Sum"""

# Normal Sum

total_t = 0

for i in range(100):
    temp_nums = nums.copy()
    
    start_t = time.time()
    result = sum_list(temp_nums)
    exe_t = time.time() - start_t
    
    total_t += exe_t

avg_t = round(total_t * 10 ** 6 / 100, 3)

print("Sum")
print("-------")
print(str(avg_t) + "us")
print(result)
print("")

# Sum with Numpy

total_t = 0

for i in range(100):
    temp_nums = np.array(nums.copy())
    
    start_t = time.time()
    result = np.sum(temp_nums)
    exe_t = time.time() - start_t
    
    total_t += exe_t

avg_t = round(total_t * 10 ** 6 / 100, 3)

print("Sum with Numpy")
print("--------------")
print(str(avg_t) + "us")
print(result)
print("")

# Sum with C

lib.sumlist.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

total_t = 0

for i in range(100):
    IntegerList = ctypes.c_int * len(nums)
    arr = IntegerList(*nums.copy())
    
    start_t = time.time()
    result = lib.sumlist(arr, len(arr))
    exe_t = time.time() - start_t
    
    total_t += exe_t

avg_t = round(total_t * 10 ** 6 / 100, 3)

print("Sum with C")
print("----------")
print(str(avg_t) + "us")
print(result)
print("")
