n = input("Enter any positive integer: ")
n += 'x'
output = ''
count = 1
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count+=1
    if n[i]!=n[i+1] or i==len(n)-2:
        output += str(count) + n[i]
        count = 1
print(output)   