n = input("Enter a credit card number: ")
if len(n)<12 or len(n)>17 or not(n.isdigit()):
    print("This is not a valid credit card.")
else:
    x = ''
    for i in range(len(n)-2,-1,-2):
        x+= str(2*int(n[i]))
    for i in range(len(n)-1,-1,-2):
        x+= n[i]
    x = [int(i) for i in x]
    sum = sum(x)
    if sum%10==0:
        print("This may be a valid credit card.")
    else:
        print("This is not a valid credit card.")