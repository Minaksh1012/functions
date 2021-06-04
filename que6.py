# # Question 3 (Part 1)

# # Apko students naam ka ek function define karna hai or uss function mai list of students name as a parameter pass karna hai(List ka use nahi karna hai)
# def list_of_students(*names):
#     print("student list is",names)
# list_of_students("minakshi", "varsha" ,"namrata" ,"ayushi")

    


# Question 3 (Part 2)

# Apko isGreaterThen20 naam ka function define karna hai jismai apko function mai 
# do parameter pass karane hai or first parameter by default 20 hi hona chahiye.
def isGreaterThen20(x,y):
    if x>y:
        print(x,"is greater than ",y)
    else:
        print(y,"is greater than ",x)
isGreaterThen20(20,67)   
         


# def checkdiv(x,y):
#     if x>=y:
#         if x%y == 0:
#             print(x,"is divisible by",y)
#         else:
#             print(x,"is not divisible by",y)
#     else:
#         print("Enter first number greater than or equal to second number")

# checkdiv(4,2)
# checkdiv(4,3)
# checkdiv(2,4)
