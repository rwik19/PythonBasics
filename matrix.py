def main():
    A = [[1,0,2],[3,1,1],[0,0,2]]
    B = [[2,1,0],[1,3,1],[2,0,1]]
    print(subMatrix(A,0,1))

def Sum(A,B):
    if len(A)==len(B) and len(A[0])==len(B[0]):
        return [list(map(sum,zip(*row))) for row in zip(A,B)]
    else:
        return False

def scalarMultiply(c,A):
    return [list(map(lambda a: c*a, row)) for row in A]

def transpose(A):
    return list(map(list,zip(*A)))

def product(A,B):
    if len(A)==len(B[0]):
        return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    else:
        return False

def subMatrix(A,i,j):
    X = A
    del(X[i])
    X = transpose(X)
    del X[j]
    return transpose(X)

main()