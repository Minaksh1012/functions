# Ek function define kijiye jo ki drivers ki speed check karega. 
# Aur ye function speed naam ka ek parameter lega. 
# 1. Agar speed 70 se kam hai to ye “ok” print karega.

#     Agar driver ki speed 70 se jyaada hai to function use har 5 km 
# ke liye 1 point dega (ye 70 ko count nahi karega).

#     example ke liye agar speed 80 hai to print karega “points:2” .

#     Agar driver ko 12 points se jyaada points milte hai to 
# , function “License suspended” print karega.

def  speed(speed):
    speed=int(input("enter the speed"))
    if speed <=70:
        print("ok")
        # print("point:3")
    elif 70<speed:
        s=speed-70
        point=s/5
        print("point=",point)   
        if point>12:
            print("license suspended")

speed(speed)