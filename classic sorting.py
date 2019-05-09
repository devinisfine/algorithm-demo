def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i-1
        temp = arr[i]
        while j>=0:
            if arr[j]>temp:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = temp
    return arr



def merge(arr,l,mid,r):
    left = arr[l:mid+1]
    right = arr[mid+1:r+1]
    k = l
    i = 0
    j = 0
    while k<= r and i < len(left) and j< len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def mergeSort(arr,l,r):
    if l<r:
        mid = (l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
    return arr



def quickSort(arr,l,r):
    if l>=r:
        return
    if l<r:
        pivot=arr[l]
        i = l
        j = r
        while i<j:
            while arr[j]>=pivot and i<j:
                j -= 1
            while arr[i]<=pivot and i<j:
                i += 1
            if i<j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        arr[l] = arr[i]
        arr[i] = pivot
    quickSort(arr,l,i-1)
    quickSort(arr,i+1,r)
    return arr

x=[1,7,6,5,4,3,100,99,200,33]
x=quickSort(x,0,len(x)-1)
print(x)
