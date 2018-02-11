# 求解一个大规模的问题，可以将其划分为两个子问题，
# 其一是平凡问题，另一个规模缩减。由子问题的解，得到原问题的解。


def sum_f(arr, n):
    if n < 1:
        return 0
    else:
        total_sum = sum_f(arr, n-1) + arr[n-1]
        return total_sum

print(sum_f([1, 2, 3, 4, 5, 6], 6))
