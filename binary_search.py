#to search a value in a SORTED(increasing order) list.
#if list name is values and you are searching for x, use binarySearch(values, x)

def binarySearch(arr, value):
    
    #find the middle of the list
    m = len(arr)//2

    #value found
    if value == arr[m]:
        return True
    
    #list exhausted. value not found
    if len(arr)==1:
        return False
    if value<arr[m]:
        #if value less than middle value, binary search the left
        return binarySearch(arr[:m], value)
    if value>arr[m]:
        #if value greater than middle value, binary search the right
        return binarySearch(arr[m+1:], value)
