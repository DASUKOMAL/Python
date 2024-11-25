#program to display the multiplication table of a given number

num=int(input("Enter a number"))
for i in range(1,11):
    res = num*i
    print(f'{num}X{i}={res}')
