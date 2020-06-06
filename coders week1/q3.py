#Using greedy algorithm, starting at a corner the rook can move clockwise(or, anti-clockwise) into the centre or in zig-zag fashion through the rows(or, columns).
#In either case the number of moves is 2N-1.
N = int(input('N = '))
print(2*N-1)