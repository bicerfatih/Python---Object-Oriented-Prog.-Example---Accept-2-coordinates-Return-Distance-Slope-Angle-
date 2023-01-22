#!/usr/bin/env python
# coding: utf-8

# In[42]:


import math


# In[ ]:


'''
Accept 2 coordinates as a pair of duples,

Return: 
Distance 
Slope 
Angle 

between these 2 coordinates. 

Coordinate_1 = (x1,y1)
Coordinate_2 = (x2,y2)

'''


# In[44]:


class Coordinates ():
    def __init__ (self, coordinate_1, coordinate_2):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2
    def Distance(self):
        (x1,y1) = self.coordinate_1
        (x2,y2) = self.coordinate_2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def Slope(self):
        (x1,y1) = self.coordinate_1
        (x2,y2) = self.coordinate_2
        return (y2-y1)/(x2-x1)
    def Angle(self):
        (x1,y1) = self.coordinate_1
        (x2,y2) = self.coordinate_2
        return math.degrees(math.atan(y2-y1)/(x2-x1))
        


# In[45]:


c1 = (4,8)
c2 = (1,3)


# In[46]:


my_distance = Coordinates(c1,c2)


# In[47]:


my_distance.Distance()


# In[48]:


my_Slope = Coordinates(c1,c2)


# In[49]:


my_Slope.Slope()


# In[50]:


my_Angle = Coordinates(c1,c2)


# In[51]:


my_Angle.Angle()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




