#!/usr/bin/env python
# coding: utf-8

# # Rules of Inference

# Explaining the rules of inference

# In[1]:


get_ipython().run_line_magic('run', 'operators.ipynb')


# In[2]:


class rule_of_inference:
    def __init__(self, validity):
        self.validity = validity


# ## Rules for Negations

# ### Double Negation Elimination

# In[3]:


def double_negation_elimination(negation):
    if 'negation' in negation.types and 'negation' in negation.proposition.types:
        if negation.isTrue():
            negation.proposition.proposition.truth_value = True


# ### Double Negation Introduction

# In[4]:


def double_negation_introduction(negation):
    if 'negation' in negation.types and 'negation' in negation.proposition.types:
        if negation.proposition.proposition.isTrue():
            negation.truth_value = True


# ### Reductio ad Absurdum
# 
# A reduction ad absurdum occurs when we can suppose something and then derive a statement and its negation.

# In[5]:


def reductio_ad_absurdum(negation, supposition):
    if 'negation' in negation.types and 'proposition' in supposition.types:
        if negation.isTrue() and negation.proposition.isTrue():
            supposition.truth_value = False


# ## Rules for Implications

# ## Modus Ponens

# In[6]:


def modus_ponens(implication, proposition):
    if 'implication' in implication.types and 'proposition' in proposition.types:
        if implication.antecedent == proposition:
            if implication.isTrue() and proposition.isTrue():
                implication.consequent.truth_value = True


# ## Modus Tollens

# In[7]:


def modus_tollens(implication, proposition):
    if 'implication' in implication.types and 'proposition' in proposition.types:
        if implication.consequent == proposition:
            if implication.isTrue() and proposition.isTrue() == False:
                implication.antecedent.truth_value = False


# ## Rules for Conjunctions

# ### Conjunction Introduction

# In[8]:


def adjunction(conjunction):
    if 'conjunction' in conjunction.types:
        for prop in conjunction.propositions:
            if prop.isTrue():
                continue
            else:
                return
        conjunction.truth_value = True


# ### Conjunction Elimination

# In[9]:


def simplification(conjunction):
    if 'conjunction' in conjunction.types:
        if conjunction.isTrue():
            for prop in conjunction.propositions:
                prop.truth_value = True


# ## Rules for Disjunctions

# ### Disjunction Introduction

# In[10]:


def disjunction_introduction(disjunction):
    if 'disjunction' in disjunction.types:
        for prop in disjunction.propositions:
            if prop.isTrue():
                disjunction.truth_value = True
                break


# ### Disjunction Elimination

# In[11]:


def disjunctive_syllogism(disjunction):
    if 'disjunction' in disjunction.types:
        if disjunction.isTrue():
            temp = None
            for prop in disjunction.propositions:
                if prop.isTrue():
                    return
                if prop.isTrue() == None:
                    if temp == None:
                        temp = prop
                    else:
                        return
            if temp != None:
                temp.truth_value = True


# ### Case Analysis

# In[12]:


def disjunction_elimination(disjunction, implications):
    if 'disjunction' in disjunction.types and disjunction.isTrue():
        props = disjunction.propositions
        consequent = props[0].consequent
        for prop in props:
            t = False
            for imp in implications:
                if imp.isTrue() and prop == imp.antecedent:
                    if consequent == imp.consequent:
                        t = True
                        break
                    else:
                        return
            if t is False:
                return
        consequent.truth_value = True


# In[ ]:




