#Literals-----
#constant value of any variable or constant data is known as literals.
#x=10,  #10 is literal.


#types of literals


#1-numeric( integer, float, complex)


#2-string-- it is a collection of characters 

# string is represented in single quotes(' '), double quotes(" ")and triple quotes("' '")

#single line String
x='H'
#print(x)
#print(type(x))
y="H"
#print(x)
#print(type(y))
#multiple line string
z='''H'''
#print(x)
#print(type(z))

#example of multiple line

a='''
    *
   ***
  *****
 *******
*********'''
#print(a)

b=''' this 
    is
     python
            class'''
#print(b)

#3- List----------------

#collection of objects
#list is represented by square brackets [] with comma (,) separated objects.
#object-
#I-homogenous(same data types)
#II-heterogenous(different data types)

h=[10, 12.5, 10+2j, "Harshal", [10, 20, 30, 40]]
#print(h)
#print(type(h)) #output is <class 'list'>


#4 Dictionary----


#5- Tuple------


#6-Set


#7.Boolean--


#8- frozen-set

#it is immutable but it have different memory address(because it is unordered).
fset1= frozenset({"Harshal", 10, 20, "Thakre"})
fset2= frozenset({"Harshal", 10, 20, "Thakre"})
#print(id(fset1)) 
#print(id(fset2))
#print(type(fset1))

