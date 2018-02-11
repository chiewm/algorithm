# a = [10, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 21, 50, 41, 60, 80]
# length = len(a)
# b = [1] * length
# c = []
# for i in range(length):
#     if a[i] > a[i-1]:
#         b[i] = b[i-1] + 1
#         c.append(a[b[i]])
#     else:
#         b[i] = b[i-1]
#
#     print(b)
#
# print(max(b))
# print(c)
#

def LIS(l):
    n=len(l)
    F=[0]*n
    c = []
    for i in range(1 ,n):
        if l[i]>l[i-1]:
            F[i]=F[i-1]+1
        else:
            F[i]=F[i-1]

        c.append(l[F[i]])
    print(F)
    print(c)
    return max(F)

a = [10, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 21, 50, 41, 60, 80]
print(LIS(a))

