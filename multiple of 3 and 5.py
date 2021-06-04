def limit():
    num=int(input("enter the limit"))
    i=1
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
            
        i+=1
    print(sum,"sum")    
limit()            