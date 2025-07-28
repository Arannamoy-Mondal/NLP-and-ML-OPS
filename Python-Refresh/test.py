n=int(input("n:"))
l1=[]
sum=0
for i in range (0,n):
    input1=int(input("number:"))
    l1.append(input1)
    sum+=input1
print(l1)
print(sum/n)
l1=list(set(l1))
print(l1)