#!/usr/bin/env python
# coding: utf-8

# # Propositions

# In[1]:


get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('run', 'utils.ipynb')
get_ipython().run_line_magic('cd', 'logic/')


# In[2]:


class proposition(multityped):
    def __init__(self, truth_value):
        multityped.__init__(self)
        self.types["proposition"] = []
        self.truth_value = truth_value

    def isTrue(self):
        if self.truth_value == None:
            return self.calculate()
        return self.truth_value

class atomic_proposition(proposition):
    def __init__(self, text, truth_value):
        proposition.__init__(self, truth_value)
        self.text = text

    def getText(self):
        return self.text
    
    def calculate(self):
        return None


# ## Truth
# 
# Atomic proposition that is simply true.

# In[3]:


truth = atomic_proposition("True", True)


# ## Falsity
# 
# Atomic proposition that is simply false.

# In[4]:


falsity = atomic_proposition("False", False)

