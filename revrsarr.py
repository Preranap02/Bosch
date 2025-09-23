import sys
def reversearr(A):
    return A[::-1]
data=sys.stdin.read().split()
N=int(data[0])
A=list(map(int,data[1:]))
revar= reversearr(A)
print(revar)
print(' '.join(map(str, revar)))