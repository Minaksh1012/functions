# Ek function define karo jo ki 
# input me 2 strings lega aur dono strings me se jiski length jyaada hogi use 
# print karega aur agar dono strings ki 
# length equal hui to dono ko line by line print karega .
#  Hint :- use len() builtin function..

# Input:-

# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)

# Output :-

# welcome

# sonu
# monu


def name(name1,name2):
    if len(name1)==len(name2):
        print(name1,name2)
    elif len(name1)>len(name2):
        print(name1)
    else:
        print(name2)        
name("hello","welcome")


name("monu","sonu")    