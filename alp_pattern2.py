n=int(input())
for i in range(n):
    k=ord("A")+i
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
