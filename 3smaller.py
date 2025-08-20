a = int(input("Enter your first number:"))
b = int(input("Enter your scond number:"))
c = int(input("Enter your third number:"))

if a < b and a < c:
    print("smallest number is-",a)
    
elif  b< a and b < c:
    print("smallest number is-",b)
    
else:
    print("smallest number is-",c)