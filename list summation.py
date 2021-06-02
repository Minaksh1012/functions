# Question (Part 2)

# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale integers ka sum print karta ho. 
# Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi add_numbers waale function ka use karo. 
# Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega

def add_number_list(sum1,sum2):
    # sum1=[50,60,10]
    # sum2=[10,20,13]
    i=0
    sum=0
    while i<len(sum1):
        s=sum1[i]+sum2[i]
        print(s)
        i=i+1
add_number_list([50,60,10],[10,20,13])