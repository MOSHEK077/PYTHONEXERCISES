"""Sorting Algorithms,
Fantastic! Let's dive into the answers for some of the advanced exercises I suggested:

Advanced Exercise 1: Sorting Algorithms (Bubble Sort Example)

Let's start with Bubble Sort, a simple sorting algorithm."""
def sorted(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [24,24,542,452,42244,1313414,1,4,134141413,41341413,43134]
sorted(arr)
print(arr)