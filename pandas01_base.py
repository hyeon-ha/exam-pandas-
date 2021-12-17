#!/usr/bin/env python
# coding: utf-8

# # Pandas

# ## Series

# In[13]:


import pandas as pd


# In[2]:


pd.set_option('display.unicode.east_asian_width', True)


# In[17]:


dict_data = {'a':[1, 2], 'b':2, 'c':3}
sr = pd.Series(dict_data)
print(sr)
print(type(sr))
print(sr['a'])
print(sr[1])


# In[5]:


list_data = ['2022-10-14', 3.14, "ABC", 100, True]
sr = pd.Series(list_data)
print(sr)
print(sr[3])


# In[6]:


print(sr.index)
print(sr.values)


# In[7]:


tup_data = ('2021-10-14', '하늘', 200, False)
sr = pd.Series(tup_data, index=['가입일', '이름', '잔액', '할인쿠폰 발행'])
print(sr)


# In[8]:


print(sr.index)
print(sr.values)


# In[9]:


print(sr['이름'])
print(sr[2])
print(sr[1:3])
print(sr['이름':'할인쿠폰 발행'])


# ## DataFrame

# In[25]:


dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
              'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)


# In[43]:


df = pd.DataFrame([[15, '남', '영훙중'],
                    [17, '여', '성암중']],
                 index=['서준', '도연'],
                 columns=['나이', '성별', '학교'])
print(df)
print(df.index)
print(df.columns)


# In[44]:


df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)


# In[45]:


df3 =df.rename(columns= {'연령':'나이'},inplace=True)
print(df)
print(df3)


# In[46]:


df2 = df.rename(columns= {'나이':'연령'}, inplace=False)
print(df)
print(df2)


# In[49]:


df.rename(index={'학생2':'도연', '학생1':'서준'},
          inplace=True)
print(df)


# In[50]:


print(df['나이'])


# In[52]:


print(df.loc['서준'])


# In[53]:


print(df.loc['서준', '나이'])


# In[59]:


df3 = df['나이']['서준']
print(type(df3))
print(df3)


# In[61]:


df.loc['서준', '나이'] = 22
print(df)


# In[63]:


df.loc[2] = 0
print(df)


# In[64]:


df.loc['진석'] = [18, '남', '신일중']
print(df)


# In[65]:


df.loc['선희'] = [14, '여', '풍문중']
print(df)


# In[66]:


df.drop([2],inplace=True,axis=0)
print(df)


# In[71]:


df['학년'] = 3
print(df)


# In[69]:


df['height'] = [175, 156, 170, 185]
print(df)


# In[72]:


df.drop(['학년'],inplace=True, axis='columns')
print(df)


# In[74]:


label1 = df.loc[['서준','진석']]
print(label1)


# In[75]:


label2 = df.iloc[[1,3]]
print(label2)


# In[76]:


label3 = df.loc['서준':'진석']
print(label3)


# In[77]:


label4 = df.iloc[0:2]
print(label4)


# In[78]:


age = df['나이']
print(type(age))
print(age)


# In[79]:


age2 = df[['나이', '소속']]
print(type(age2))
print(age2)


# In[80]:


age3 = df[['나이']]
print(type(age3))
print(age3)


# In[81]:


height = df.height
print(type(height))
print(height)


# In[82]:


age4 = df.나이
print(age4)


# In[86]:


df3 = df.loc[df['height'] < 175]
print(df3)


# In[87]:


df4 = df.loc[df['height'] < 175, ['height']]
print(df4)


# In[88]:


df.loc[df['height'] < 175, ['height']] += 10
print(df)


# In[90]:


df.loc[df['소속'] == '성암중', ['height']] += 100
print(df)


# In[92]:


print(df.loc[(df['height'] < 185) & (df['나이'] < 20)])


# In[93]:


df.loc['도연','height'] += 100
print(df)


# In[102]:


df.loc[df['height'] == df['height'].max()]


# In[98]:


print(df.info())


# In[101]:


print(df.describe())


# In[106]:


print(df.height.max())

