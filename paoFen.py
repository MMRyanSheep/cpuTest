#paoFen
import time, random, pygame
from quickSort import quick_sort, L
SCREEN_W, SCREEN_H = 1920, 1080
def arrGenerator(num):
    arr = [random.randint(0, num * 2) for i in range(num)]
    return arr
def test(func, data):
    start = time.time()
    func(data)
    end = time.time()
    score = (end - start) // 0.0000008
    return int(score)
def qucikSortTest():
    start = time.time()
    quick_sort(0, len(L) - 1)
    end = time.time()
    score = (end - start) // 0.00008
    return int(score)
def intAdd(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum
def bubble_sort(times):
    arr = arrGenerator(times)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def floatAdd(num):
    sum = 0.0
    i = 3.1415926
    for c in range(num):
        sum += i
    return sum
def intDivide(num):
    sum = 1
    for i in range(1, num):
        sum /= i
    return sum
def single_partition_swap(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

print("主线程正在运行...")
intTestScore = test(intAdd, 100000) * 3
floatTestScore = test(floatAdd, 100000) * 3
intDivideTestScore = test(intDivide, 100000) * 3
bubbleSortTestScore = test(bubble_sort, 1000) // 4
qucikSortTestScore = qucikSortTest()
score = intTestScore + floatTestScore + intDivideTestScore + bubbleSortTestScore + qucikSortTestScore
print("yout CPU score is: ", score)
print('Details: ', '\n', 'intTestScore: ', intTestScore, '\n', 'floatTestScore: ', floatTestScore \
    , '\n', 'intDivideTestScore: ', intDivideTestScore,  \
     '\n', 'bubbleSortTestScore: ', bubbleSortTestScore, '\n', 'qucikSortTestScore: ', qucikSortTestScore)

