#!/usr/bin/env python
# coding: utf-8

# # Operators

# In[1]:


get_ipython().run_line_magic('run', 'propositions.ipynb')


# In[2]:


def negate(truth_value):
    if truth_value == None:
        return None
    return not truth_value

class negation(proposition):
    def __init__(self, prop, truth_value):
        proposition.__init__(self, truth_value)
        self.types["negation"] = ["proposition"]
        self.proposition = prop

    def calculate(self):
        return negate(self.proposition.isTrue())


# ## Conditional

# In[3]:


class implication(proposition):
    def __init__(self, antecedent, consequent, truth_value=None):
        proposition.__init__(self, truth_value)
        self.types["implication"] = ["proposition"]
        self.antecedent = antecedent
        self.consequent = consequent

    def calculate(self):
        antecedent = self.antecedent
        consequent = self.consequent
        if antecedent.truth_value == False:
            return True
        if consequent.truth_value == True:
            return True
        if antecedent.truth_value == True and consequent.truth_value == False:
            return False
        return self.truth_value

    def getText(self):
        return "if " + self.antecedent.getText() + " then " + self.consequent.getText()


# ## Conjunction

# In[4]:


class conjunction(proposition):
    def __init__(self, propositions, truth_value=None):
        proposition.__init__(self, truth_value)
        self.types["conjunction"] = ["proposition"]
        self.propositions = propositions

    def calculate(self):
        temp = True
        for prop in self.propositions:
            if prop.isTrue() == False:
                temp = False
                break
            if prop.isTrue() != True:
                temp = prop.isTrue()
        return temp

    def getText(self):
        text = self.propositions[0].getText()
        for prop in self.propositions[1:]:
            text += " and " + prop.getText()


# ## Disjunction

# In[5]:


class disjunction(proposition):
    def __init__(self, propositions, truth_value=None):
        proposition.__init__(self, truth_value)
        self.types["disjunction"] = ["proposition"]
        self.propositions = propositions

    def calculate(self):
        temp = False
        for prop in self.propositions:
            if prop.isTrue() == True:
                temp = True
                break
            if prop.isTrue() != False:
                temp = prop.isTrue()
        return temp

    def getText(self):
        text = self.propositions[0].getText()
        for prop in self.propositions[1:]:
            text += " or " + prop.getText()


# ## Biconditional

# In[6]:


class biconditional(proposition):
    def __init__(self, propositions, truth_value=None):
        proposition.__init__(self, truth_value)
        self.types["biconditional"] = ["proposition"]
        self.propositions = propositions

    def calculate(self):
        first = self.propositions[0]
        temp = first.isTrue()
        if temp is None:
            return None
        for prop in self.propositions[1:]:
            if prop.isTrue() != temp:
                return None
        return True

    #def getText(self):
    #    return self.antecedent.getText() + " if and only if " + self.consequent.getText()

