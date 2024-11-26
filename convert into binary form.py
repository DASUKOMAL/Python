#program to convert the Deciemal number to binary.

n=int(input("Enter the number"))
binary=0
while n>0 :
    r=n%2
    n=n//2
    binary=binary+(r*P)
    p=p*10
print(f' the brinary representation is {binary}')
