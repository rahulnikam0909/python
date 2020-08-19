#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#input


# In[1]:


ages=input('please enter age')


# In[2]:


ages


# In[3]:


name=input('please enter your name')


# In[4]:


name


# In[5]:


type(name)


# In[6]:


ages


# In[8]:


type(ages)


# In[12]:


ages=int(input('enter your age'))


# In[10]:


ages


# In[11]:


type(ages)


# In[13]:


ages=float(input('enter your age'))


# In[14]:


ages


# In[17]:


numbers=input('enter 5 number')


# In[18]:


numbers


# In[19]:


numbers=input('enter 5 nubmer').split()


# In[20]:


numbers


# In[21]:


numbers=input('enter 5 number').split()


# In[22]:


numbers


# In[25]:


numbers=input('enter 5 number').split(',')


# In[26]:


numbers


# In[27]:


numbers=input('enter 5 number').split(',')


# In[28]:


numbers


# In[30]:


numbers=[int(x) for x in input('enter 5 number').split(',')]


# In[31]:


numbers


# In[32]:


type(numbers)


# In[33]:


sum(numbers)


# In[35]:


detail=input('enter Name,age,ms,salary').split(',')


# In[36]:


detail


# In[37]:


type(detail)


# In[40]:


detail=[eval(x) for x in input('enter Name,age,ms,salary').split(',')]


# In[44]:


detail=[eval(x) for x in input('enter Name,age,ms,salary').split(',')]


# In[45]:


detail


# In[47]:


type(detail[0])


# In[48]:


type(detail[1])


# In[49]:


type(detail[2])


# In[50]:


type(detail[3])


# In[ ]:


#output


# In[51]:


print('hello')
print()
print('hi')


# In[52]:


print('hello \n all')


# In[53]:


print('hello \t hi')


# In[55]:


print('Rahul'+' '+'Nikam')


# In[56]:


#form
a,b,c=10,20,30
print('enter the value: ',a,b,c)


# In[58]:


print(a,b,c,sep=(':'))


# In[60]:


print('Hello',end=' ')
print('student',end=' ')


# In[62]:


print(10,20,30,50,40,80,sep=('/'),end='-----')


# In[2]:


a,b,c=10,20,30.5


# In[3]:


print('the value of b is %f'%b)


# In[4]:


print('the value of c is %i'%c)


# In[2]:


name = 'Rahul'
salary = 30000
company = 'Mercedes-Benz'
print('Hello', name, 'your salary is', salary,'and your comapany is', company)


# In[6]:


print('Hello {} your salary is {}  and your company is {}'. format(name,salary,company))


# In[7]:


print('Hello {} your salary is {}  and your company is {}'. format(company,salary,name))


# In[8]:


print('Hello {2} your salary is {1}  and your company is {0}'. format(company,salary,name))


# In[9]:


print('Hello {c} your salary is {s}  and your company is {n}'. format(n=name,s=salary,c=company))


# In[10]:


print('Hello {n} your salary is {s}  and your company is {c}'. format(n=name,s=salary,c=company))


# In[11]:


#Flow control
#If else
#For 
#While


# In[ ]:


if codition:
    output
else condition:
    output


# In[12]:


marks= int(input('enter your marks'))
if marks<35:
    print('ýou failed exam')
else:
    print('you passed exam')


# In[13]:


marks= int(input('enter your marks'))
if marks<35:
    print('ýou failed exam')
else:
    print('you passed exam')


# In[ ]:


if codition:
    output
elif codition:
    output
elif codition:
    output
else condition:
    output


# In[16]:


marks= int(input('enter your marks'))
if marks<35:
    print('ýou failed exam')
elif marks>=35 and marks<=60:
    print('you got average marks')
else:
    print('you got excellent marks')


# In[17]:


marks= int(input('enter your marks'))
if marks<35:
    print('ýou failed exam')
elif marks>=35 and marks<=60:
    print('you got average marks')
else:
    print('you got excellent marks')


# In[18]:


marks= int(input('enter your marks'))
if marks<35:
    print('ýou failed exam')
elif marks>=35 and marks<=60:
    print('you got average marks')
else:
    print('you got excellent marks')


# In[19]:


x=int(input('enter the number'))
if x%2==0:
    print('the number is even')
else:
    print('the number is odd')


# In[20]:


x=int(input('enter the number'))
if x%2==0:
    print('the number is even')
else:
    print('the number is odd')


# In[ ]:


#ForLoop


# In[ ]:


for codition:
    statement1
    statement2
statement3


# In[23]:


x= 'Rahul'
for a in x:
    print(a)
    print('HI')
print('Hello')


# In[24]:


name= 'The Mercedes'
count = 0
for x in name:
    print('before the loop')
    print(count)
    count = count+1
    print('after the loop')
    print(count)
    
print(count)


# In[25]:


sales=[2121,5512,3221,4562]
profit=[211,321,251,254]


# In[30]:


for i in range(0,len(sales)):
    print(profit[i]/sales[i])


# In[ ]:


#while loop
while condition:
    statement1
    statement2
statement3
    


# In[31]:


coupons = 5
utilized = 0
while utilized<6:
    print('total coupons left', coupons-utilized)
    utilized=utilized+1
print('no coupons left')
    


# In[ ]:


#operator


# In[ ]:


#Arithmatic operators
#Relational operators or comparision operators
#Logical operators
#Equality 
#bitwise
#Assignment 
#special


# In[ ]:


#Arithmatic operators

#+  addition
#-  subtraction
#*  multiplication
#/  division
#%  modulo(remainder)
#// floor division9(neariest int of quatient)
#** power


# In[1]:


a=10
b=3


# In[2]:


print('a+b',a+b)
print('a-b',a-b)
print('a*b',a*b)
print('a/b',a/b)
print('a%b',a%b)
print('a//b',a//b)
print('a**b',a**b)


# In[4]:


#relational operators
a = 50
b = 30
print('a>b',a>b)
print('a<b',a<b)
print('a>=b',a>=b)
print('a<=b',a<=b)


# In[5]:


#relational operators(ascii value based problem)
a = 'Rahul'
b = 'rahul'
print('a>b',a>b)
print('a<b',a<b)
print('a>=b',a>=b)
print('a<=b',a<=b)


# In[6]:


#Equality operator
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list1==list2


# In[7]:


list1!=list2


# In[8]:


#Equality operator
list1 = [1,2,3,4,5]
list2 = [12,2,3,4,5]
list1==list2


# In[9]:


list1!=list2


# In[10]:


10=='10'


# In[11]:


10==int('10')


# In[ ]:


#logical operators
and
or
not


# In[13]:


#non zero number true
#empty string false
#when 0 false
x = ''
y = 10
x and y


# In[14]:


x = 1
y = 10
x and y


# In[15]:


x or y


# In[16]:


y and x


# In[17]:


y or x


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




