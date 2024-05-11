number=int(input("Enter a number: "))
n1=number//1000
print (n1)
n2=number//100%10
print (n2)
n3=number//10%10
print (n3)
n4=number%10
print (n4)
result=n1+n2+n3+n4
print ("Result",result)