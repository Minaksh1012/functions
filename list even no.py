# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi.
# Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] 
# Toh usko yeh output deni chaiye:

def is_even(x,y):
    i=0
    while i <len(x):
        if x[i]%2==0 and y[i]%2==0:
            print("dono even hai")
        else:
            print("dono even nahi hai") 
        i+=1     
is_even([2,6,18,10,3,75],[6,19,24,12,3,87])           