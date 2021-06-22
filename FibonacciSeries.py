#Fibonacci series
nterms=int(input())
count=0
n1=0
n2=1
while count<nterms:
    print(n1)
    nxt=n1+n2
    n1=n2
    n2=nxt
    count+=1
