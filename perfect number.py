# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana hai ki vo perfect number hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print kare.[ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number ke barabar hota hai.

# Example:-

#  6 ek perfect number hai 6=1+2+3.

# Expected Output :-

# 6,28,496


# def perfect():
#     n= int(input("Enter any number: "))
#     sum1 = 0
#     for i in range(1, n):
#         if(n % i == 0):
#             sum1 = sum1 + i
#     if (sum1 == n):
#         print("The number is a Perfect number!")
#     else:
#         print("The number is not a Perfect number!")
# perfect()    



def perfect():
    n=int(input("enter any number"))
    sum1=0
    i=1
    while i<n:
        if (n%i==0):
            sum1=sum1+i
        i+=1
    if (sum1==n):
        print("the number is perfect square")
    else:
        print("number is not perfect square")
    # i+=1    
perfect()        
