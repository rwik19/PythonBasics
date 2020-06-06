message = input(("Message: "))
k = int(input("k = "))
message = (message.upper()).replace(' ', '')
Z = ord('Z')
A = ord('A')
output = ''.join(chr((ord(x) + k - (Z+1))%26 + A) for x in message) #'Z'+1 maps back to 'A'
print(output)