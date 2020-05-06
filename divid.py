#lets do it

import math

def minmax_divid(L,U,arr):
    a_min = arr[L]
    a_max = arr[U]

    if(L==U):
        a_min = a_max = arr[L]
        return(a_min,a_max)
    elif (U==L+1):
        if(arr[L]<arr[U]):
            a_min=arr[L]
            a_max=arr[U]
        else:
            a_min=arr[U]
            a_max=arr[L]
        return (a_max, a_min) 
    else:
        mid = int((L+U)/2)
        a_min1,a_max1 = minmax_divid(L,mid,arr)
        a_min2,a_max2 = minmax_divid(mid+1,U,arr)
    return (min(a_min1,a_min2), max(a_max1,a_max2))
