from math import factorial
inputs=input()
sum=0
for i in list(inputs):
    sum+=factorial(int(i))
    
if sum==int(inputs):
    print("Strong Number")
else:
    print("Not Strong Number")
