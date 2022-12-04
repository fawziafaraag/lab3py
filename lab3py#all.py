# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:58:28 2022

@author: MaKaNaK
"""

"""
1- Using a list comprehension, create two new list called "newlist_1","newlist_2" out of the list "numbers", 
which contains only the positive numbers and negative number from the list, as integers.

"""
print('\n\n')
list_ = [-4,-3,-2,-1,0,1,2,3,4]
newlist_1 =[i for i in list_ if i<0]
newlist_2 =[x for x in list_ if x>=0]
print(newlist_1,"\n",newlist_2)

"""
2- Write program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
	Sample Dictionary ( n = 5) :
	Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
print('\n\n')
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

"""
3- Write a program to merge two Python dictionaries
"""
print('\n\n')
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

print({**dict_1, **dict_2})

"""

4- Write a function to generate all pairs from two lists
"""
print('\n\n')
c=[] 
def pair_two_lists(a,b) : 
     for i in a :
         for j  in b :
             c.append((i,j))
     return c
 
a ,b = [1, 2, 3],[4, 5, 6]
print(pair_two_lists(a,b))             



"""
5- rewrite this function using list comp.
"""
print('\n\n')  
def pair_two_lists(a,b) : 
      c = [(i,j)for i in a for j in b]    
      return c
a ,b = [1, 2, 3],[4, 5, 6]
print(pair_two_lists(a,b))


"""
6- convert 2D list to 1D -> flatten list and do it using list comp.
"""
print('\n\n')
lst_lsts = [[1,2],[3,7],[4,5,8],[9,11]]
lst = [i for lst in lst_lsts for i in lst]
print(lst)

"""
7- write function sort number don't use any built in function
"""
print('\n\n')
print(" write function sort number don't use any built in function ")

def sort_num(lst):
    for i in range(len(lst)):
       for j in range(i,len(lst)):
            if lst[i]>lst[j] :
                lst[i],lst[j]=lst[j],lst[i]
    return lst


lst =[2,15,10,3,50]
print(sort_num(lst))

"""
8- write function to get max pair in list
	ex-> lst =[2,15,10,3,50]
	out-> 15+50 = 65
then get min pair  
"""
print('\n\n')
lst =[2,15,10,3,50]

def max_pair (lst):
   lst=sorted(lst)
   return lst[len(lst)-1]+lst[len(lst)-2]

print(max_pair(lst))


def min_pair(lst):
   lst=sorted(lst)
   return lst[0]+lst[1]

print(min_pair(lst))

"""
9- write function to replace min and max inplace 
	ex -> lst = [4,1,3,10,8,10,10]
	out-> [4,10,3,1,8,1,1]
"""
print('\n\n')    
lst =[4,1,3,10,8,10,10]


def replace_min_max(lst) :
  max_=max(lst)
  min_=min(lst)
  for i in range(len(lst)):
        if lst[i] == max_:
            lst[i]= min_
        elif lst[i] == min_:
            lst[i] = max_
  return lst
   
print(replace_min_max(lst))
    
 






























