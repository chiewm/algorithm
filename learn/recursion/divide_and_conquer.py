def sum_f(array, low, high):
    if low == high:
        return array[low]
    else:
        return sum_f(array, low, (low + high) // 2) + sum_f(array, (low + high) // 2 + 1, high)


arr = [1, 2, 3, 4, 5, 6]
print(sum_f(arr, 0, 5))
