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

str1="python"
print(str1.index('T'))

print(str1.index('t'))

print(str1.index('t',3))

print(str1.index('o', 2, 4))

print(str1.index('o', 2, 5))

print(str1.index('o', 2))