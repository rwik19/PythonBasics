def main():
    arr = [1,2,3,4,5,6,7,8]
    value = int(input("Enter a value to be searched: "))
    print(binarySearch(arr, value))

def binarySearch(arr, value):
    m = len(arr)//2
    if value == arr[m]:
        return True
    if len(arr)==1:
        return False
    if value<arr[m]:
        return binarySearch(arr[:m], value)
    if value>arr[m]:
        return binarySearch(arr[m+1:], value)

main()