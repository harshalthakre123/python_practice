#1 airthmetic operator (// is floor, %, +, -, *, /, ** for power)
#2 Comparison operator (<, >, <=, >=, ==, !=)
#3 assignment operator (=, +=, -=)
#4 logical operator (&&, ||, not)

x=10
y=20
z=30

#print(not((x>y) and (y>z)))

#not is used for invert 
#logical operator returns boolean value.


#5 identity operator () [is, is not]
#python is call by reference , not call by value
a=10
b=20
#print(id(a))
#print(id(b))
#print( a is b)  #is operator compares the memory address. 
#print(id(a))
#print(id(b))

a=[10]
b=[10]
#print(a is b)
#print(id(a))
#print(id(b))



#6 membership operator ()

#to find out the character membership in the string or in other words character x is available in the string or not
# in , not in keywords are used to find out membership.
# used in all the collections (dictionary, list, string, frozenset)


str= "Harshal"
#print('a' in str)
#print('R'not in str)


#7 Bitwise operator [&- (and), |- (or), ^ - (x-or), << - (left shift), >> (right shift)]

#1- Binary-(0, 1) base is 2
#2- octal- (0-7) base is 8
#3- decimal (0-9) base is 10
#4- hexadecimal- (0-9), (A-F) or (a-f) base is 16


x=10
y=20
print(x & y) #and operator
print(x | y) # or operator
print(~x) #not operator
print(x^y)
print(x>>3)


