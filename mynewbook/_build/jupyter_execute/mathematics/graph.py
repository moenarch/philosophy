#!/usr/bin/env python
# coding: utf-8

# # Graphs

# In[1]:


get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('run', 'utils.ipynb')
get_ipython().run_line_magic('cd', 'mathematics/')


# In[2]:


class node(multityped):
    def __init__(self, value):
        multityped.__init__(self)
        self.types["node"] = []
        self.value = value
    
    def getValue(self):
        return self.value


# In[3]:


class edge(multityped):
    def __init__(self):
        multityped.__init__(self)
        self.types["edge"] = []

class directed_edge(edge):
    def __init__(self, source, target):
        edge.__init__(self)
        self.types["directed_edge"] = ["edge"]
        self.source = source
        self.target = target

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target

