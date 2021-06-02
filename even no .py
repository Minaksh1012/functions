# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono 
# numbers even(2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"


def check_numbers(num1,num2):
    if num1%2==0 and num2%2==0:
        print("dono number even hai")
        # print()
    else:
        print("these no are not even numbers") 
check_numbers(56,8)           