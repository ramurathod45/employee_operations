### 1 write python program to PRINT DUPLICATE
# l=[11,22,55,4,77,88,22,11,66,55,3,66,44]
# d=[]
# for i in l:
#     if l.count(i)>1 and i not in d:
#         d.append(i)
# print(d)
### Ans:- [11, 22, 55, 66]

### 2. REMOVE DUPLICATE item from a list
### take only one time
# l=[11,22,55,4,77,88,22,11,66,55,3,66,44]
# d=[]
# for i in l:
#     if i not in d:
#         d.append(i)
# print(d)
###Ans [11, 22, 55, 4, 77, 88, 66, 3, 44]

### 3.INPUT:- "sky is blue"
### OUTPUT:- "blue is sky"
# a = "sky is blue"
# mylist = a.split()
# mylist = mylist[::-1]
# print(mylist)
# d = " , ".join(mylist)
# print(d)
# ##ANS :- blue is sky

### 4.find DUPLICATE AT TWO TIME
# l = [1,22,22,22,3,3,33,44,44]
# d=[]
# for i in l:
#     if l.count(i)==2 and i not in d:
#         d.append(i)
# print(d)
# #ANS:- [3, 44]

# ## 5.write a function to FIND COMMON letters
# # words in a word find {'i', 'c', 'k'}
# l={"Flick","lick","trick"}
# s1 = set.intersection(*map(set,l))
# print(s1)
# Ans {'i', 'c', 'k'}

# ## 6.write a SORT FUNCTIONS to sort the
# # element in a list
# l = [11,55,44,112,12,4,15,78]
# l.sort(reverse=True)
# print(l)
# #Ans:- [112, 78, 55, 44, 15, 12, 11, 4]

### 7 write a python to MULTIPLICATION TABLE
## of a given number using for loop
# num = int(input("enther the num:-"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
##Ans:-2*1=2
# #     2*2=4

# ## 8.FACTORIAL of a given number using for loop
# num=int(input("enter the num:-"))
# factorial = 1  ##1*1=1 , 1*2=2, 2*3=6 ....24*5=120
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"the factorial of {num} is {factorial}")
# #Ans the factorial of 5 is 120

##OR
##.FIND FACTORIAL
# import math
# n = int(input("enter the num:-"))
# result = math.factorial(n)
# print("factorial of",n,"is",result)
##ANS:-factorial of 5 is 120

# ## 8.create a LAMBDA function which will print the SUM
# from functools import reduce
# i=[5,8,10,20,50,44,100]
# sum=reduce(lambda x,y:x+y,i)
# print(sum)
# # #Ans 237
#
# # # 9.Palindrome of a string
# s =input("Enter a string:-")
# if(s==s[::-1]):
#     print("The given string is Palindrome")
# else:
#     print("The Given String is Not Palindrome")
# Enter a string:-radar
# The given string is Palindrome

# # PALINDROME IN STRING AND INT
# def ispalindrome(x):
#     x=str(x)
#     left,right=0,len(x)-1
#     while left<=right:
#         if x[left]!=x[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# print(ispalindrome(122))    # False
# print(ispalindrome("level")) # True

# # 10.REVERSE the string
# s=input("Enter the string:-")
# for i in s[::-1]:
#     print(i,end='')
# # Enter the string:-ramesh
# # hsemar
# # or
# s="ramesh"
# print(s[::-1])

## OR REVERSE for list
# s=(11,22,4,5)
# r=list(s)
# r.reverse()
# print(r)

# # 11.STAR pattern problems
# n = int(input("Enter the no. of row:-"))
# for i in range(1,n+1): #1 to 8
#      for j in range(1,n+1):
#          print(i,end="")
#      print()

# Enter the no. of row:-4
# 1111
# 2222
# 3333
# 4444

# 12.
# n = int(input("Enter the row:-"))
# for i in range(1,n+1):
#     # for j in range(1,n+1):
#      print(i,end="")
# print()

# n= 5
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print("*",end="")
#     print()
# # ****
# ***
# **
# *
#
# n=9
# for i in range(1,n+1):
#     for j in range(1,n+2-i): #1,9
#         print(n+1-j,end="")
#     print()

# 10987654321
# 1098765432
# 109876543
# 10987654
# 1098765
# 109876
# 10987
# 1098
# 109
# 10


# # 12.Remove first n characters from a string
# n="rameshwar"
# print(n[4:])

# # or without slicing
# def remove_char(word,n):
#     x = word[n:]
#     return x
# print(remove_char("rameshwar",4))

## 13. Print only EVEN INDEX characters
# word = input("enter the string:-")
# size = len(word)
# for i in range(0,size-1,2):
#     print("index[",i,"]",word[i])

# # or list slicing
# word = input("enter the string:-")
# x=list(word)
# for i in x[0::2]:
#     print(i)

# 14.
# n = int(input("Enter the number of rows:-"))
# for i in range(0,n+1):
#     print(" "*(n-i),end=" ") # 9 space,new line
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# Enter the number of rows:-10
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *
#     * * * * * *
#    * * * * * * *
#   * * * * * * * *
#  * * * * * * * * *
# * * * * * * * * * *

# for item in range(1,200):
#     print(item,chr(item))
# ans 44 ,
# 45 -
# 46 .
# 47 /
# 48 0
# 49 1
# 50 2
# 51 3
# 52 4
# 53 5

## 14.USE MAP FUNCTION

# def square(x):
#     return x*x
#
# l=[11,22,44,1,2,4]
# update=map(square,l)
# print(list(update))
# print(update)
## ans[121, 484, 1936, 1, 4, 16]
## ans<map object at 0x0000015DFACAB370>


# # 15.A Sample class with init method
# class Person:
#
# 	# init method or constructor
# 	def __init__(self, name):
# 		self.name = name
#
# 	# Sample Method
# 	def say_hi(self):
# 		print('Hello, my name is', self.name)
#
#
# p = Person('Nikhil')
# p.say_hi()

## 16.MAKE SIMPL DECORE FUNCTION

# def decor(func):
#     def inner():
#         func()  # call func
#         print("welcome to 3")
#
#     return inner
#
# @decor
# def printer():
#     print("welcome")
#     print("welcome")
# printer()

## 17.ADD TWO NUMBER
# def add(a,b):
#     return a * b
# print(add(12,5))
# ans 60

## 18.PRINT THE SUM OF THE CURRENT NUMBER AND THE PREVIOUS NUMBER
# privious_num = 0
# for i in range(1,11):
#     sum = privious_num + i
#     print("current number ",i,'previous number',privious_num,'sum:',sum)
#     privious_num = i

## 19.PRINT CHARACTERS FROM A STRING PRSENT AT EVEN INDEX NUMBER
# x = "pynative"
# l =len(x)#8
# for i in range(0,l-1,2):
#     print('index[',i,']',x[i])
#  ans
# index[ 0 ] p
# index[ 2 ] n
# index[ 4 ] t
# index[ 6 ] v

# # OR LIST SLICING
# y = 'pynative'
# v =list(y)
# for i in v[0::2]:
#     print(i)

## 20.REMOVE FIRST N CHARACTERS FROM A STRING
# X="RAMESHWAR"
# for z in X[3:]:
#     print(z,end='')

# # OR
# def remove_chars(word,n):
#     x = word[n:]
#     return x
# print(remove_chars("rameshwar",4))
# shwar

##OR
# n='rameshwar'
# x=n[4:]
# print(x)

## 21.FIRST AND LAST NUMBER IS SAME OR NOT
# y =[12,2,5,4,7,12]
# def same_list(y):
#     fist=y[0]
#     last=y[-1]
#
#     if fist == last:
#         return True
#     else:
#         return False
# print(same_list(y))

## OR
# x=[12,2,15,4,7,12]
# def fist_last(x):
#     if x[0]==x[-1]:
#         print("True")
#     else:
#         print("False")
# fist_last(x)

# # ANS = True

## 22. IS DIVISIBLE OR NOT
# x = [10,20,33,46,55]
# for i in x:
#     if i%5==0:
#         print(i)
# # ans
# #10
# # 20
# # 55

# # 23.PALINDROME OF A STRING:-
# S = input("enter the string")
# if s == s[::-1]:
#     print("given string is palindrome")
# else:
#     print("given string is not palindrome")

## 24.reverse the given string
#
# x= 'rameshwar'
# for i in x[::-1]:
#     print(i,end=" ")

## 25. SUM VALUE FROM THE DICT
# from functools import reduce
# d ={'ram':200,'shyam':100}
# s = reduce(lambda x,y:x+y,d.values())
# print(s)
# ANS 300

##26. pryamid pattern
# n = int(input("enter the row:-"))
# for i in range(1,n+1):   # 1 to 10
#     print(" "*(n-i),end="") # space * 9 , newline
#     for j in range(1,i+1): # 1 to 2,3,4
#         print(j,end=" ") # 1,2,3
#     print()

# enter the row:-10
#          1
#         1 2
#        1 2 3
#       1 2 3 4
#      1 2 3 4 5
#     1 2 3 4 5 6
#    1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8
#  1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10

## 27. DISPLAY UNIQUE VOWELS PRESENT IN THE GIVEN WORD
# vowels = ['a', 'e', 'i', 'o', 'u']
# s = input("enter the name:-")
# d = []
# for i in s:
#     if i in vowels and i not in d:
#         d.append(i)
# print(d)
## enter the name:-rameshwar rathod
# ['a', 'e', 'o']

## OR
# v = ['a','e','i','o','u']
# x = 'rameshwar rathod'
# v = set(v)
# print(v.intersection(x))

##  ans {'e', 'o', 'a'}

## 28.CREATE A NEW LIST FROM A TWO LIST USING THE
# FOLLOWING CONDITION

# list1 = [10,20,25,30,35]
# list2 = [40,45,60,75,90]
# def merge_list(list1,list2):
#
#     result_list = []
#     for i in list1:
#         if i%2 !=0:
#             result_list.append(i)
#
#     for j in list2:
#         if j%2 ==0:
#             result_list.append(j)
#     return result_list
#
# print("result list:",merge_list(list1,list2))
#
# ## ANS result list: [25, 35, 40, 60, 90]


## 29.MULTIPLICATION TABLE
# for i in range(1,11):
#    ## print(i)                ## 1 , 2
#     for j in range(1,11):
#     ## print(j)            ## 1 to 10 , 1 to 10
#         print(i*j, end=" ")  ## 1*(1..10), sameline  ,2*(1..10)
#     print("\t\t")

# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100

## 30.STAR PATTERN IN REVESE
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print(" ")

# * * * * *
# * * * *
# * * *
# * *
# *

## 31.
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(j,end=" ")
#     print()
#
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

## 32.SEPERATE NAME GIVE
# str1, str2, str3 = input("Enter three string").split()
# print('Name1:', str1)
# print('Name2:', str2)
# print('Name3:', str3)

# ANS Enter three string  rameshawr pralhad rathod
# Name1: rameshawr
# Name2: pralhad
# Name3: rathod

## 33.Print for using FORMATE FUNCTION
# print("I have {} dollars so I can buy{} football for {}".format({100},{200},{300}))


## 34. CALCULATE THE SUM OF ALL NUMBERS FROM 1 TO A
# GIVEN NUMBER
# n=int(input("enter the number:-"))
# s = 0
# for i in range(1,n+1,1):
#     s=s+i #1,3,6,10,15
# print("sum is :", s)
## ANS
# enter the number:-5
# sum is : 15

## or built in functionn sum
# n=int(input("enter the number:-"))
# x=sum(range(1,n+1))
# print("sum is :",x)

## 35.MULTIPLICATION OF 2 TABLES
# x=2
# for i in range(11):
#     r = x*i
#     print("multiplication is :-",r)

## 36.
# x = [12, 75, 150, 180, 145, 525, 50]
# for i in x:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
# ANS 75
# 150
# 145

## 37.WRITE A PROGRAM TO USE FOR LOOP TO PRINT THE FOLLOWING REVERSE NUMBER PATTERN
# n = 5
# k = 5
##  REVERSE THE STAR PATTERN
# for i in range(0,n+1):
#
#     for j in range(n-i,0,-1):
#         print(j,end=' ')
#     print()
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

## 38.FACTORIAL OF 5
# num = 5
# factorial = 1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(factorial)

# ANS 120

## 39.USE A LOOP DISPLAY ODD INDEX POSITIONS
# my_list = [10,20,30,40,50,60,70,80,90,100]
# for i in my_list[1::2]:
#     print(i,end=" ")
#  ANS 20 40 60 80 100

## 40.
# n = 6
# for i in range(n):
#     b=(i*i)
#     print(b,end=',')
# ANS = 0,1,4,9,16,25

## 41.SUM OF ALL VALUE
# l = [23,11,22,33]
# print(sum(l))
# # ANS 89

## 42.  *****
# x = {'red':2,'green':'4',
#      'blue':'5'}
#
# for key in sorted(x):
#     print(key,x[key],end=' , ')
#
#  ANS :- blue 5 , green 4 , red 2

### 43. PRINT FIRST 10 NATURAL NUMBERS
# i = 1
# while i <=10:
#     print(i)
#     i += 1
# ## OR
# for i in range(1,11):
#     print(i)

# 44.calculate the sum of all numbers from 1 to a
# given number
# n=10
# s=0
# for i in range(1,n+1,1):
#     s =s+i
# print(s)
# ## ANS: 55

## OR
# x=sum(range(1,11))
# print(x)
# ## ANS: 55

## 45.MULTIPLICATION TABLE OF A GIVEN NUMBER
# n = 2
# for i in range(1,11,1):
#     print(i*n)

## 46.
# n =[12,75,150,180,145,525,50]
# for i in n:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#
#     elif i % 5 == 0:
#         print(i)

## ANS
# 75
# 150
# 145

# 47.
# n=5
# for i in range(0,n+1):
#     for j in range(n-i,0,-1):
#         print(j,end='')
#     print()
# ans
# 54321
# 4321
# 321
# 21
# 1

## 48.
# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)

# ans
# 50
# 40
# 30
# 20
# 10

## 49.else block
# for i in range(5):
#     print(i)
# else:
#     print("DONE!")
#
# 0
# 1
# 2
# 3
# 4
# DONE!

## 50.find only even number
# for i in range(25,51,1):
#     if i%2!=0:
#         print(i)

## 51.factorial of 5
# import math
# n=5
# result =math.factorial(n)
# print(result)

## 52.FIBONACCI SERIES UP TO 10 TERMS
# num = 0
# num2= 1
# for i in range(10):
#      print(num, end=" ")
#     res = num+num2
#     num=num2
#     num2=res
# ANS 0 1 1 2 3 5 8 13 21 34

# ## 53.REVERSE
# N ="54984" #IT IS ONLY SUPPORTED BY STRING NOT LIST
# for i in N[::-1]:
#     print(i,end='')
# ## ans 48945

## 54.ODD NUMBER
# def odd_number():
#     for i in range(50):
#         if i%2!=0:
#             print(i)
# odd_number()

# 1
# 3
# 5
# 7
# 9

## 55.WRITE A PROGRAM TO PRINT THE CUBE OF ALL NUMBER
# FROM 1 TO A GIVEN NUMBER
# n=6
# for i in range(1,n+1):
#     print(f"Current Number is {i} and the Cube is {i**3}")
## ANS
# Current Number is 1 and the Cube is 1
# Current Number is 2 and the Cube is 8
# Current Number is 3 and the Cube is 27
# Current Number is 4 and the Cube is 64
# Current Number is 5 and the Cube is 125
# Current Number is 6 and the Cube is 216

## OR

# def cube(x):
#     return x**3
# print(cube(2))
#
# # ANS
# # 8

## 56.USE STAR PATTERN FOR LOOP TWO TIME
# num = 5
# for i in range(0,num):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range(num,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

## 57.create the function with two
## parameter name and age

# def person(name,age):
#     print(name,age)
# person("rameshwar",24)
# rameshwar 24

## 58.Create a function with variable length
## of arguments
# def func1(*args):
#     for i in args:
#         print(i)
#
# func1(00,949,22)
# UnicodeTranslateError
# 0
# 949
# 22

## 59.RETURN MULTIPLE VALUES FROM A FUNCTION

# def calculation(a,b):
#     return a+b,a-b
# print(calculation(40,10))

# ANS (50, 30)

## 60.CREATE A FUNCTION WITH A DEFAULT ARGUMENT
# def show_employee(name,sallary=9000):#9000 default argument
#     print("name:",name,"salary:",sallary)
#
# show_employee("ben",12000)
# show_employee("jessa")
##ANS
# name: ben salary: 12000
# name: jessa salary: 9000

## 61.create an inner function to calculate the
# addition in the following way

# def func(a,b):
#     squre = a**2
#     def inner(a,b):
#         return a+b
#     add = inner(a,b) #call inner function
#     return add + 5
# result =func(5,10)
# print(result)
# ans 20

## 62.print max value in list using function
# v=[11,22,33,55,11,44]
# def maxi(x):
#     print(max(x))
# maxi(v)
## ans 55

## 63.Generate a python list of all the even
# numbers betweeen 4 to 30
# def num():
#     print(list(range(4,30,2)))
#
# num()
## ans [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# 64.
# def sum_2(x):
#     print(sum(x))
# y=[11,22,55,44,6,4]
# sum_2(y)
# ans : 142

## 65.write lambda function for add and multiple
# r =lambda a,b:a+b
# print(r(10,5))
# result=lambda x,y:x*y
# print(result(10,5))
## ans 25
# 50

## 66.create lambda function with multiple by 15
# x=lambda x:x*15
# print(x(2))
# print(x(3))
# print(x(4))
# print(x(5))
#
# ans
# 30
# 45
# 60
# 75

## 67.write a python program to sort a list of tuples using lambda

# c=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# c.sort(key=lambda x:x[1])
# print(c)
#
# ans
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# #

# d=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# r=sorted(d,key=lambda x:x[1][-1],reverse=True)
# print(r)

# l="rameshwar rathod"
# print(len(l))

# 68.
# s = 'google.com'
# d=[]
# for i in s:
#     i.count()
#     print(d)

## 69.count the string how many time present

# st = 'google.com'
# ste = {}
# for i in set(st):
#     ste[i] = st.count(i)
# print(ste)
# {'e': 1, 'l': 1, 'o': 3, '.': 1, 'c': 1, 'm': 1, 'g': 2}

# OR
# from collections import Counter
# str="google.com"
# res=Counter(str)
# ret=dict(res)
# print(ret)
# ans {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# 70.from functools import reduce
# i = [12,32,54,1]
# s=reduce(lambda x,y:x*y,i)
# print(s)
# ans
# 20736

## or
# i = [12,32,54,1]
# d=1
# for n in i:
#     d=d*n
# print(d)

# import math
# n=5
# result =math.factorial(n)
# print(result)

# 71.** python program to interchange first
# and last elements in a list
# n=[18, 11, 9, 56, 12]
# def swaplist(x):
#     n[0],n[3]=n[3],n[0]
#     n[1],n[-1]=n[-1],n[1]
#     return x
# print(swaplist(n))
# ans [56, 12, 9, 18, 11]

## swap the two elements in the list ****
# list=[19,90,23,65]
# Output : [19, 65, 23, 90]
# #list=[23,65,19,90,45,21]
## [90,65,19,23,21,45]

# def swaplist(list,pose1,pos2,pose3,pose4):
#     list[pose1],list[pos2],list[pose3],list[pose4] = list[pos2],list[pose1],list[pose4],list[pose3]
#     return list
# print(swaplist(list,pose1=1,pos2=-1,pose3=0,pose4=0))

# ans
# [19, 65, 23, 90]

## 72.the given value present in list or not
# def r(x):
#     for i in test_list:
#         if 3 in test_list:
#             return True
#         else:
#             return False
# test_list = [1, 6, 3, 5, 3, 4]
# print(r(test_list))

# ans
# True

## 73.*** find second largest number
# list2 = [70, 11, 20,4, 4, 100]
# r=list(set(list2))
# r.sort()
# print(f"second largest number is :-{r[-2]}")
# ANS
# second largest number is :-70

# OR
# def second_largest(x):
#     r=list(set(x))
#     r.sort()
#     print(f"second largest num is:-{r[-2]}")
# y = [12,56,87,41,2]
# second_largest(y)

## 74.python program to print even number in a list
# x=[10,21,4,45,66,93]
# for i in x:
#      if i%2 == 0:
#          print(i,end=' , ')
# print()  ## this is for new line
# for j in x:
#     if i%2 !=0:
#         print(j,end=' , ')

## or
# li = [10,21,4,45,66,93]
# s =list(filter(lambda x: (x%2==0),li))
# print(s)

# ANS
# [10, 4, 66]

# list1 = [10, 21, 4, 45, 66, 93, 11]
# # we can also print even no's using lambda exp.
# even_nos = list(filter(lambda x: (x % 2 == 0),list1)
# print("Even numbers in the list: ", even_nos)

## 75.*** print positive number in a list
# list2 = [12, 14, -95, 3]
# for i in list2:
#     if i >0:
#         print(i,end=',')
# ans 12,14,3,

## or
# r =list(filter(lambda x:(x>=0),list2))
# print(r)
# ans
# [12, 14, 3]

## print negative number in the list
# l1=[121,12,-12,-44,-5,0]
# s=(filter(lambda x:(x<0),l1))
# print(list(s))
# ans
# [-12, -44, -5]

## 76.*** print pasitive and negative number
# l=[11,2,-2,11,-5,55,-3,-3]
# s=list(set(l))
# s.sort()
# for i in s:
#     if i>=0:
#         print(i,end=",")
# print()
# for j in s:
#     if j<=0:
#         print(j,end=',')

# ans
# 2,11,55,
# -5,-3,-2,

# OR
# l=[11,2,-2,11,-5,55,-3,-3]
# s=list(filter(lambda x: (x>0),l))
# print(s)
# d=list(filter(lambda x: (x<0),l))
# print(d)
# ans
# [11, 2, 11, 55]
# [-2, -5, -3, -3]

## 77.
# l=[11,2,-2,11,-5,55,-3,-3,5]
# s=list(set(l)) # duplicate deleted and return in list
# s.sort()
# k=1
# d=1
# for i in s:
#     if i>=0:
#         k=k+1 #,0+1=1 ,1+1=2
#     else:
#         d=d+1
# print("positive number is :+",k)
# print("negative number is :-",d)

##or
# g=len(list(filter(lambda x: True if (x>0) else False,l)))
# h=len(list(filter(lambda x: (x<0),l)))
# print(f"positive num is :+ {g}")
# print(f"negative num is :- {h}")
# ans
# positive num is :+ 5
# negative num is :- 4

## 78.delete in between 1 to 4 index
## x='rameshwar'  'str' object doesn't support item deletion
# x=[12, 15, 3, 10,45,12,3]
# del x[1:4]
# print(x)
# ans
# [12, 45, 12, 3]

## 79.wpp remove duplicate
## x='aaabbcdeffab'  ## ans ['a', 'b', 'c', 'd', 'e', 'f']
# x=[12, 15, 3, 10,45,12,15,12,3]
# d=[]
# for i in x:
#     if i not in d:
#         d.append(i)
# print(d)
# ans
# [12, 15, 3, 10, 45]

## 80.print duplicate
## for string x="aaabbbscccdd"   ### ans ['a', 'b', 'c', 'd']
# x=[12, 15, 3, 10,45,12,15,12,3]
# d=[]
# for i in x:
#     if x.count(i)>1 and i not in d:
#         d.append(i)
# print(d)
# ans [12, 15, 3]

## 80.find number between list
# test_list = [[4, 5, 5], [2, 7, 4],[1,5,45]]
   ###             0          1         2
# print("The original list is : ",test_list)
# print(test_list[2][2])
# ans
# 45

# 81.**
# test_list = [4, 5, 5, [2, 7, 4],[1,5,45]]
#         ##  0   1   2      3         4
# print(test_list[3][1])
# # ans
# 7

## 82.reverse the string ***
# test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
# for ele in test_list:
#     ele.sort(reverse=True)
# print("The reverse sorted Matrix is : ",test_list)
# ans
# The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
# The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]

# 83.
# from collections import Counter
# l="rameshwar pralhad rathod"
# r=Counter(l)
# d=dict(r)
# print(r)
## ans Counter({'a': 5, 'r': 4, 'h': 3, ' ': 2,

## 84.use *args parameter
# def func1(*args):
#     for i in args:
#         print(i)
#
# func1(20, 40, 60)
# func1(80, 100)
# ans
# 20
# 40
# 60
# 80
# 100

## 85.print **jms
# str1="james"
# for i in range(0,5,2):
#     print(str1[i],end="")
# ans
# jms

## 86.output Dip
# str1 = "JhonDipPeta"
# for i in range(4,7):
#     print(str1[i],end='')

## or
# str1 = "JhonDipPeta"
# for i in str1[4:7]:
#     print(i,end='')

## 87.output:- yaivePNT
# s="PyNaTive"
# d=[]
# f=[]
# for i in s:
#     if i.islower():
#         d.append(i)
#     else:
#         f.append(i)
# sorted_str ="".join(d + f)
# print("result is:-",sorted_str)
# result is:- yaivePNT

## 88.
## ****how many number of occerance present in the string
# s="aabbbbccccddddddeeee"
# for i in range(97,123):
#     j = chr(i)
#     count=0
#     for k in s:
#         if j==k:
#             count=count+1
#     if count >0:
#         print(j,":",count,end=" , ")
# ans
# a : 2 , b : 4 , c : 4 , d : 6 , e : 4 ,

### 89.*****
# d = "rameshwar pralhad rathod".split(' ')#split deduct space
# for g in d:                             ## # and return vertical line
#     ## print(g)  #rameshwar
#                 # pralhad
#                 # rathod
#     print(g[-1::-1],end=" ")
# ans
# rawhsemar dahlarp dohtar

##90.
# x="aaabbcccc"   ## output a:3 b:2 c:4
# for i in range(97,123):
#     d=chr(i)
#     count=0
#     for j in x:
#         if d==j:
#             count=count+1      ##1+1=2,2+1=3,3+1=4
#     if count>0:
#         print(d,":",count,end=" ")
## ans a : 3 b : 2 c : 4

## 90.1
# str1 = "Apple"
# # create a result dictionary
# char_dict = {}
# for char in str1:
#     x = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = x
# print('Result:', char_dict)
# ans
# Result: {'A': 1, 'p': 2, 'l': 1, 'e': 1}


## 91.*****
# a = "a4b3c2d4f6" ##output aaaabbbccddddffffff
# output ="" ## empty string for concatination
# for char in a:
#     if char.isalpha():
#         var=char     #  assign in var
#     else:
#         num=int(char)
#         output=output+(var*num)  ## concatinate string ""+a*3=aaa
# print(output)
# ans
# aaaabbbccddddffffff

## 92.
# *** input[1,2,3,4]
##     output[1,9]
# d=[1,2,3,4]
# s=[]
# s.append(d[0])
# g=0
# for i in range(1,len(d)):
##print(d[i]) ## means it start 2,3,4
#     g=g+d[i]   #0+2=2 ,2+3=5,5+4=9
# s.append(g)
# print(s)

## 93. ***seperate alphabet ,  digit and symbol
# a = "P@yn2at&#i5ve"
# def find_all_result(a):
#     char =0
#     num=0
#     symol=0
#     for i in a:
#         if i.isalpha():
#             char += 1
#
#         elif i.isdigit():
#             num += 1
#         else:
#             symol+=1
#     print(f"char is : {char} \n digit is :{num} \n symol is :{symol}")
# find_all_result(a)
# ans
# char is : 8
#  digit is :2
#  symol is :3

## 94.***find sum and average
# input_str = "PYnative29@#8496"
# total = 0
# cnt = 0
# for char in input_str:
#     if char.isdigit():
#         total = total+ int(char)
#         cnt += 1
#
# # #average = sum / count of digits
# avg = total / cnt
# print("Sum is:", total, "Average is ", avg)
## ans Sum is: 38 Average is  6.333333333333333

## 95. reverse the string
# str1 = "PYnative"
# print("Original String is:", str1)
# str1 = str1[::-1]
# print("Reversed String is:", str1)
# ans
# Reversed String is: evitanYP

## or
# str1 = "PYnative"
# print("Original String is:", str1)
# str1 = ''.join(reversed(str1))
# print("Reversed String is:", str1)

# 96.find a index 'Emma' name
# str1 = "is a data scientist who knows Python. Emma works at google."
# d=str1.rfind("Emma")
# f=str1.index("Emma")
# print(f) ##38
# print("index of Emma is :-", d)
# ans
# index of Emma is :- 38

## 97. how many time get usa
# str1 = "Welcome to USA. usa awesome, isn't it?"
# f=str1.lower()
# d=f.count("usa")
# print(d)
# ans
# 2

##98.
# import re
# target_str = "Jessa knows testing and machine learning".split()
# res_str = re.sub(r"\s", "_", target_str)
# # String after replacement
# print(res_str)
# # Output 'Jessa_knows_testing_and_machine_learning'

# 0r
# target_str = "Jessa knows testing and machine learning".split()
# x='_'.join(target_str)
# print(x)
# ans
# Jessa_knows_testing_and_machine_learning

## 99. remove white spaces
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# g=list(filter(None,str_list))
# print(g)
# ## ans
# ['Emma', 'Jon', 'Kelly', 'Eric']

## 100.replace symbol to #
# str1 = '/*Jon is @developer & musician!!'
# for i in string.punctuation:
#     str1=str1.replace(i,"#")
# print(str1)
# ans
##Jon is #developer # musician##

## 101. output :- My name is Kelly
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[]
# for i ,j in zip(list1,list2):
#     list3=i+j
#     print(list3,end=" ")
# ans
# My name is Kelly

## 102.Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# d=[]
# for i in numbers:
#     d.append(i*i)
# print(d)
# ans
# [1, 4, 9, 16, 25, 36, 49]

## or
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = [x * x for x in numbers]
# print(res)
# ans
# [1, 4, 9, 16, 25, 36, 49]

## 103.
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# for i in list1:
#     for j in list2:
#         print(i+j,end=' ,')

## or
# x=(x+y for x in list1 for y in list2 )
# print(list(x))
##ans
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

## ***104.
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i,j in zip(list1,list2[::-1]):
#     print(i,j)
#ans
# 10 400
# 20 300
# 30 200
# 40 100

## **105. remove spaces
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# d=filter(None,list1)
# print(list(d))
#ans
# ['Mike', 'Emma', 'Kelly', 'Brad']

##** 106.
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

##
# x=['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# sub_list = ["h", "i", "j"]
# x[2][1][2].extend(sub_list)
# print(x)
# #ans
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

## **106. replace 20 to 200
# list1 = [5, 10, 15, 20, 25, 50, 20]
# k=list1.index(20)
# list1[k]=200
# print(list1)
# ans
# [5, 10, 15, 200, 25, 50, 20]

## 107.***
# list1 = [5, 20, 15, 20, 25, 50, 20]
# d=[]
# for i in list1:
#     if i==20:
#         continue
#     print(i,end=", ")
## ans
## 5, 15, 25, 50,

# or
# c=list(i for i in list1 if i!=20 )
# print(c)
# ans
# [5, 15, 25, 50]

# or 2
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in list1:
#     if 20 in list1:
#         list1.remove(20)
# print(list1)
# ans
# [5, 15, 25, 50]

## 108.**
# aList = [5, 10, 15, 25,11,55,12,10]
# print(aList[::-2])
#ans
# [10, 55, 25, 10]

##109**
# sampleList = [10, 20, 30, 40]
# del sampleList[0:2]
# print(sampleList)
#ans
#[30, 40]

## 110*** write a program to remove duplicate characters
# from the given string
# a="ABACDACBDGE"
# d=[]
# for i in a:
#     if i not in d:
#         d.append(i)
# print(d)
## ans
# ['A', 'B', 'C', 'D', 'G', 'E']

## 111
# input= "a4b3c2"
# # output=aaaabbbcc
# for i in input:
#     if i.isalpha():
#         var=i
#     else:
#         num=int(i)
#         d=var*num
#         print(d,end='')
#ans
# aaaabbbcc

## 112. *** output :- ABD134
# c="B4A1D3"
# s1=''  ## BAD
# s2=''  ## 413
# output='' ### ABD134
# for i in c:
#     if i.isalpha():
#         s1+=i
#     else:
#         s2+=i
# for j in sorted(s1):
#     output+=j
# for k in sorted(s2):
#     output+=k
# print(output)
# #ans
# ABD134

#***************************TUPLE**********************

## 1.reverse a tuple
# t= (10, 20, 30, 40, 50)
# x=t[::-1]
# print(x)
#ans
# (50, 40, 30, 20, 10)

##*** 2. access value 20 from the tuple
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# # understand indexing
# # tuple1[0] = 'Orange'
# # tuple1[1] = [10, 20, 30]
# # list1[1][1] = 20
# print(tuple1[1][1])
# #ans 20

## 3. create a tuple with single value
# tuple1= (50,)
# print(type(tuple1))
#ans <class 'tuple'>

##** 4 modify the given tuple
# tuple1 = (11, [22, 33], 44, 55)
# x=tuple1[1][0]= 222
# print(tuple1)
# ans  (11, [222, 33], 44, 55)

#*** 5 sort a tuple of tuples by 2nd items
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# x=list(sorted(tuple1,key= lambda x: x[1])) ## x:x -> a,b,c,d
# print(x)
#ans [('c', 11), ('a', 23), ('d', 29), ('b', 37)]


#********************************_____SET_____*************************

# 1. add a list of element to a set
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
#
# sample_set.update(sample_list)
# print(sample_set)
#ans  {'Blue', 'Black', 'Orange', 'Red', 'Yellow', 'Green'}

## 2.Return a new set from two sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# d=set1.intersection(set2)
# print(d)
#ans   {40, 50, 30}

# 3.difference between two sets
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)
#ans {10, 30}

#4. remove 10,20 and 30 in a set
# set1 = {10,20,30,40,50}
# d=set1.difference({10,20,30})
# print(d)
# ans {40, 50}

# 5.
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# f=set2.symmetric_difference(set1)
# print(f)
# ans {20, 70, 10, 60}

# 6.use isdisjoint method it is not allow common ele
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
## print(set1.isdisjoint(set2)) # False 10 present in both list
# if set1.isdisjoint(set2):
#   print("Two sets have no items in common")
# else:
#   print("Two sets have items in common")
#   print(set1.intersection(set2))
# ans
# Two sets have items in common
# {10}

## 7.use issubset method if set1 ele present in set2 it return True
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 10, 30, 40, 80, 20, 50}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# ans True
#     True

## 8.*** Sorting a set
# set1 = {20, 4, 6, 10, 8, 15}
## print(max(set1))
## sorted_list = sorted(set1,reverse=True)  #it return reverse a set
#                                             {4, 6, 8, 10, 15, 20}
# sorted_list = sorted(set1)
# sorted_set = set(sorted_list)
# print(sorted_set)
# output {4, 6, 8, 10, 15, 20}

###*****************______Dict______**********

# 1.*** convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# x=dict(zip(keys,values))
# print(x)
#ans {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# OR *** without built in method zip
# x = ['Ten', 'Twenty', 'Thirty']
# y = [10, 20, 30]
# #          empty dictionary
# res_dict = dict()
# for i in range(len(x)):  ## ten , twenty , thirty
#     res_dict.update({x[i]: y[i]}) # ten:10 , twenty:20
# print(res_dict)
# ans {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

##2.*** merge dictionaries
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict2,**dict1}
# print(dict3)
# ans
#{'Thirty': 30, 'Fourty': 40, 'Fifty': 50, 'Ten': 10, 'Twenty': 20}

# OR with update()
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)  ## not use any variable x=dic..
# print(dict1)
# ans
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

##3.*** nested dictionary find 80 (access)
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])
# ans 80

# or access by value with slicing
# d = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# print(d['Thirty']) #30 only take key not take value
# print(d['Fourty']) #40
## print(d[50])    # key error

# d['seven']=7   # add to dic
# print(d)      #{'Thirty': 30, 'Fourty': 40, 'Fifty': 50, 'seven': 7}

# del d['Thirty']   # delete Thirty
# print(d)          # {'Fourty': 40, 'Fifty': 50, 'seven': 7}

## it give keys
# print(d.keys())   ##  dict_keys(['Fourty', 'Fifty', 'seven'])

## it give values
# print(d.values())   ##dict_values([40, 50, 7])


## 4. initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# r=dict.fromkeys(employees,defaults)
# print(r)
# # ans
# {'Kelly': {'designation': 'Developer', 'salary': 8000},
#  'Emma': {'designation': 'Developer', 'salary': 8000}}

# 5.*** delete a key "name" and "salary"
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# d=["name","salary"]
# for i in d:
#     sample_dict.pop(i)
# print(sample_dict)
# ans
# {'age': 25, 'city': 'New york'}

# 6.** check if a value present in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')
# # ans 200 present in a dict
# if "a" in sample_dict.keys():
#     print("a is present in dict")
# # ans a is present in dict

# 7.change key name and replace another
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict["location"]=sample_dict.pop("city")
# print(sample_dict)
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

# 8.** find the minimum value from given dict
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# d=min(sample_dict)
# print(d)   # math
# f=max(sample_dict)
# print(f)   # history


# 9. change value from given dict
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
# #
# sample_dict['emp3']['salary'] = 10000
# print(sample_dict)
#ans
# {'emp1': {'name': 'Jhon', 'salary': 7500},
#  'emp2': {'name': 'Emma', 'salary': 8000},
#  'emp3': {'name': 'Brad', 'salary': 10000}}

# 10. use items -> it return key-value pairs in tuple
# d = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# for k , v in d.items():
#     print(k,"-",v)
#ans
# Physics - 82
# Math - 65
# history - 75

# use of d.get
# d = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# x=d.get('Physics')
# print(x)  #  ans 82

# 10.*** find number of occurrences of each letter
# present in the given string
# word = input("enter the string:-")
# d={}
# for x in word:
#     d[x]=d.get(x,0)+1
# for k ,v in d.items():
#     print(k,"occurred",v,"times")

# ans
# a occurred 3 times
# b occurred 3 times
# c occurred 2 times
# d occurred 2 times
# e occurred 1 times
# s occurred 1 times
# f occurred 1 times


#****************************************************************
# def greater_charecter(x):
#     d={}
#     for x in x:
#         d[x]=d.get(x,0)+1
#     # print(d)  ## {'a': 2, 'b': 4, 'c': 7, 'd': 2}
#     for k,v in d.items():
#         print(k,"occured",v,"time")
# x = "aabbbbcccccccdd"
# greater_charecter(x)
#  ans  a occured 2 time
# b occured 4 time
# c occured 7 time
# d occured 2 time


# 0r
# from collections import Counter
# x="aaaaaabbbcccc"
# d=Counter(x)
# print(d)

# greater_charecter(x)
#ans
# a occured 6 time
# b occured 3 time
# c occured 4 time


# # ****output ['t', 'h', 'e', 'th', 'the']
# x="the"
# d=[]
# for i in x:
#     if i not in d:
#         d.append(i)
# k="th","the"
# d.extend(k)
# print(d)
# ans
# ['t', 'h', 'e', 'th', 'the']

## ***output [2, 5, 1, 4, 3]
# p=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# d=[]
# for i in p:
#     for j in i:
#         if j not in d:
#             d.append(j)
# k=sorted(d)
# print(k)
#  ans [1, 2, 3, 4, 5]

## ***
# n=[[10,20,30],[11,45,36],[11,22,33]]
# for i in range(len(n)): ##len(n)=3 and len(n[i]) = 3
#     ## print(i)   # 0 :->0,1,2  1:-> 0,1,2  2:->0,1,2
#     for j in range(len(n[i])):  # len(n[i]) = 3
#       ## print(j)    # 0,1,2   0,1,2   0,1,2
#       print(n[i][j],end=' ')
#     print()
# ans
# 10 20 30
# 11 45 36
# 11 22 33


## change value in the tuple
# it is possible b'couse inear side present list
# s=(10,20,30,[10,22])
# s[3][0]=444
# print(s)  ##(10, 20, 30, [444, 22])

## remove duplicate for nested list
# test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
# 						[1, 2, 3], [3, 4, 1]]
# res1 = []
# for i in test_list:
# 	x=sorted(i)
# 	res1.append(x)
# res=[]
# for i in res1:
# 	if tuple(i) not in res:
# 		res.append(tuple(i))
# print("The list after duplicate removal : ", res)
## ans The list after duplicate removal :  [(-1, 0, 1), (1, 2, 3), (1, 3, 4)]

## **** how many number are occured
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print("Original list ", sample_list)
#
# count_dict = dict()
# for item in sample_list:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
#
# print("Printing count of each item  ", count_dict)
## ans Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

##** merge two list
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# x=list(zip(first_list,second_list))
# print(x)
## ans
# [(2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)]











