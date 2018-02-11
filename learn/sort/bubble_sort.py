def bubble_sort(myarr):
    length = len(myarr)
    for i in range(length - 1):
        for j in range(length - i - 1):  # 每次比较少一次
            print(j)
            if myarr[j] > myarr[j + 1]:
                myarr[j], myarr[j + 1] = myarr[j + 1], myarr[j]
        print("-----------")
    print(arr)

arr = [3, 5, 2, 6, 1, 7]
bubble_sort(arr)

