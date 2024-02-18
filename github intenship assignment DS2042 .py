#!/usr/bin/env python
# coding: utf-8

# In[16]:


def func(a,b):
    return b if a == 0 else func(b % a, a)


# In[6]:


return b if a == 0 else func(b % a, a)


# In[7]:


print(func(30, 7))


# In[9]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)


# In[10]:


sorted_numbers = sorted(numbers)


# In[11]:


even = lambda a: a % 2 == 0


# In[12]:


even_numbers = filter(even, sorted_numbers)


# In[13]:


print(type(even_numbers))


# In[ ]:


question 4


# In[17]:


set1 = {14, 3, 55}


# In[18]:


set2 = {82, 49, 62}


# In[20]:


set3 = {99, 22, 17}


# In[23]:


print(len(set1 + set2 + set3))


# In[ ]:


QUESTION 5


# In[25]:


get_ipython().run_line_magic('pinfo', 'exceptions')


# In[ ]:


Answer... Raise is used to raise exceptions


# In[ ]:


Question 6 Which of the following modules need to be imported to handle date time computations in
get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Answer ..datetime


# In[26]:


get_ipython().run_line_magic('pinfo', 'snippet')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'snippet')


# In[27]:


print(4**3 + (7 + 5)**(1 + 1))


# In[ ]:


get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


answer .. strptime


# In[ ]:


Question 9}The python tuple is _____ in nature


# In[ ]:


Answer  immutable


# In[ ]:


Question 10  The ___ is a built-in function that returns a range object that consists series of integer numbers, which
we can iterate using a for loop.


# In[ ]:


Answer =  Range


# In[ ]:


get_ipython().run_line_magic('pinfo', 'name')


# In[ ]:


Lambda function


# In[ ]:


question 12}The module Pickle is used to ___


# In[ ]:


Answer= Both A and B


# In[ ]:


Question 13 Amongst which of the following is / are the method of convert Python objects for writing data in
get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


Answer..dump


# In[ ]:


get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


Answer...The load


# In[ ]:


Question 15} A text file contains only textual information consisting of ___.


# In[ ]:


Answer...Alphabert, Number and special symbols


# In[ ]:


Question 16} Which Python code could replace the ellipsis (...) below to get the following output? (Select all that
apply.)


# In[ ]:


Answer...a) for ship, captain in captains.items():
print(ship, captain)
b) for ship in captains:
print(ship, captains[ship])


# In[ ]:


get_ipython().run_line_magic('pinfo', 'captains')


# In[ ]:


Answer .. captains = {}


# In[ ]:


Question 18} Now you have your empty dictionary named captains. It’s time to add some data!
Specifically, you want to add the key-value pairs "Enterprise": "Picard", "Voyager": "Janeway",
and "Defiant": "Sisko".
Which of the following code snippets will successfully add these key-value pairs to the
get_ipython().run_line_magic('pinfo', 'dictionary')



# In[ ]:


Answer: - c)
captains = { "Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko",


# In[ ]:


Question 19 } You’re really building out the Federation Starfleet now! Here’s what you have:
captains = {
"Enterprise": "Picard",
"Voyager": "Janeway",
"Defiant": "Sisko",
"Discovery": "unknown",
}Now, say you want to display the ship and captain names contained in the dictionary, but you also
get_ipython().run_line_magic('pinfo', 'it')


# In[ ]:


Answer ... b)for ship, captain in captains.items(): print(f"The {ship} is captained by {captain}.")


# In[ ]:


Question 20} You’ve created a dictionary, added data, checked for the existence of keys, and iterated over it with a for loop. Now you’re ready to delete a key from this dictionary:  captains = {      "Enterprise": "Picard",      "Voyager": "Janeway",      "Defiant": "Sisko" 


# In[ ]:


Answer...captains["Discovery"] this will remove entry for key “discover”  from captains dictionary 

