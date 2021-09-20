#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('run', 'utils.ipynb')
get_ipython().run_line_magic('cd', 'modal/')


# In[3]:


class model(multityped):
    def __init__(self, worlds, relations, valuation):
        multityped.__init__(self)
        self.types["model"] = []
        self.worlds = worlds
        self.relations = relations
        self.valuation = valuation
    
    def addWorld(world):
        self.worlds.add(world)


# In[ ]:




