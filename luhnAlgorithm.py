#implement Luhn's Algorithm on n

n = input("Enter a credit card number: ")

#reject if n has less than 12 or more than 17 digits
if len(n)<12 or len(n)>17 or not(n.isdigit()):
    print("This is not a valid credit card.")
else:
    x = ''
    for i in range(len(n)-2,-1,-2):#start from 2nd last digit and go to the left, selecting alternate digits.
        x+= str(2*int(n[i]))
    for i in range(len(n)-1,-1,-2): #select rest of the digits
        x+= n[i]
    
    sum = sum(map(int,x))
    
    if sum%10==0:
        print("This may be a valid credit card.")
    else:
        print("This is not a valid credit card.")