def filter(arr, func):
    return [i for i in arr if func(i)]



print(filter([1, 2, 3, 4], lambda i: i % 2 == 1))