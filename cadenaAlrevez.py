i = 4
def imp_arr(arr, i):
    if i == 0:
        return

    print(arr[i])

    imp_arr(arr, i - 1)

arr = [10, 20, 30, 40, 50]

imp_arr(arr, i)


