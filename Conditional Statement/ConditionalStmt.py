#if===========================================================================
# n= int(input("Enter any number:"))

# if (n%2==0):  #if is complete by itself but if we want to use elif and else we need to use if and then else and #elif.
#     print(f"{n} even number") #or print("even no=", n)
# print("Hello")



#2. if-else===========================================================
# age= int(input("enter your age:"))

# if(age>=18):
#     print("Eligible for voting")
# else:
#     print("not eligible")    


#3.  nested if========================================================================================
# to avoid  nesting we use if-elif-else int the code 

# 4. if-elif=============================================================================


#Calculator=========================================================
# a= int(input("Enter number1:"))
# b= int (input ("Enter number2:"))
# solution= int (input('''press-1 for addition
# press-2 for subtraction
# press-3 for division
# press-4 for multiplication:'''))

# if(solution==1):
#     print("sum is:", a+b)
# elif(solution==2):
#     print("subtraction is:", a-b)
# elif(solution==3):
#     print("Division is:", a/b)
# elif(solution==4):
#     print("product is:", a*b)
# else:
#     print("Invalid input")


#Percentage==============================================================
percent= int(input("Enter your percentage:"))

if(percent>=60):
    print("Pass with A-grade.")

elif(percent<60 and percent>=51):
    print("Pass with B-grade.")

elif(percent<=50 and percent>=41):
    print("Pass with c-grade.")
elif(percent<=40 and percent>=33):
    print("Pass with D-grade")
else:
    print("Fail")