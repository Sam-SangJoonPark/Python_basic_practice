#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd

train = pd.read_csv("C:/Users/ASIA_07/Downloads/titanic.csv")


# In[83]:


train


# #Data Dictionary
# Survived: 0 = No, 1 = Yes 0.생존하지 못함 1.생존
# pclass: Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd 승객등급
# Name,Sex, Age
# sibsp: # of siblings / spouses aboard the Titanic 함께 탑승한 형제, 배우자의 수
# parch: # of parents / children aboard the Titanic 함게 탑승한 자녀, 부모의 수
# ticket: Ticket number 티켓 id
# Fare : 티켓 아이디
# cabin: Cabin number 객실 번호
# embarked: Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton 탑승한곳

# In[84]:


train.isnull().sum()


# In[85]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()


# In[86]:


plt.rcParams["figure.figsize"] = (4,3)


# In[87]:


# survived는 Survived 열에서 살아남은 사람을 Sex 로 분류.
# dead는 Survived 열에서 살아남지 못한 사람을 Sex로 분류
# df화 한것.

survived = train[train["Survived"]==1]["Sex"].value_counts()
dead = train[train["Survived"]== 0]["Sex"].value_counts()
df = pd.DataFrame([survived, dead], index= ["survived","dead"])
df.plot(kind='bar', stacked = True, figsize=(4,3))


# In[88]:


# 함수로 정의
def bar_chart(feature) :
    survived = train[train["Survived"]==1][feature].value_counts()
    dead = train[train["Survived"]== 0][feature].value_counts()
    df = pd.DataFrame([survived, dead], index= ["survived","dead"])
    df.plot(kind='bar', stacked = True, figsize=(6,7))


# In[89]:


bar_chart("Sex")


# In[90]:


bar_chart('Pclass')


# In[91]:


bar_chart("SibSp")


# In[92]:


bar_chart("Parch")


# In[93]:


bar_chart("Embarked")


# In[94]:


train.groupby("Pclass").agg({'Age' : 'max', 'SibSp' : 'sum', 'Fare' : 'mean'})


# #이름과 생존율 상관성?

# In[95]:


#.Mr, .Mrs 등 호칭 뽑아내기   step 1.

train['Title'] = train['Name'].str.extract(' ([A-Za-z]+)\.', expand = False)


train     # Title 열이 생김. 확인

train['Title'].value_counts()   # Mr가 몇개고 Miss가 몇개인지 등 생성


# In[96]:


# step 2. Mr, Miss 부분을 숫자로 바꿔서 분석에 편리하게 해주기

train["Title1"] = 9     # 일단 Title1 열을 만들어주자 

for row in range(len(train)) :                     #for문으로 문자를 숫자로 바꿈
    if train.iloc[row, 12] == "Mr" :
        train.iloc[row, 13] = 0
    elif train.iloc[row, 12] == "Miss" :
        train.iloc[row, 13] = 1
    elif train.iloc[row, 12] == "Mrs" :
        train.iloc[row, 13] = 2   
    else :
        train.iloc[row, 13] = 3





# In[97]:


# 다른 방법 step1,2 같이 : map 활용하기   

title_mapping = {"Mr" : 0, "Miss" : 1, "Mrs" : 2, "Master" : 3, 
                 "Dr" :3, "Rev" : 3, "Col":3, "Major" :3, "Mlle" :3,
                 "Countess" :3, "Ms" :3, "Lady" :3,
                 "Jonkheer" :3, "Don" :3, "Mme" :3, "Capt" :3, "Sir" :3 }

train['Title2'] = train['Title'].map(title_mapping)


# In[100]:


bar_chart('Title1')   # Title1변수로 ...


# In[101]:


#불필요한 열 제거하기     = del train['열이름']

train.drop('Name', axis =1, inplace= True)


# In[105]:


# 여기까지 저장
train_01 = train.copy()


# In[106]:


train = train_01.copy()


# In[108]:


train


# In[109]:


#성별도 작업하자
mapp = {"male" : 0, "female" : 1}

train["Sex1"] = train["Sex"].map(mapp)     #Sex1이라는 열을 만든다리


# In[118]:


bar_chart("Sex1") ; bar_chart("Sex")    # 같은거


# In[119]:


# fill missing age with median age for each title (Mr, Mrs 등등)


train["Age"].fillna(train.groupby("Title")["Age"].transform("median"),inplace =True)


# In[121]:


train.isnull().sum()   # 다 채워짐


# In[123]:


# 씨본으로 그리자
#잘 모르겠지만 어쨌든 Seaborn으로 나이대별로 사망, 생존자 그림

facet = sns.FacetGrid(train, hue = "Survived", aspect = 4 )
facet.map(sns.kdeplot, 'Age', shade = True)
facet.set(xlim=(0, train['Age'].max()))
facet.add_legend()
plt.xlim(0,20)
# plt.xlim(0,20)  부분은 맨 나이대임.


# In[141]:


# 그래서 아예 함수로 만들었음.  -나이대별로 차이, 구간별 차이 다 볼 수 있음.
# feature에 따옴표 빼야함.

def chart_kdeplot(feature, x_min, x_max) :
    facet = sns.FacetGrid(train, hue = "Survived", aspect = 4 )
    facet.map(sns.kdeplot, feature, shade = True)
    facet.set(xlim=(0, train[feature].max()))
    facet.add_legend()
    plt.xlim(x_min, x_max)


# In[142]:


chart_kdeplot("Age",20,30)


# In[144]:


# loc를 이용하여 
# Numerical Age 를 Categorical variable로 바꾸자!
# 또 Age1 은 새로운 열을 생성하는 거다.

train.loc[train['Age'] <= 16, 'Age1'] = 0,
train.loc[(train['Age'] > 16) & (train['Age'] <= 26), 'Age1'] = 1,
train.loc[(train['Age'] > 26) & (train['Age'] <= 36), 'Age1'] = 2,
train.loc[(train['Age'] > 36) & (train['Age'] <= 62), 'Age1'] = 3,
train.loc[train['Age'] > 62, 'Age1'] = 4


# In[147]:


train['Age1'].value_counts()


# In[149]:


# 그럼 age와 사망률

bar_chart("Age1")


# In[150]:


train_02 = train.copy()
train = train_02


# # embark : 탑승한곳.
# # 이제 embark 를 0, 1, 2 로 묶어서 앞에와 같이 해보기

# In[151]:


train["Embarked"].value_counts()


# In[158]:


# 아까 survive, dead랑 비슷
# Pclass 1등석을 embarked로 분류 ,,, 등.. 해서 df화.

Pclass1 = train[train["Pclass"] ==1]['Embarked'].value_counts()
Pclass2 = train[train["Pclass"]==2]['Embarked'].value_counts()
Pclass3 = train[train["Pclass"]==3]['Embarked'].value_counts()

df = pd.DataFrame([Pclass1, Pclass2, Pclass3], index = ['1st class','2nd class','3rd class'])
df.plot(kind = 'bar', stacked = True, figsize = (4,3))


# In[159]:


train.isnull().sum()     #embarked 결측치가 있음


# In[160]:


train["Embarked1"] = train["Embarked"].fillna("S")


# In[161]:


train.isnull().sum()     #Embarked 1 열이 결측치 없음. EMbarked 아님 주의.


# In[167]:


#Embarked2를 S C Q 를 0 1 2 로 바꿈
embarked_mapping = {"S" : 0, "C" : 1, "Q" : 2}
train["Embarked2"] = train['Embarked1'].map(embarked_mapping)


# In[168]:


train.head()


# In[170]:


print(train["Embarked1"].value_counts()) ; train["Embarked2"].value_counts()

# 두 개가 같음을 확인. Embark1은 SCQ, Embark2는 012


# In[171]:


train.isnull().sum()


# # 이제 실습. Fare 컬럼
#   <= 17 이면 0 
#   >17 and <= 30 이면 1
#  >30 and <= 100 이면 2
#  >100 이면 3   
#   
# 해서 Fare 1 이라는 새로운 컬럼 만들기 .
# 

# In[172]:


train_03 = train.copy()
train= train_03


# In[174]:


train.loc[train["Fare"] <= 17, "Fare1"] = 0
train.loc[(train["Fare"] > 17) & (train["Fare"] <= 30), "Fare1"] = 1
train.loc[(train["Fare"] >30) & (train["Fare"]<= 100), "Fare1"] = 2
train.loc[train["Fare"] > 100 , "Fare1"] = 3


# In[ ]:





# In[181]:


# 이제 cabin . Cabin1열을 생성.

train["Cabin1"] = train["Cabin"].str[:1]
train["Cabin1"].value_counts()


# In[183]:


#Pclass와 Embarked와 똑같은것임.

Pclass1 = train[train['Pclass']==1]['Cabin1'].value_counts()
Pclass2 = train[train['Pclass'] ==2]['Cabin1'].value_counts()
Pclass3 = train[train['Pclass'] ==3]['Cabin1'].value_counts()

df = pd.DataFrame([Pclass1,Pclass2,Pclass3])
df.index = ['1st class', '2nd class', '3rd class']
df.plot(kind = 'bar', stacked = True, figsize = (4,3))



# In[184]:


#mapping 방식으로 한것.
# Cabin2를 만들어서 Cabin1에서의 알파벳을 숫자로 바꿈.



df.plot(kind = 'bar', stacked = True, figsize = (4,3))
cabin_mapping = {"A":0, "B" :0.4, "C":0.8, "D" : 1.2, "E" : 1.6, "F" : 2 , 
                "G" : 2.4, "T" : 2.8}

train["Cabin2"]  = train["Cabin1"].map(cabin_mapping)

# 결측치는 median 으로 채움.-- Cabin2만 해당.
train["Cabin2"].fillna(train.groupby("Pclass")["Cabin2"].transform("median"), inplace = True)


# In[194]:


#train.isnull().sum()


# In[196]:


train.columns


# In[197]:


# 가족 수를 합치자
train["FamilySize"] = train["SibSp"] + train["Parch"] + 1    #가족의 수


family_mapping = {1:0, 2:0.4, 3:0.8, 4:1.2, 5:1.6, 6:2, 7:2.4, 8:2.8, 9: 3.2, 10 :3.6
                 ,11:4}

train["FamilySize1"] = train['FamilySize'].map(family_mapping)

# Famliysize를 약간 정교하게 수치화 한 듯 하다.


# In[200]:


#마지막. train _ne w 만들기 : 필요없는 것 빼고 다듬는과정

sel_column = ["Survived","Pclass", "Title2", "Sex1", "Age1", "Embarked2", 
             "Fare1", "Cabin2", "FamilySize1"]

train_new = train[sel_column]








# In[202]:


train_04 = train.copy()
train = train_04


# In[204]:


train_new


# In[205]:


# train_new의 컬럼들 이름 바꾸어주자!
train_new.columns = ["Survived","Pclass", "Title", "Sex", "Age", "Embarked", 
             "Fare", "Cabin", "FamilySize"]


# In[207]:


train_new.head


# In[208]:


# 이제 마지막. 엑셀로 저장하기

train_new.to_excel("C:/Users/ASIA_07/sjpark/train_new.xlsx")



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




