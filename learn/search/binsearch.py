def bin_search(search_array, n, low, high):
    if low > high:
        return -1
    mid = (high + low) // 2
    if n < search_array[mid]:
        return bin_search(search_array, n, low, mid-1)
    elif n > search_array[mid]:
        return bin_search(search_array, n, mid+1, high)
    return mid

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bin_search(array, 102, 0, len(array)-1))