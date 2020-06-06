N = int(input("N(greater than 2) = "))
def valid(node, N): #check if square is inside board
        if node[0]<=N and node[1]<=N and node[0]>=1 and node[1]>=1:
            return True
        else:
            return False
def knight_shortest(start=(1,1), end=(N,N), N=N):
    moves = [(1,-2), (1,2), (-1,2), (-1,-2), (-2,1), (2,1), (2,-1), (-2,-1)]
    level_index = 0 #(number_of_moves - 1), root of tree is indexed as 0. each node in tree is a tuple representing a square.  
    level = [start]
    mem = {start}   #keep track of visited squares. do not go to same square twice.
    while(True):    #O(N^2)
        new_level = []
        for node in level:
            for move in moves:
                A = (node[0]+move[0], node[1]+move[1])
                if A == end:
                    return level_index + 1
                elif valid(A, N) and A not in mem:
                    new_level.append(A)
                    mem.add(A)
        level = new_level   #get rid of old level of tree, not relevant in this problem
        level_index+=1    
print(knight_shortest())