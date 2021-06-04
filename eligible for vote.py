# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote de sakta hai ya nahi. ( Consider minimum age of voting to be 18. )

# Example:-

# Agar user input me 18 se kam deta hai to “not eligible “ print kare aur agar user 18 ya 18 se jyaada input kare to “you are eligible” print kare.

# Input:-

# 18
# 16

# Output :-

# “you are eligible”
# “not eligible”


def eligible_for_vote():
    age=int(input("enter the age"))
    if age>=18:
        print("eligible_for_vote")
    else:
        print("not eligible_for_vote") 
eligible_for_vote()         

