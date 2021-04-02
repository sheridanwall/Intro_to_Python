#!/usr/bin/env python
# coding: utf-8

# # Machine learning on wine
# 
# **Topics:** Text analysis, linear regression, logistic regression, text analysis, classification
# 
# **Datasets**
# 
# - **wine-reviews.csv** Wine reviews scraped from https://www.winemag.com/
# - **Data dictionary:** just go [here](https://www.winemag.com/buying-guide/tenuta-dellornellaia-2007-masseto-merlot-toscana/) and look at the page
# 
# ## The background
# 
# You work in the **worst newsroom in the world**, and you've had a hard few weeks at work - a couple stories killed, a few scoops stolen out from under you. It's not going well.
# 
# And because things just can't get any worse: your boss shows up, carrying a huge binder. She slams it down on your desk.
# 
# "You know some machine learning stuff, right?"
# 
# You say "no," but she isn't listening. She's giving you an assignment, the _worst assignment_...
# 
# > Machine learning is the new maps. Let's get some hits!
# >
# > **Do some machine learning on this stuff.**
# 
# "This stuff" is wine reviews.
# 
# ## A tiny, meagre bit of help
# 
# You have a dataset. It has some stuff in it:
# 
# * **Numbers:**
#     - Year published
#     - Alcohol percentage
#     - Price
#     - Score
#     - Bottle size
# * **Categories:**
#     - Red vs white
#     - Different countries
#     - Importer
#     - Designation
#     - Taster
#     - Variety
#     - Winery
# * **Free text:**
#     - Wine description

# # Cleaning up your data
# 
# Many of these pieces - the alcohol, the year produced, the bottle size, the country the wine is from - aren't in a format you can use. Convert the ones to numbers that are numbers, and extract the others from the appropriate strings.

# In[1]:


import pandas as pd


# In[2]:





# In[3]:





# In[37]:


#df['alcohol'] = df.alcohol.astype(float)
#df.dtypes


# In[38]:


# Turning date published into a datetime
#df['date published'] = pd.to_datetime(df['date published'], format='%m/%d/%Y')
#df.head()


# In[39]:


# Bottle size into float
#df['bottle size'] = df['bottle size'].str.replace('ml','',regex=False)
#df['bottle size'] = df['bottle size'].str.replace('ML','',regex=False)
#df['bottle size'] = df['bottle size'].str.replace('L','',regex=False)
#df.head()


# In[40]:


#df['bottle size'] = df['bottle size'].astype(float)
#df.dtypes


# In[41]:


# Extracting Country
#df['country'] = df['appellation'].str.extract(r'(\b(\w+)\b$)')
#df.head()


# In[ ]:


df.price.value_counts()


# In[ ]:





# In[42]:


#Converting price to a float
#df['price_clean'] = df.price.str.extract(r'(\b(\d{0,5})\b)')
#df.head()


# In[43]:


#df.price_clean.isnull().value_counts()


# In[44]:


#df.price.isnull().value_counts()


# # Reimport CSV

# In[45]:


df = pd.read_csv('wine-reviews.csv')
df.head()


# # Alcohol

# In[46]:


df['alcohol_clean'] = df.alcohol.str.replace('%','',regex=False)
df.head()


# In[47]:


df['alcohol_clean'] = df.alcohol_clean.astype(float)


# In[48]:


df.dtypes


# # Date to datetime

# In[50]:


df['date_clean'] = pd.to_datetime(df['date published'],format='%m/%d/%Y')
df.head()


# # Bottle Size

# In[54]:


df['bottle_size_clean'] = df['bottle size'].str.extract(r'([\d\W]*)[ml L ML l]')
df.head(50)


# In[55]:


df.bottle_size_clean.value_counts()


# In[56]:


df['bottle_size_clean'] = df.bottle_size_clean.astype(float)


# In[57]:


df.bottle_size_clean[df.bottle_size_clean < 100] = df.bottle_size_clean[df.bottle_size_clean < 100]*1000


# In[61]:


df.bottle_size_clean.value_counts()


# # Price

# In[51]:


df['price_clean'] = df.price.str.extract(r'\$(\d*)')
df.head()


# In[77]:


df['price_clean'] = df.price_clean.astype(float)


# # Extracting Country

# In[92]:


df['country'] = df['appellation'].str.extract(r'\b(\w+)\b$')
df.wine_desc.isnull().value_counts()


# In[65]:


df.country.value_counts()


# ## What might be interesting in this dataset?
# 
# Maybe start out playing around _without_ machine learning. Here are some thoughts to get you started:
# 
# * I've heard that since the 90's wine has gone through [Parkerization](https://www.estatewinebrokers.com/blog/the-parkerization-of-wine-in-the-1990s-and-beyond/), an increase in production of high-alcohol, fruity red wines thanks to the influence of wine critic Robert Parker.
# * Red and white wines taste different, obviously, but people always use [goofy words to describe them](https://winefolly.com/tutorial/40-wine-descriptions/)
# * Once upon a time in 1976 [California wines proved themselves against France](https://en.wikipedia.org/wiki/Judgment_of_Paris_(wine)) and France got very angry about it

# In[69]:


df.groupby('country').wine_points.max().sort_values(ascending=False)


# In[70]:


df.groupby('country').wine_points.mean().sort_values(ascending=False)


# In[71]:


df.groupby('country').wine_points.min().sort_values(ascending=False)


# In[80]:


df.groupby('category').price_clean.mean().sort_values(ascending=False)


# In[81]:


df.groupby('country').price_clean.max().sort_values(ascending=False)


# In[82]:


df.groupby('country').price_clean.min().sort_values(ascending=False)


# In[85]:


df.groupby('country').price_clean.mean().sort_values(ascending=False)


# ## But machine learning?
# 
# Well, you can usually break machine learning down into a few different things. These aren't necessarily perfect ways of categorizing things, but eh, close enough.
# 
# * **Predicting a number**
#     - Linear regression
#     - For example, how does a change in unemployment translate into a change in life expectancy?
# * **Predicting a category** (aka classification)
#     - Lots of algos options: logistic regression, random forest, etc
#     - For example, predicting cuisines based on ingredients
# * **Seeing what influences a numeric outcome**
#     - Linear regression since the output is a number
#     - For example, minority and poverty status on test scores 
# * **Seeing what influences a categorical outcome**
#     - Logistic regression since the output is a category
#     - Race and car speed for if you get a waring vs ticket
#     - Wet/dry pavement and car weight if you survive or not in a car crash)
# 
# We have numbers, we have categories, we have all sorts of stuff. **What are some ways we can mash them together and use machine learning?**
# 
# ### Brainstorm some ideas
# 
# Use the categories above to try to come up with some ideas. Be sure to scroll up where I break down categories vs numbers vs text!
# 
# **I'll give you one idea for free:** if you don't have any ideas, start off by creating a classifier that determines whether a wine is white or red based on the wine's description.

# In[98]:


import numpy as np


# In[99]:


df.dtypes


# In[ ]:





# In[103]:


from sklearn.feature_extraction.text import CountVectorizer

# Make a vectorizer
vectorizer = CountVectorizer()

# Learn and count the words in df.content
matrix = vectorizer.fit_transform(df.wine_desc.values.astype('str'))

# Convert the matrix of counts to a dataframe
words_df = pd.DataFrame(matrix.toarray(),
                        columns=vectorizer.get_feature_names())


# In[104]:


words_df.head()


# In[105]:


df['is_red'] = (df['category'] == 'Red').astype(int)
df.head()


# In[106]:


df['is_white'] = (df['category'] == 'White').astype(int)
df.head()


# In[107]:


X = words_df
y = df.is_red


# In[108]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)


# In[109]:


from sklearn.tree import DecisionTreeClassifier 
clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)


# In[111]:


from sklearn.metrics import confusion_matrix

y_true = y_test
y_pred = clf.predict(X_test)
matrix = confusion_matrix(y_true, y_pred)

label_names = pd.Series(['not red', 'red'])
pd.DataFrame(matrix,
     columns='Predicted ' + label_names,
     index='Is ' + label_names)


# In[113]:


import eli5

eli5.show_weights(clf, feature_names=vectorizer.get_feature_names())


# In[ ]:


# 2. Predicting price based on alcohol content - are stronger wines more expensive?


# In[ ]:





# In[ ]:





# In[ ]:





# You can also go to https://library.columbia.edu and see if you can find some academic papers about wine. I'm sure they'll inspire you! (and they might even have some ML ideas in them you can steal, too)

# # Implement 2 of your machine learning ideas

# In[114]:


import statsmodels.formula.api as smf

model = smf.ols('price_clean ~ alcohol_clean', data=df)
results = model.fit()

results.summary()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




