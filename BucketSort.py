H = []
for i in range(100):
    H.append([])
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    bucket_size = (max_value - min_value) / bucket_count + 1e-9
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_value) / bucket_size)
        print(index)
        buckets[index].append(num)
    sorted_array = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        sorted_array.extend(sorted_bucket)
    return sorted_array
import random

def generate_non_integer_list(num):
    if num < 0:
        raise ValueError("列表长度不能为负数。")
    non_integer_list = [random.uniform(0.0, 100.0) for _ in range(num)]
    return non_integer_list

print(bucket_sort(generate_non_integer_list(1000)))
