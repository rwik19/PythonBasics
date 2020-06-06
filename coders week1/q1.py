def isComplete(arr, flag = True):
    if len(arr) < 2:    #empty lists are taken as 'complete'
        return True
    elif arr[0] < arr[1]:
            return all(l < m for l, m in zip(arr, arr[1:])) #checks if list is strictly increasing
    elif arr[0] == arr[1]:
        return isComplete(arr[1:], False)
    elif flag:
        return isComplete(arr[1:])
    else:
        return False
arr = [int(item) for item in input("Enter the integers in the array (separate using blank spaces): ").split()]     
if(isComplete(arr)):
    print("Yes")
else:
    print("No")    