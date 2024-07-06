#!/usr/bin/env python
# coding: utf-8

# #                                      Machine Learning                        
#     
#     
# # Question No.2 
#     
# 
# # ( B) What's the use of pandas, numpy, seaborn, matplotlib, OS library in python

#                                            # Answer :
#   
#     
# # 1. Pandas :
#     
# Use Case : Pandas is used for data manipulation and analysis. It provides data structures like DataFrame and Series,
# 
# which are highly efficient for handling structured data.
#     
# # 2. NumPy :
#     
# Use Case : NumPy is used for numerical computations in Python. It provides support for large, multi-dimensional arrays
# 
# and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
# 
# 
# # 3. Matplotlib
# 
# Use_Case: Matplotlib is a plotting library used for creating static, animated, and interactive visualizations in Python.
# 
# It provides a MATLAB-like interface and supports a wide variety of plots and customization options.
# 
# # 4. Seaborn
# 
# Use_Case : Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and
#     
# informative statistical graphics. It simplifies the process of creating complex visualizations like heatmaps, violin plots,
# 
# and pair plots.
# 
# 
# 
# # 5. OS Library :
#     
# Use_Case : The OS library provides a way of using operating system-dependent functionality in Python programs. 
# 
# It allows you to interact with the operating system, manipulate file paths, and perform various system-related tasks.
# 

# # Conclusion :
# 
# Pandas : It is used for data manipulation and analysis.
# 
# NumPy : It is used for numerical computations and working with arrays.
# 
# Matplotlib : It is used for creating static, animated, and interactive visualizations.
# 
# Seaborn : It is used for creating statistical graphics with attractive and informative designs.
# 
# OS library : It is used for interacting with the operating system, manipulating files, and managing directories.
# 
# 
# These libraries are essential tools for various tasks ranging from data analysis to visualization and system-level 
# 
# operations in Python programming.

# In[ ]:





# In[ ]:


#( A ) Take any dataset from kaggle and handling missing values.


# After removing missing values, from the same dataset - draw bar chart, pie chart, line chart, histogram 


# # " House Prices - Advanced Regression Techniques " 

#           # Instead of Google Colab.I have done this in "Jupyter Notebook", Because i am familar with this

# In[12]:


import pandas as pd


# In[16]:


df = pd.read_csv('train.csv')

print(df.head())


# In[ ]:


# Step 2:                    

# Check for missing values

# Drop rows with missing values (you could also fill them, depending on the situation

# Verify that there are no missing values left


# In[17]:


print(df.isnull().sum())

df_cleaned = df.dropna()


print(df_cleaned.isnull().sum())


# In[ ]:


# Step 3:  

                               #Create Visualizations
    
# Create a bar chart, pie chart, line chart, and histogram using the cleaned dataset.

# Bar Chart: Count of Houses by Overall Quality


# In[20]:


pip install matplotlib seaborn


# In[22]:


print(df_cleaned['OverallQual'].isnull().sum())


# In[23]:


print(df_cleaned['OverallQual'].dtype)


# In[24]:


print(df_cleaned.columns)


# In[27]:


pip install matplotlib seaborn


# In[29]:


pip install --upgrade matplotlib seaborn


# # 1.Create a histogram using the cleaned dataset.

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('train.csv')

# Drop rows with missing values
df_cleaned = df.dropna()

# Set up the figure size
plt.figure(figsize=(10, 6))

# Histogram: Distribution of house sale prices
plt.hist(df_cleaned['SalePrice'], bins=20, edgecolor='k')
plt.title('Distribution of House Sale Prices')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# # 2. Create a bar chart 

# In[34]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('train.csv')

# Drop rows with missing values
df_cleaned = df.dropna()

# Calculate percentage of houses in each category (for example, top 5 categories)
top_categories = df_cleaned['SalePrice'].value_counts().head(5)

# Set up the figure size
plt.figure(figsize=(8, 8))

# Pie chart: Distribution of top house sale prices
plt.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Top House Sale Prices')
plt.show()


# # 3.Create Create a Line chart

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('train.csv')

# Drop rows with missing values
df_cleaned = df.dropna()

# Sort values by 'YearBuilt' to see trend over time
df_cleaned.sort_values(by='YearBuilt', inplace=True)

# Set up the figure size
plt.figure(figsize=(10, 6))

# Line chart: Trend of house sale prices over time (by YearBuilt)
plt.plot(df_cleaned['YearBuilt'], df_cleaned['SalePrice'], marker='o', linestyle='-')
plt.title('Trend of House Sale Prices over Time')
plt.xlabel('Year Built')
plt.ylabel('Sale Price')
plt.grid(True)
plt.show()


# In[ ]:




