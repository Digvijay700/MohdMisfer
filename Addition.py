#Writing a python program that accepts an integer n and computes the value n+nn+nnn
n=int(input("Enter a number"))

n1=int("%s" %n)
n2=int("%s%s" % (n,n))
n3=int("%s%s%s" % (n,n,n))

x=n1+n2+n3
print(x)