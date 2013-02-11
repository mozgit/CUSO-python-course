def Sort(arr=[2, 4, 5, 1, 2, 3, 6]):
    less = []
    type(less)
    more = []
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    for i in range(0, len(arr) - 1):
        if arr[i] < pivot:
            less.append(arr[i])
        else:
            more.append(arr[i])
    a = Sort(less)
    b = Sort(more)
    a.append(pivot)
    return a + b

print Sort()
