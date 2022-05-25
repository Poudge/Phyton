import random

arrey =[]

for i in range(1, 20):
    arrey.append(random.randint(0, i) + i)

print(arrey)

def binSearch(arr, n):
    arr.sort()
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = int((start + end) / 2)
        if arr[mid] == n:
            return mid
        elif n > arr[mid]:
            start = mid + 1
        elif n < arr[mid]:
            end = mid - 1

    return -1

print(binSearch(arrey, 11))

