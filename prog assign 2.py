#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?
1 kilometer equals 0.62137 miles.
# In[13]:


#convert kilometer into miles

kilometers = float(input('How many kilometers?: '))
convert = 0.62137 
miles = kilometers * convert  
print(f"{kilometers} kilometer is equal to {miles} mile")


# 2. Write a Python program to convert Celsius to Fahrenheit?

# In[19]:


#convert Celsius to Fahrenheit
celsius = float(input("enter the temperature in celsius: "))  
fahrenheit = (celsius * 1.8) + 32  
print(f" {celsius} celsius is equal to {fahrenheit} degree Fahrenheit %(celsius,fahrenheit)")  


# 3. Write a Python program to display calendar?

# In[21]:


import calendar    
yy = int(input("Enter year(yyyy): "))  
mm = int(input("Enter month(1-12): "))   
print(calendar.month(yy,mm))  


# 4. Write a Python program to solve quadratic equation?

# In[24]:


# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculation  
d = (b**2) - (4*a*c)  
    
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   


# 5. Write a Python program to swap two variables without temp variable?

# In[27]:


a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 

