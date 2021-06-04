def show_number():
    num=int(input("enter the limit of numbers"))
    i=0
    while i<num:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
show_number()                