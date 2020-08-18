```python
import pandas as pd

train = pd.read_csv("C:/Users/ASIA_07/Downloads/titanic.csv")


```


```python
train
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>



#Data Dictionary
Survived: 0 = No, 1 = Yes 0.생존하지 못함 1.생존
pclass: Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd 승객등급
Name,Sex, Age
sibsp: # of siblings / spouses aboard the Titanic 함께 탑승한 형제, 배우자의 수
parch: # of parents / children aboard the Titanic 함게 탑승한 자녀, 부모의 수
ticket: Ticket number 티켓 id
Fare : 티켓 아이디
cabin: Cabin number 객실 번호
embarked: Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton 탑승한곳


```python
train.isnull().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64




```python
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()
```


```python
plt.rcParams["figure.figsize"] = (4,3)
```


```python
# survived는 Survived 열에서 살아남은 사람을 Sex 로 분류.
# dead는 Survived 열에서 살아남지 못한 사람을 Sex로 분류
# df화 한것.

survived = train[train["Survived"]==1]["Sex"].value_counts()
dead = train[train["Survived"]== 0]["Sex"].value_counts()
df = pd.DataFrame([survived, dead], index= ["survived","dead"])
df.plot(kind='bar', stacked = True, figsize=(4,3))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x28efa0d1c10>




![png](output_6_1.png)



```python
# 함수로 정의
def bar_chart(feature) :
    survived = train[train["Survived"]==1][feature].value_counts()
    dead = train[train["Survived"]== 0][feature].value_counts()
    df = pd.DataFrame([survived, dead], index= ["survived","dead"])
    df.plot(kind='bar', stacked = True, figsize=(6,7))

```


```python
bar_chart("Sex")
```


![png](output_8_0.png)



```python
bar_chart('Pclass')
```


![png](output_9_0.png)



```python
bar_chart("SibSp")
```


![png](output_10_0.png)



```python
bar_chart("Parch")
```


![png](output_11_0.png)



```python
bar_chart("Embarked")
```


![png](output_12_0.png)



```python
train.groupby("Pclass").agg({'Age' : 'max', 'SibSp' : 'sum', 'Fare' : 'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Fare</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>80.0</td>
      <td>90</td>
      <td>84.154687</td>
    </tr>
    <tr>
      <th>2</th>
      <td>70.0</td>
      <td>74</td>
      <td>20.662183</td>
    </tr>
    <tr>
      <th>3</th>
      <td>74.0</td>
      <td>302</td>
      <td>13.675550</td>
    </tr>
  </tbody>
</table>
</div>



#이름과 생존율 상관성?


```python
#.Mr, .Mrs 등 호칭 뽑아내기   step 1.

train['Title'] = train['Name'].str.extract(' ([A-Za-z]+)\.', expand = False)


train     # Title 열이 생김. 확인

train['Title'].value_counts()   # Mr가 몇개고 Miss가 몇개인지 등 생성

```




    Mr          517
    Miss        182
    Mrs         125
    Master       40
    Dr            7
    Rev           6
    Col           2
    Major         2
    Mlle          2
    Sir           1
    Jonkheer      1
    Mme           1
    Capt          1
    Don           1
    Lady          1
    Countess      1
    Ms            1
    Name: Title, dtype: int64




```python
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





```


```python
# 다른 방법 step1,2 같이 : map 활용하기   

title_mapping = {"Mr" : 0, "Miss" : 1, "Mrs" : 2, "Master" : 3, 
                 "Dr" :3, "Rev" : 3, "Col":3, "Major" :3, "Mlle" :3,
                 "Countess" :3, "Ms" :3, "Lady" :3,
                 "Jonkheer" :3, "Don" :3, "Mme" :3, "Capt" :3, "Sir" :3 }

train['Title2'] = train['Title'].map(title_mapping)


```


```python
bar_chart('Title1')   # Title1변수로 ...
```


![png](output_18_0.png)



```python
#불필요한 열 제거하기     = del train['열이름']

train.drop('Name', axis =1, inplace= True)

```


```python
# 여기까지 저장
train_01 = train.copy()
```


```python
train = train_01.copy()
```


```python
train
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
      <th>Title1</th>
      <th>Title2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>Mrs</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>Miss</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>Mrs</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
      <td>Rev</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
      <td>Miss</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Miss</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 14 columns</p>
</div>




```python
#성별도 작업하자
mapp = {"male" : 0, "female" : 1}

train["Sex1"] = train["Sex"].map(mapp)     #Sex1이라는 열을 만든다리


```


```python
bar_chart("Sex1") ; bar_chart("Sex")    # 같은거
```


![png](output_24_0.png)



![png](output_24_1.png)



```python
# fill missing age with median age for each title (Mr, Mrs 등등)


train["Age"].fillna(train.groupby("Title")["Age"].transform("median"),inplace =True)
```


```python
train.isnull().sum()   # 다 채워짐
```




    PassengerId      0
    Survived         0
    Pclass           0
    Sex              0
    Age              0
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    Title            0
    Title1           0
    Title2           0
    Sex1             0
    dtype: int64




```python
# 씨본으로 그리자
#잘 모르겠지만 어쨌든 Seaborn으로 나이대별로 사망, 생존자 그림

facet = sns.FacetGrid(train, hue = "Survived", aspect = 4 )
facet.map(sns.kdeplot, 'Age', shade = True)
facet.set(xlim=(0, train['Age'].max()))
facet.add_legend()
plt.xlim(0,20)
# plt.xlim(0,20)  부분은 맨 나이대임.

```




    (0.0, 20.0)




![png](output_27_1.png)



```python
# 그래서 아예 함수로 만들었음.  -나이대별로 차이, 구간별 차이 다 볼 수 있음.
# feature에 따옴표 빼야함.

def chart_kdeplot(feature, x_min, x_max) :
    facet = sns.FacetGrid(train, hue = "Survived", aspect = 4 )
    facet.map(sns.kdeplot, feature, shade = True)
    facet.set(xlim=(0, train[feature].max()))
    facet.add_legend()
    plt.xlim(x_min, x_max)
```


```python
chart_kdeplot("Age",20,30)
```


![png](output_29_0.png)



```python
# loc를 이용하여 
# Numerical Age 를 Categorical variable로 바꾸자!
# 또 Age1 은 새로운 열을 생성하는 거다.

train.loc[train['Age'] <= 16, 'Age1'] = 0,
train.loc[(train['Age'] > 16) & (train['Age'] <= 26), 'Age1'] = 1,
train.loc[(train['Age'] > 26) & (train['Age'] <= 36), 'Age1'] = 2,
train.loc[(train['Age'] > 36) & (train['Age'] <= 62), 'Age1'] = 3,
train.loc[train['Age'] > 62, 'Age1'] = 4
```


```python
train['Age1'].value_counts()
```




    2.0    336
    1.0    255
    3.0    181
    0.0    104
    4.0     15
    Name: Age1, dtype: int64




```python
# 그럼 age와 사망률

bar_chart("Age1")

```


![png](output_32_0.png)



```python
train_02 = train.copy()
train = train_02
```

# embark : 탑승한곳.
# 이제 embark 를 0, 1, 2 로 묶어서 앞에와 같이 해보기


```python
train["Embarked"].value_counts()
```




    S    644
    C    168
    Q     77
    Name: Embarked, dtype: int64




```python
# 아까 survive, dead랑 비슷
# Pclass 1등석을 embarked로 분류 ,,, 등.. 해서 df화.

Pclass1 = train[train["Pclass"] ==1]['Embarked'].value_counts()
Pclass2 = train[train["Pclass"]==2]['Embarked'].value_counts()
Pclass3 = train[train["Pclass"]==3]['Embarked'].value_counts()

df = pd.DataFrame([Pclass1, Pclass2, Pclass3], index = ['1st class','2nd class','3rd class'])
df.plot(kind = 'bar', stacked = True, figsize = (4,3))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x28ef7ac4a00>




![png](output_36_1.png)



```python
train.isnull().sum()     #embarked 결측치가 있음
```




    PassengerId      0
    Survived         0
    Pclass           0
    Sex              0
    Age              0
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    Title            0
    Title1           0
    Title2           0
    Sex1             0
    Age1             0
    dtype: int64




```python
train["Embarked1"] = train["Embarked"].fillna("S")
```


```python
train.isnull().sum()     #Embarked 1 열이 결측치 없음. EMbarked 아님 주의.
```




    PassengerId      0
    Survived         0
    Pclass           0
    Sex              0
    Age              0
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    Title            0
    Title1           0
    Title2           0
    Sex1             0
    Age1             0
    Embarked1        0
    dtype: int64




```python
#Embarked2를 S C Q 를 0 1 2 로 바꿈
embarked_mapping = {"S" : 0, "C" : 1, "Q" : 2}
train["Embarked2"] = train['Embarked1'].map(embarked_mapping)


```


```python
train.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Title</th>
      <th>Title1</th>
      <th>Title2</th>
      <th>Sex1</th>
      <th>Age1</th>
      <th>Embarked1</th>
      <th>Embarked2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>Mrs</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>C</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>Miss</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>Mrs</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Mr</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2.0</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(train["Embarked1"].value_counts()) ; train["Embarked2"].value_counts()

# 두 개가 같음을 확인. Embark1은 SCQ, Embark2는 012
```

    S    646
    C    168
    Q     77
    Name: Embarked1, dtype: int64
    




    0    646
    1    168
    2     77
    Name: Embarked2, dtype: int64




```python
train.isnull().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Sex              0
    Age              0
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    Title            0
    Title1           0
    Title2           0
    Sex1             0
    Age1             0
    Embarked1        0
    Embarked2        0
    dtype: int64



# 이제 실습. Fare 컬럼
  <= 17 이면 0 
  >17 and <= 30 이면 1
 >30 and <= 100 이면 2
 >100 이면 3   
  
해서 Fare 1 이라는 새로운 컬럼 만들기 .



```python
train_03 = train.copy()
train= train_03
```


```python
train.loc[train["Fare"] <= 17, "Fare1"] = 0
train.loc[(train["Fare"] > 17) & (train["Fare"] <= 30), "Fare1"] = 1
train.loc[(train["Fare"] >30) & (train["Fare"]<= 100), "Fare1"] = 2
train.loc[train["Fare"] > 100 , "Fare1"] = 3

```


```python

```


```python
# 이제 cabin . Cabin1열을 생성.

train["Cabin1"] = train["Cabin"].str[:1]
train["Cabin1"].value_counts()


```




    C    59
    B    47
    D    33
    E    32
    A    15
    F    13
    G     4
    T     1
    Name: Cabin1, dtype: int64




```python
#Pclass와 Embarked와 똑같은것임.

Pclass1 = train[train['Pclass']==1]['Cabin1'].value_counts()
Pclass2 = train[train['Pclass'] ==2]['Cabin1'].value_counts()
Pclass3 = train[train['Pclass'] ==3]['Cabin1'].value_counts()

df = pd.DataFrame([Pclass1,Pclass2,Pclass3])
df.index = ['1st class', '2nd class', '3rd class']
df.plot(kind = 'bar', stacked = True, figsize = (4,3))



```




    <matplotlib.axes._subplots.AxesSubplot at 0x28ef7b78370>




![png](output_49_1.png)



```python
#mapping 방식으로 한것.
# Cabin2를 만들어서 Cabin1에서의 알파벳을 숫자로 바꿈.



df.plot(kind = 'bar', stacked = True, figsize = (4,3))
cabin_mapping = {"A":0, "B" :0.4, "C":0.8, "D" : 1.2, "E" : 1.6, "F" : 2 , 
                "G" : 2.4, "T" : 2.8}

train["Cabin2"]  = train["Cabin1"].map(cabin_mapping)

# 결측치는 median 으로 채움.-- Cabin2만 해당.
train["Cabin2"].fillna(train.groupby("Pclass")["Cabin2"].transform("median"), inplace = True)
```


![png](output_50_0.png)



```python
#train.isnull().sum()
```


```python
train.columns
```




    Index(['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
           'Ticket', 'Fare', 'Cabin', 'Embarked', 'Title', 'Title1', 'Title2',
           'Sex1', 'Age1', 'Embarked1', 'Embarked2', 'Fare1', 'Cabin1', 'Cabin2'],
          dtype='object')




```python
# 가족 수를 합치자
train["FamilySize"] = train["SibSp"] + train["Parch"] + 1    #가족의 수


family_mapping = {1:0, 2:0.4, 3:0.8, 4:1.2, 5:1.6, 6:2, 7:2.4, 8:2.8, 9: 3.2, 10 :3.6
                 ,11:4}

train["FamilySize1"] = train['FamilySize'].map(family_mapping)

# Famliysize를 약간 정교하게 수치화 한 듯 하다.

```


```python
#마지막. train _ne w 만들기 : 필요없는 것 빼고 다듬는과정

sel_column = ["Survived","Pclass", "Title2", "Sex1", "Age1", "Embarked2", 
             "Fare1", "Cabin2", "FamilySize1"]

train_new = train[sel_column]








```


```python
train_04 = train.copy()
train = train_04
```


```python
train_new
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Title2</th>
      <th>Sex1</th>
      <th>Age1</th>
      <th>Embarked2</th>
      <th>Fare1</th>
      <th>Cabin2</th>
      <th>FamilySize1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>887</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.4</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>889</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.8</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>890</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2.0</td>
      <td>2</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 9 columns</p>
</div>




```python
# train_new의 컬럼들 이름 바꾸어주자!
train_new.columns = ["Survived","Pclass", "Title", "Sex", "Age", "Embarked", 
             "Fare", "Cabin", "FamilySize"]


```


```python
train_new.head
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Title</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Embarked</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>FamilySize</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0.8</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 이제 마지막. 엑셀로 저장하기

train_new.to_excel("C:/Users/ASIA_07/sjpark/train_new.xlsx")



```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
