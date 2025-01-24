#Indexing
#
#it is applicable on the ordered immutable collections only (string, tuple, list)
#in indexing we have to pass 3 attributes
#1. name.index('obj') runs for 0 index to end index
#2. name.index('obj', start) runs for start index to end index
#3. name.index('obj', start, stop) runs for start index to stop (returns except current value or stop -1) index  #


#Types

#I- Positive indexing 
# starts with 0
# read direction left to right
# write direction left to right
#lenght = (end-1) 5-1=4   #

#II- Negative indexing
#starts with -1
# read direction right to left
# write direction left to right
# lenght= (end-1) -5-1=-6   



# 
# Example  #

#string=================

str1="python"
#print(str1.index('T'))

#print(str1.index('t'))

#print(str1.index('t',3))

#print(str1.index('o', 2, 4))

#print(str1.index('o', 2, 5))

#print(str1.index('o', 2))


#Slice=============================================================24/01/25

#syntax-----------
# collection[start: stop: step/direction]
# collection[start: stop]


#1.  findout direction of step
#(by default it is positive("+"ve) starts with 0 i.e., direction is positive)
#I- if step value is positive. i.e., positive direction.
#II- if step value is negative i.e., negative direction.


#2. findout start and stop 
#3- if 1 and 2 direction are matched then we get the answer output but if direction are not matched then we always get empth output.    #


s1="python"
#print(s1[:])
#print(s1[::])


#print(s1[1:4])
#print(s1[1:4:1])
#print(s1[1:4:2])


#print(s1[::-1])


#print(s1[-1:-5: -1])


str="i love python"
#print(str[-4:6: -1])
