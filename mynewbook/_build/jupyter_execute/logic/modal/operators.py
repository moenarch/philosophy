#!/usr/bin/env python
# coding: utf-8

# # Operators

# In[1]:


get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('run', 'operators.ipynb')


# ## Necessity

# In[2]:


class necessity(proposition):
    def __init__(self, proposition, truth_value):
        proposition.__init__(self, proposition, truth_value)
        self.types['necessity'] = ['proposition']


# ## Possibility

# In[3]:


class possibility(proposition):
    def __init__(self, proposition, truth_value):
        proposition.__init__(self, proposition, truth_value)
        self.types['possibility'] = ['proposition']

