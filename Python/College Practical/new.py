a = int(input("Enter The First Number = "))
b = int(input("Enter The Secound Number = "))
c = int (input("Enter The Theard Number = "))
if((a > b) and (a > c)):
    print("Biggest Number is ",a)
    if(b < a) and (b < c):
        print("Smaller Number is ",b)
    
    else:
        print("Smaller Number is ",c)
    
elif(b > c) and (b > a):
    print("biggest NUmber is ",b)
    if(c < b) and (c < a):
        print("Smaller Number is ",c)
    else:
        print("Smaller Number is ",a)
    
else:
    print("Biggest Number is ",c)
    if(a < c) and (a < b):
        print("Smaller Number is ",a)
    else:
        print("Smaller Number is ",b)
