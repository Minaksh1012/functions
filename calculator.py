# calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation. number_x aur number_y mein 
# hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge. 
# Jaise: * Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.

#     Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge.
#     Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
#     Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega

# Neeche kuch function calls ke examples diye hue hain: * calculator(20, 25, "add") call karne pe 45 returna karega. 45 hume 20+25 karne se milega.

#     calculator(40, 3, "subtract") call karne pe 37 return karega. 37 hume 40-3 karne se milega.
#     calculator(10, 4, "multiply") call karne pe 40 return karega. 40 hume 10*4 karne se milega.
#     calculator(40, 4, "divide") call karnse pe 10 return karega. 10 hume 40/3 karne se milega.

def calculator():
    a=int(input("enter the number"))
    b=int(input("enter the number")) 
    c=input("enter the symbol")
    if c=="+":
        e=a+b
        return(e)
    elif c=="-":
        f=a-b
        return(f)
    elif c=="*":
        g=a*b
        return(g)
    elif c=="/":
        h=a/b
        return(h)
    else:
        print("not")
e=calculator()
print(e)
f=calculator()
print(f)
g=calculator()
print(g)
h=calculator()
print(h)