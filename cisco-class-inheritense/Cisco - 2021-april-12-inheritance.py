#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. What is inheritance?
# 2. Reminder: Attributes + ICPO
# 3. Simple inheritance
# 4. `super()` and
# 5. Three paradigms for method inheritance
# 6. Multiple inheritance

# In[1]:


class Publication:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
p = Publication('My Book', 100)        


# In[2]:


p.name


# In[3]:


p.price


# In[4]:


# DRY -- don't repeat yourself!


# # Two types of relationships in object-oriented programming
# 
# 1. `has-a`: aka "composition." Means: One object contains another.  Publication has-a name. Publication has-a price. 
# 
# 2. `is-a`: aka "inheritance." Means: The child class is just like the parent class, except where otherwise specified. We can take advantage of the work that someone else has done on the parent class.

# # What are attributes?
# 
# Simplest definition: Every object has a private dictionary, its attributes. We can access these via ".".
# 
# Example:
# 
# ```python
# i = 10
# print(i.real)   # real_part is an attribute on "i"
# ```
# 
# An attribute can contain any type of data in Python. That includes strings, lists, and tuples, but also functions, modules, and classes.
# 
# With the exception of built-in types (strings, lists, etc), we can add any attribute we want to any object, whenever we want.

# In[7]:


i = 10
print(i.real)


# In[8]:


vars(p)  # what are the attributes of p?


# In[9]:


p.self_published = True

vars(p)


# In[11]:


p.self_published  # does p have an attribute self_published?  True


# In[12]:


s = 'abcd'
s.upper()  # call the "upper" method on s


# In[13]:


# First, Python turns to the instance and asks: Do you have an attribute?
#  If so, then we get the value back
# If not, then Python turns to the instance's CLASS.  And it asks: Do you have
#  the attribute?


# In[15]:


# s.upper -> str.upper(s)

str.upper(s)


# # Search path for attributes
# 
# - `I` instance (i.e., check on the object that we wanted to get it from)
# - `C` class (i.e., the type of object that the instance is)
# - `P` parents (i.e., the parent classes of our class)
# - `O` object (i.e., the top of our entire object hierarchy)

# In[16]:


class Person:
    def __init__(self, name):   # Person.__init__
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'   # Person.greet
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


# In[17]:


class Person:
    def __init__(self, name):   # Person.__init__
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'   # Person.greet
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):
    def __init__(self, name, id_number):   # Person.__init__
        self.name = name
        self.id_number = id_number
        
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())


# # Exercise: Products
# 
# 1. Define a `Product` class, in which each product has a name and a price. Those should be attributes on each individual instance.
# 2. Define a `TaxedProduct` class, in which each product has a name, price, and tax amount. 
# 3. There should be a `get_invoice` method on `Product`, which returns a string containing the name of the product and the current price. 
# 4. Implement these classes, and *don't* implement `get_invoice` on `TaxedProduct`. And yes, that means the invoice will be wrong!

# In[20]:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_invoice(self):
        return f'{self.name} costing {self.price}'
    
p = Product('apple', 1)
vars(p)


# In[21]:


p.get_invoice()


# In[22]:


class TaxedProduct(Product):
    def __init__(self, name, price, tax_amount):
        self.name = name
        self.price = price
        self.tax_amount = tax_amount
        
tp = TaxedProduct('phone', 500, 0.1)
tp.get_invoice()


# In[ ]:





# In[27]:


class Person:
    def __init__(self, name):   # Person.__init__
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'   # Person.greet
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):
    def __init__(self, name, id_number):   # Person.__init__
        # Person.__init__(self, name) 

        super().__init__(name)
        self.id_number = id_number
        
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())


# In[24]:


vars(e1)


# In[25]:


vars(e2)


# In[28]:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_invoice(self):
        return f'{self.name} costing {self.price}'
    
p = Product('apple', 1)

class TaxedProduct(Product):
    def __init__(self, name, price, tax_amount):
        super().__init__(name, price)
        self.tax_amount = tax_amount
        
tp = TaxedProduct('phone', 500, 0.1)
tp.get_invoice()


# # Exercise:  Improve + differentiate our products
# 
# Improve the `__init__` situation for Product vs. TaxedProduct, using `super()`.
# 

# # Three paradigms for method inheritance
# 
# 1. Do nothing in the child class, and use the implementation in the parent class
# 2. The method in the child class invokes the parent class's method, and then adds its own functionality as well.
# 3. Have a method in the child class that overrides the parent class's method or creates new functionality not found in the parent.

# In[30]:


class Person:
    def __init__(self, name):   # Person.__init__
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'   # Person.greet
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):
    def __init__(self, name, id_number):   # Person.__init__
        # Person.__init__(self, name) 

        super().__init__(name)
        self.id_number = id_number
        
    def employee_badge(self):
        return f'Name: {self.name}\nID: {self.id_number}\n'
        
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())
print()
print(e1.employee_badge())


# # Exercise: Include the tax
# 
# Define a new `get_invoice` method on the child (`TaxedProduct`) class, which will return an invoice that shows the price, the tax, and the total.  This method should override the `get_invoice` method that we had on the original `Product` parent class.

# In[34]:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_invoice(self):
        return f'{self.name} costing {self.price}'
    
p = Product('apple', 1)

class TaxedProduct(Product):
    def __init__(self, name, price, tax_amount):
        super().__init__(name, price)
        self.tax_amount = tax_amount
        
    def get_invoice(self):
        return f'''
        Product: {self.name} 
        Price: {self.price}
        Tax: {self.tax_amount * self.price}
        Total: {self.price + self.tax_amount * self.price}
        '''
        
tp = TaxedProduct('phone', 500, 0.1)
print(tp.get_invoice())


# In[35]:


TaxedProduct.__bases__  # this is where Python stores the inheritance info


# In[36]:


class A:
    def __init__(self, x):
        self.x = x
        
    def x2(self):
        return self.x * 2
    
class B:
    def __init__(self, y):
        self.y = y
        
    def y3(self):
        return self.y * 3
    
class C(A, B):
    pass
    


# In[37]:


C.__bases__


# In[38]:


# When we search for an attribute on an instance of C, 
# we'll be looking at:

# - the instance
# - the class (C)
# - the parents (A, then B)
# - object, the top object in Python's hierarchy


# In[39]:


C.__mro__ # Method resolution order


# In[45]:


class A:
    def __init__(self, x):
        self.x = x
        
    def x2(self):
        return self.x * 2
    
class B:
    def __init__(self, y):
        self.y = y
        
    def y3(self):
        return self.y * 3
    
class C(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)
    
c = C(10,20)
vars(c)


# In[46]:


c.x2() 


# In[47]:


c.y3() 


# In[48]:


C.__mro__


# In[49]:


class C(B, object, A):
    pass


# In[ ]:




