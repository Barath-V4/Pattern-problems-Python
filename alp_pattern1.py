n=int(input())
k=ord("A")
for i in range(n):
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
