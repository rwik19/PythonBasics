arr = [1,6,7,8,2,5]
value = int(input("Enter value to be searched: "))
if value in arr:
    print(f"{value} found.")  
else:
    print(f"{value} not found.")