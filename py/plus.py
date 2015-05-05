x = raw_input("please input")
a = x.split(" ")
if a[1] == "+":
    p = int(int(a[0])) + int(int(a[2]))
if a[1] == "-":
    p = int(a[0]) - int(a[2])
if a[1] == "*":
    p = int(a[0]) * int(a[2])  
if a[1] == "/":
    p = int(a[0]) / int(a[2])
if a[1] == "%":
    p = int(a[0]) % int(a[2])
if a[1] == "**":
    p = int(a[0]) ** int(a[2])
print p


    
    
