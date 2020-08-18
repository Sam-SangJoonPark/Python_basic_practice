```python
# https://github.com/HyunSu-Jin/seoul_crime/blob/master/seoul_crime.ipynb
```


```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import platform
```


```python
frame = pd.read_csv('06.seoul_crime/seoul_crime_2015.csv',encoding='euc-kr')
frame.head()
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
      <th>관서명</th>
      <th>살인(발생)</th>
      <th>살인(검거)</th>
      <th>강도(발생)</th>
      <th>강도(검거)</th>
      <th>강간(발생)</th>
      <th>강간(검거)</th>
      <th>절도(발생)</th>
      <th>절도(검거)</th>
      <th>폭력(발생)</th>
      <th>폭력(검거)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>중부서</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>105</td>
      <td>65</td>
      <td>1,395</td>
      <td>477</td>
      <td>1,355</td>
      <td>1,170</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로서</td>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>115</td>
      <td>98</td>
      <td>1,070</td>
      <td>413</td>
      <td>1,278</td>
      <td>1,070</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남대문서</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>4</td>
      <td>65</td>
      <td>46</td>
      <td>1,153</td>
      <td>382</td>
      <td>869</td>
      <td>794</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서대문서</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>154</td>
      <td>124</td>
      <td>1,812</td>
      <td>738</td>
      <td>2,056</td>
      <td>1,711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>혜화서</td>
      <td>3</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>96</td>
      <td>63</td>
      <td>1,114</td>
      <td>424</td>
      <td>1,015</td>
      <td>861</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 후 이거 이해하였음!! 대신에 짅짜 코드를 하나씩 하나씩 쳐보면서 알았음! good ok.

# 이거는 뭐냐면 ,,그 1,153 1,395 이런식으로 되니까 계산이 안되는거.그 컴마없애주는것.
for tuple in frame.values:
    for ele in tuple[-1:-4:-1]:
        ele.replace(',','')

textData = frame[frame.columns[-4:]].values

for idx,row in enumerate(textData) :
    for idx2,ele in enumerate(row) :
        textData[idx][idx2] = int(ele.replace(',',''))
        
textData
frame[frame.columns[-4:]] = textData
```


```python

```


```python
frame['소계(발생)'] = frame['살인(발생)'] + frame['강도(발생)'] +\
frame['강간(발생)'] + frame['절도(발생)'] + frame['폭력(발생)']

frame['소계(검거)'] = frame['살인(검거)'] + frame['강도(검거)'] + frame['강간(검거)'] + frame['절도(검거)'] + frame['폭력(검거)']
```


```python
frame
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
      <th>관서명</th>
      <th>살인(발생)</th>
      <th>살인(검거)</th>
      <th>강도(발생)</th>
      <th>강도(검거)</th>
      <th>강간(발생)</th>
      <th>강간(검거)</th>
      <th>절도(발생)</th>
      <th>절도(검거)</th>
      <th>폭력(발생)</th>
      <th>폭력(검거)</th>
      <th>소계(발생)</th>
      <th>소계(검거)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>중부서</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>105</td>
      <td>65</td>
      <td>1395</td>
      <td>477</td>
      <td>1355</td>
      <td>1170</td>
      <td>2860</td>
      <td>1716</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로서</td>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>115</td>
      <td>98</td>
      <td>1070</td>
      <td>413</td>
      <td>1278</td>
      <td>1070</td>
      <td>2472</td>
      <td>1589</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남대문서</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>4</td>
      <td>65</td>
      <td>46</td>
      <td>1153</td>
      <td>382</td>
      <td>869</td>
      <td>794</td>
      <td>2094</td>
      <td>1226</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서대문서</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>154</td>
      <td>124</td>
      <td>1812</td>
      <td>738</td>
      <td>2056</td>
      <td>1711</td>
      <td>4029</td>
      <td>2579</td>
    </tr>
    <tr>
      <th>4</th>
      <td>혜화서</td>
      <td>3</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>96</td>
      <td>63</td>
      <td>1114</td>
      <td>424</td>
      <td>1015</td>
      <td>861</td>
      <td>2233</td>
      <td>1354</td>
    </tr>
    <tr>
      <th>5</th>
      <td>용산서</td>
      <td>5</td>
      <td>5</td>
      <td>14</td>
      <td>14</td>
      <td>194</td>
      <td>173</td>
      <td>1557</td>
      <td>587</td>
      <td>2050</td>
      <td>1704</td>
      <td>3820</td>
      <td>2483</td>
    </tr>
    <tr>
      <th>6</th>
      <td>성북서</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>86</td>
      <td>71</td>
      <td>953</td>
      <td>409</td>
      <td>1194</td>
      <td>1015</td>
      <td>2237</td>
      <td>1498</td>
    </tr>
    <tr>
      <th>7</th>
      <td>동대문서</td>
      <td>5</td>
      <td>5</td>
      <td>13</td>
      <td>13</td>
      <td>173</td>
      <td>146</td>
      <td>1981</td>
      <td>814</td>
      <td>2548</td>
      <td>2227</td>
      <td>4720</td>
      <td>3205</td>
    </tr>
    <tr>
      <th>8</th>
      <td>마포서</td>
      <td>8</td>
      <td>8</td>
      <td>14</td>
      <td>10</td>
      <td>294</td>
      <td>247</td>
      <td>2555</td>
      <td>813</td>
      <td>2983</td>
      <td>2519</td>
      <td>5854</td>
      <td>3597</td>
    </tr>
    <tr>
      <th>9</th>
      <td>영등포서</td>
      <td>14</td>
      <td>12</td>
      <td>22</td>
      <td>20</td>
      <td>295</td>
      <td>183</td>
      <td>2964</td>
      <td>978</td>
      <td>3572</td>
      <td>2961</td>
      <td>6867</td>
      <td>4154</td>
    </tr>
    <tr>
      <th>10</th>
      <td>성동서</td>
      <td>4</td>
      <td>4</td>
      <td>9</td>
      <td>8</td>
      <td>126</td>
      <td>119</td>
      <td>1607</td>
      <td>597</td>
      <td>1612</td>
      <td>1395</td>
      <td>3358</td>
      <td>2123</td>
    </tr>
    <tr>
      <th>11</th>
      <td>동작서</td>
      <td>5</td>
      <td>5</td>
      <td>9</td>
      <td>5</td>
      <td>285</td>
      <td>139</td>
      <td>1865</td>
      <td>661</td>
      <td>1910</td>
      <td>1587</td>
      <td>4074</td>
      <td>2397</td>
    </tr>
    <tr>
      <th>12</th>
      <td>광진서</td>
      <td>4</td>
      <td>4</td>
      <td>14</td>
      <td>26</td>
      <td>240</td>
      <td>220</td>
      <td>3026</td>
      <td>1277</td>
      <td>2625</td>
      <td>2180</td>
      <td>5909</td>
      <td>3707</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서부서</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>70</td>
      <td>59</td>
      <td>819</td>
      <td>293</td>
      <td>1192</td>
      <td>1038</td>
      <td>2085</td>
      <td>1393</td>
    </tr>
    <tr>
      <th>14</th>
      <td>강북서</td>
      <td>7</td>
      <td>8</td>
      <td>14</td>
      <td>13</td>
      <td>153</td>
      <td>126</td>
      <td>1434</td>
      <td>618</td>
      <td>2649</td>
      <td>2348</td>
      <td>4257</td>
      <td>3113</td>
    </tr>
    <tr>
      <th>15</th>
      <td>금천서</td>
      <td>3</td>
      <td>4</td>
      <td>6</td>
      <td>6</td>
      <td>151</td>
      <td>122</td>
      <td>1567</td>
      <td>888</td>
      <td>2054</td>
      <td>1776</td>
      <td>3781</td>
      <td>2796</td>
    </tr>
    <tr>
      <th>16</th>
      <td>중랑서</td>
      <td>13</td>
      <td>12</td>
      <td>11</td>
      <td>9</td>
      <td>187</td>
      <td>148</td>
      <td>2135</td>
      <td>829</td>
      <td>2847</td>
      <td>2407</td>
      <td>5193</td>
      <td>3405</td>
    </tr>
    <tr>
      <th>17</th>
      <td>강남서</td>
      <td>3</td>
      <td>3</td>
      <td>15</td>
      <td>12</td>
      <td>300</td>
      <td>225</td>
      <td>2411</td>
      <td>984</td>
      <td>2465</td>
      <td>2146</td>
      <td>5194</td>
      <td>3370</td>
    </tr>
    <tr>
      <th>18</th>
      <td>관악서</td>
      <td>9</td>
      <td>8</td>
      <td>12</td>
      <td>14</td>
      <td>320</td>
      <td>221</td>
      <td>2706</td>
      <td>827</td>
      <td>3298</td>
      <td>2642</td>
      <td>6345</td>
      <td>3712</td>
    </tr>
    <tr>
      <th>19</th>
      <td>강서서</td>
      <td>7</td>
      <td>8</td>
      <td>13</td>
      <td>13</td>
      <td>262</td>
      <td>191</td>
      <td>2096</td>
      <td>1260</td>
      <td>3207</td>
      <td>2718</td>
      <td>5585</td>
      <td>4190</td>
    </tr>
    <tr>
      <th>20</th>
      <td>강동서</td>
      <td>4</td>
      <td>3</td>
      <td>6</td>
      <td>8</td>
      <td>156</td>
      <td>123</td>
      <td>2366</td>
      <td>789</td>
      <td>2712</td>
      <td>2248</td>
      <td>5244</td>
      <td>3171</td>
    </tr>
    <tr>
      <th>21</th>
      <td>종암서</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>64</td>
      <td>53</td>
      <td>832</td>
      <td>332</td>
      <td>1015</td>
      <td>840</td>
      <td>1917</td>
      <td>1231</td>
    </tr>
    <tr>
      <th>22</th>
      <td>구로서</td>
      <td>8</td>
      <td>6</td>
      <td>15</td>
      <td>11</td>
      <td>281</td>
      <td>164</td>
      <td>2335</td>
      <td>889</td>
      <td>3007</td>
      <td>2432</td>
      <td>5646</td>
      <td>3502</td>
    </tr>
    <tr>
      <th>23</th>
      <td>서초서</td>
      <td>7</td>
      <td>4</td>
      <td>8</td>
      <td>5</td>
      <td>334</td>
      <td>193</td>
      <td>1982</td>
      <td>905</td>
      <td>1852</td>
      <td>1607</td>
      <td>4183</td>
      <td>2714</td>
    </tr>
    <tr>
      <th>24</th>
      <td>양천서</td>
      <td>3</td>
      <td>5</td>
      <td>6</td>
      <td>3</td>
      <td>120</td>
      <td>105</td>
      <td>1890</td>
      <td>672</td>
      <td>2509</td>
      <td>2030</td>
      <td>4528</td>
      <td>2815</td>
    </tr>
    <tr>
      <th>25</th>
      <td>송파서</td>
      <td>11</td>
      <td>10</td>
      <td>13</td>
      <td>10</td>
      <td>220</td>
      <td>178</td>
      <td>3239</td>
      <td>1129</td>
      <td>3295</td>
      <td>2786</td>
      <td>6778</td>
      <td>4113</td>
    </tr>
    <tr>
      <th>26</th>
      <td>노원서</td>
      <td>10</td>
      <td>10</td>
      <td>7</td>
      <td>7</td>
      <td>197</td>
      <td>121</td>
      <td>2193</td>
      <td>801</td>
      <td>2723</td>
      <td>2329</td>
      <td>5130</td>
      <td>3268</td>
    </tr>
    <tr>
      <th>27</th>
      <td>방배서</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>59</td>
      <td>56</td>
      <td>653</td>
      <td>186</td>
      <td>547</td>
      <td>491</td>
      <td>1261</td>
      <td>736</td>
    </tr>
    <tr>
      <th>28</th>
      <td>은평서</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>5</td>
      <td>96</td>
      <td>82</td>
      <td>1095</td>
      <td>418</td>
      <td>1461</td>
      <td>1268</td>
      <td>2660</td>
      <td>1774</td>
    </tr>
    <tr>
      <th>29</th>
      <td>도봉서</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>10</td>
      <td>102</td>
      <td>106</td>
      <td>1063</td>
      <td>478</td>
      <td>1487</td>
      <td>1303</td>
      <td>2664</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>30</th>
      <td>수서서</td>
      <td>10</td>
      <td>7</td>
      <td>6</td>
      <td>6</td>
      <td>149</td>
      <td>124</td>
      <td>1439</td>
      <td>666</td>
      <td>1819</td>
      <td>1559</td>
      <td>3423</td>
      <td>2362</td>
    </tr>
  </tbody>
</table>
</div>




```python
policeToArea = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
                '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
                '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
                '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
                '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
                '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
                '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
                '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}
```


```python
frame['구별'] = frame['관서명'].apply(lambda v:policeToArea.get(v,v))
frame.sort_values(by = '구별').head()
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
      <th>관서명</th>
      <th>살인(발생)</th>
      <th>살인(검거)</th>
      <th>강도(발생)</th>
      <th>강도(검거)</th>
      <th>강간(발생)</th>
      <th>강간(검거)</th>
      <th>절도(발생)</th>
      <th>절도(검거)</th>
      <th>폭력(발생)</th>
      <th>폭력(검거)</th>
      <th>소계(발생)</th>
      <th>소계(검거)</th>
      <th>구별</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>수서서</td>
      <td>10</td>
      <td>7</td>
      <td>6</td>
      <td>6</td>
      <td>149</td>
      <td>124</td>
      <td>1439</td>
      <td>666</td>
      <td>1819</td>
      <td>1559</td>
      <td>3423</td>
      <td>2362</td>
      <td>강남구</td>
    </tr>
    <tr>
      <th>17</th>
      <td>강남서</td>
      <td>3</td>
      <td>3</td>
      <td>15</td>
      <td>12</td>
      <td>300</td>
      <td>225</td>
      <td>2411</td>
      <td>984</td>
      <td>2465</td>
      <td>2146</td>
      <td>5194</td>
      <td>3370</td>
      <td>강남구</td>
    </tr>
    <tr>
      <th>20</th>
      <td>강동서</td>
      <td>4</td>
      <td>3</td>
      <td>6</td>
      <td>8</td>
      <td>156</td>
      <td>123</td>
      <td>2366</td>
      <td>789</td>
      <td>2712</td>
      <td>2248</td>
      <td>5244</td>
      <td>3171</td>
      <td>강동구</td>
    </tr>
    <tr>
      <th>14</th>
      <td>강북서</td>
      <td>7</td>
      <td>8</td>
      <td>14</td>
      <td>13</td>
      <td>153</td>
      <td>126</td>
      <td>1434</td>
      <td>618</td>
      <td>2649</td>
      <td>2348</td>
      <td>4257</td>
      <td>3113</td>
      <td>강북구</td>
    </tr>
    <tr>
      <th>19</th>
      <td>강서서</td>
      <td>7</td>
      <td>8</td>
      <td>13</td>
      <td>13</td>
      <td>262</td>
      <td>191</td>
      <td>2096</td>
      <td>1260</td>
      <td>3207</td>
      <td>2718</td>
      <td>5585</td>
      <td>4190</td>
      <td>강서구</td>
    </tr>
  </tbody>
</table>
</div>




```python

frame_by_gu = pd.pivot_table(frame, index='구별', aggfunc=np.sum)
frame_by_gu.head()
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
      <th>강간(검거)</th>
      <th>강간(발생)</th>
      <th>강도(검거)</th>
      <th>강도(발생)</th>
      <th>살인(검거)</th>
      <th>살인(발생)</th>
      <th>소계(검거)</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도(발생)</th>
      <th>폭력(검거)</th>
      <th>폭력(발생)</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>349</td>
      <td>449</td>
      <td>18</td>
      <td>21</td>
      <td>10</td>
      <td>13</td>
      <td>5732</td>
      <td>8617</td>
      <td>1650</td>
      <td>3850</td>
      <td>3705</td>
      <td>4284</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>123</td>
      <td>156</td>
      <td>8</td>
      <td>6</td>
      <td>3</td>
      <td>4</td>
      <td>3171</td>
      <td>5244</td>
      <td>789</td>
      <td>2366</td>
      <td>2248</td>
      <td>2712</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>126</td>
      <td>153</td>
      <td>13</td>
      <td>14</td>
      <td>8</td>
      <td>7</td>
      <td>3113</td>
      <td>4257</td>
      <td>618</td>
      <td>1434</td>
      <td>2348</td>
      <td>2649</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>191</td>
      <td>262</td>
      <td>13</td>
      <td>13</td>
      <td>8</td>
      <td>7</td>
      <td>4190</td>
      <td>5585</td>
      <td>1260</td>
      <td>2096</td>
      <td>2718</td>
      <td>3207</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>221</td>
      <td>320</td>
      <td>14</td>
      <td>12</td>
      <td>8</td>
      <td>9</td>
      <td>3712</td>
      <td>6345</td>
      <td>827</td>
      <td>2706</td>
      <td>2642</td>
      <td>3298</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu['강간검거율'] = frame_by_gu['강간(검거)'] / frame_by_gu['강간(발생)'] * 100
frame_by_gu['강도검거율'] = frame_by_gu['강도(검거)']/frame_by_gu['강도(발생)']*100
frame_by_gu['살인검거율'] = frame_by_gu['살인(검거)']/frame_by_gu['살인(발생)']*100
frame_by_gu['절도검거율'] = frame_by_gu['절도(검거)']/frame_by_gu['절도(발생)']*100
frame_by_gu['폭력검거율'] = frame_by_gu['폭력(검거)']/frame_by_gu['폭력(발생)']*100
frame_by_gu['검거율'] = frame_by_gu['소계(검거)']/frame_by_gu['소계(발생)']*100


del frame_by_gu['강간(검거)']
del frame_by_gu['강도(검거)']
del frame_by_gu['살인(검거)']
del frame_by_gu['절도(검거)']
del frame_by_gu['폭력(검거)']


```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2645             try:
    -> 2646                 return self._engine.get_loc(key)
       2647             except KeyError:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: '강간(검거)'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-75-9c5821455522> in <module>
    ----> 1 frame_by_gu['강간검거율'] = frame_by_gu['강간(검거)'] / frame_by_gu['강간(발생)'] * 100
          2 frame_by_gu['강도검거율'] = frame_by_gu['강도(검거)']/frame_by_gu['강도(발생)']*100
          3 frame_by_gu['살인검거율'] = frame_by_gu['살인(검거)']/frame_by_gu['살인(발생)']*100
          4 frame_by_gu['절도검거율'] = frame_by_gu['절도(검거)']/frame_by_gu['절도(발생)']*100
          5 frame_by_gu['폭력검거율'] = frame_by_gu['폭력(검거)']/frame_by_gu['폭력(발생)']*100
    

    C:\anaconda3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
       2798             if self.columns.nlevels > 1:
       2799                 return self._getitem_multilevel(key)
    -> 2800             indexer = self.columns.get_loc(key)
       2801             if is_integer(indexer):
       2802                 indexer = [indexer]
    

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2646                 return self._engine.get_loc(key)
       2647             except KeyError:
    -> 2648                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2649         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
       2650         if indexer.ndim > 1 or indexer.size > 1:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: '강간(검거)'



```python
frame_by_gu
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
      <th>강간(발생)</th>
      <th>강도(발생)</th>
      <th>살인(검거)</th>
      <th>살인(발생)</th>
      <th>소계(검거)</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도(발생)</th>
      <th>폭력(검거)</th>
      <th>폭력(발생)</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>449</td>
      <td>21</td>
      <td>10</td>
      <td>13</td>
      <td>5732</td>
      <td>8617</td>
      <td>1650</td>
      <td>3850</td>
      <td>3705</td>
      <td>4284</td>
      <td>77.728285</td>
      <td>85.714286</td>
      <td>76.923077</td>
      <td>42.857143</td>
      <td>86.484594</td>
      <td>66.519670</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>156</td>
      <td>6</td>
      <td>3</td>
      <td>4</td>
      <td>3171</td>
      <td>5244</td>
      <td>789</td>
      <td>2366</td>
      <td>2248</td>
      <td>2712</td>
      <td>78.846154</td>
      <td>133.333333</td>
      <td>75.000000</td>
      <td>33.347422</td>
      <td>82.890855</td>
      <td>60.469108</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>153</td>
      <td>14</td>
      <td>8</td>
      <td>7</td>
      <td>3113</td>
      <td>4257</td>
      <td>618</td>
      <td>1434</td>
      <td>2348</td>
      <td>2649</td>
      <td>82.352941</td>
      <td>92.857143</td>
      <td>114.285714</td>
      <td>43.096234</td>
      <td>88.637222</td>
      <td>73.126615</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>262</td>
      <td>13</td>
      <td>8</td>
      <td>7</td>
      <td>4190</td>
      <td>5585</td>
      <td>1260</td>
      <td>2096</td>
      <td>2718</td>
      <td>3207</td>
      <td>72.900763</td>
      <td>100.000000</td>
      <td>114.285714</td>
      <td>60.114504</td>
      <td>84.752105</td>
      <td>75.022381</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>320</td>
      <td>12</td>
      <td>8</td>
      <td>9</td>
      <td>3712</td>
      <td>6345</td>
      <td>827</td>
      <td>2706</td>
      <td>2642</td>
      <td>3298</td>
      <td>69.062500</td>
      <td>116.666667</td>
      <td>88.888889</td>
      <td>30.561715</td>
      <td>80.109157</td>
      <td>58.502758</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>240</td>
      <td>14</td>
      <td>4</td>
      <td>4</td>
      <td>3707</td>
      <td>5909</td>
      <td>1277</td>
      <td>3026</td>
      <td>2180</td>
      <td>2625</td>
      <td>91.666667</td>
      <td>185.714286</td>
      <td>100.000000</td>
      <td>42.200925</td>
      <td>83.047619</td>
      <td>62.734811</td>
    </tr>
    <tr>
      <th>구로구</th>
      <td>281</td>
      <td>15</td>
      <td>6</td>
      <td>8</td>
      <td>3502</td>
      <td>5646</td>
      <td>889</td>
      <td>2335</td>
      <td>2432</td>
      <td>3007</td>
      <td>58.362989</td>
      <td>73.333333</td>
      <td>75.000000</td>
      <td>38.072805</td>
      <td>80.877951</td>
      <td>62.026213</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>151</td>
      <td>6</td>
      <td>4</td>
      <td>3</td>
      <td>2796</td>
      <td>3781</td>
      <td>888</td>
      <td>1567</td>
      <td>1776</td>
      <td>2054</td>
      <td>80.794702</td>
      <td>100.000000</td>
      <td>133.333333</td>
      <td>56.668794</td>
      <td>86.465433</td>
      <td>73.948691</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>197</td>
      <td>7</td>
      <td>10</td>
      <td>10</td>
      <td>3268</td>
      <td>5130</td>
      <td>801</td>
      <td>2193</td>
      <td>2329</td>
      <td>2723</td>
      <td>61.421320</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>36.525308</td>
      <td>85.530665</td>
      <td>63.703704</td>
    </tr>
    <tr>
      <th>도봉구</th>
      <td>102</td>
      <td>9</td>
      <td>3</td>
      <td>3</td>
      <td>1900</td>
      <td>2664</td>
      <td>478</td>
      <td>1063</td>
      <td>1303</td>
      <td>1487</td>
      <td>103.921569</td>
      <td>111.111111</td>
      <td>100.000000</td>
      <td>44.967074</td>
      <td>87.626093</td>
      <td>71.321321</td>
    </tr>
    <tr>
      <th>동대문구</th>
      <td>173</td>
      <td>13</td>
      <td>5</td>
      <td>5</td>
      <td>3205</td>
      <td>4720</td>
      <td>814</td>
      <td>1981</td>
      <td>2227</td>
      <td>2548</td>
      <td>84.393064</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>41.090358</td>
      <td>87.401884</td>
      <td>67.902542</td>
    </tr>
    <tr>
      <th>동작구</th>
      <td>285</td>
      <td>9</td>
      <td>5</td>
      <td>5</td>
      <td>2397</td>
      <td>4074</td>
      <td>661</td>
      <td>1865</td>
      <td>1587</td>
      <td>1910</td>
      <td>48.771930</td>
      <td>55.555556</td>
      <td>100.000000</td>
      <td>35.442359</td>
      <td>83.089005</td>
      <td>58.836524</td>
    </tr>
    <tr>
      <th>마포구</th>
      <td>294</td>
      <td>14</td>
      <td>8</td>
      <td>8</td>
      <td>3597</td>
      <td>5854</td>
      <td>813</td>
      <td>2555</td>
      <td>2519</td>
      <td>2983</td>
      <td>84.013605</td>
      <td>71.428571</td>
      <td>100.000000</td>
      <td>31.819961</td>
      <td>84.445189</td>
      <td>61.445166</td>
    </tr>
    <tr>
      <th>서대문구</th>
      <td>154</td>
      <td>5</td>
      <td>2</td>
      <td>2</td>
      <td>2579</td>
      <td>4029</td>
      <td>738</td>
      <td>1812</td>
      <td>1711</td>
      <td>2056</td>
      <td>80.519481</td>
      <td>80.000000</td>
      <td>100.000000</td>
      <td>40.728477</td>
      <td>83.219844</td>
      <td>64.010921</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>393</td>
      <td>9</td>
      <td>6</td>
      <td>8</td>
      <td>3450</td>
      <td>5444</td>
      <td>1091</td>
      <td>2635</td>
      <td>2098</td>
      <td>2399</td>
      <td>63.358779</td>
      <td>66.666667</td>
      <td>75.000000</td>
      <td>41.404175</td>
      <td>87.453105</td>
      <td>63.372520</td>
    </tr>
    <tr>
      <th>성동구</th>
      <td>126</td>
      <td>9</td>
      <td>4</td>
      <td>4</td>
      <td>2123</td>
      <td>3358</td>
      <td>597</td>
      <td>1607</td>
      <td>1395</td>
      <td>1612</td>
      <td>94.444444</td>
      <td>88.888889</td>
      <td>100.000000</td>
      <td>37.149969</td>
      <td>86.538462</td>
      <td>63.222156</td>
    </tr>
    <tr>
      <th>성북구</th>
      <td>150</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>2729</td>
      <td>4154</td>
      <td>741</td>
      <td>1785</td>
      <td>1855</td>
      <td>2209</td>
      <td>82.666667</td>
      <td>80.000000</td>
      <td>100.000000</td>
      <td>41.512605</td>
      <td>83.974649</td>
      <td>65.695715</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>220</td>
      <td>13</td>
      <td>10</td>
      <td>11</td>
      <td>4113</td>
      <td>6778</td>
      <td>1129</td>
      <td>3239</td>
      <td>2786</td>
      <td>3295</td>
      <td>80.909091</td>
      <td>76.923077</td>
      <td>90.909091</td>
      <td>34.856437</td>
      <td>84.552352</td>
      <td>60.681617</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>120</td>
      <td>6</td>
      <td>5</td>
      <td>3</td>
      <td>2815</td>
      <td>4528</td>
      <td>672</td>
      <td>1890</td>
      <td>2030</td>
      <td>2509</td>
      <td>87.500000</td>
      <td>50.000000</td>
      <td>166.666667</td>
      <td>35.555556</td>
      <td>80.908729</td>
      <td>62.168728</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>295</td>
      <td>22</td>
      <td>12</td>
      <td>14</td>
      <td>4154</td>
      <td>6867</td>
      <td>978</td>
      <td>2964</td>
      <td>2961</td>
      <td>3572</td>
      <td>62.033898</td>
      <td>90.909091</td>
      <td>85.714286</td>
      <td>32.995951</td>
      <td>82.894737</td>
      <td>60.492209</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>194</td>
      <td>14</td>
      <td>5</td>
      <td>5</td>
      <td>2483</td>
      <td>3820</td>
      <td>587</td>
      <td>1557</td>
      <td>1704</td>
      <td>2050</td>
      <td>89.175258</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>37.700706</td>
      <td>83.121951</td>
      <td>65.000000</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>166</td>
      <td>9</td>
      <td>3</td>
      <td>3</td>
      <td>3167</td>
      <td>4745</td>
      <td>711</td>
      <td>1914</td>
      <td>2306</td>
      <td>2653</td>
      <td>84.939759</td>
      <td>66.666667</td>
      <td>100.000000</td>
      <td>37.147335</td>
      <td>86.920467</td>
      <td>66.743941</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>211</td>
      <td>11</td>
      <td>5</td>
      <td>6</td>
      <td>2943</td>
      <td>4705</td>
      <td>837</td>
      <td>2184</td>
      <td>1931</td>
      <td>2293</td>
      <td>76.303318</td>
      <td>81.818182</td>
      <td>83.333333</td>
      <td>38.324176</td>
      <td>84.212822</td>
      <td>62.550478</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>170</td>
      <td>9</td>
      <td>2</td>
      <td>3</td>
      <td>2942</td>
      <td>4954</td>
      <td>859</td>
      <td>2548</td>
      <td>1964</td>
      <td>2224</td>
      <td>65.294118</td>
      <td>66.666667</td>
      <td>66.666667</td>
      <td>33.712716</td>
      <td>88.309353</td>
      <td>59.386354</td>
    </tr>
    <tr>
      <th>중랑구</th>
      <td>187</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>3405</td>
      <td>5193</td>
      <td>829</td>
      <td>2135</td>
      <td>2407</td>
      <td>2847</td>
      <td>79.144385</td>
      <td>81.818182</td>
      <td>92.307692</td>
      <td>38.829040</td>
      <td>84.545135</td>
      <td>65.569035</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu[frame_by_gu[['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']]>100] = 100
```


```python
frame_by_gu.head(2)
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
      <th>강간(발생)</th>
      <th>강도(발생)</th>
      <th>살인(검거)</th>
      <th>살인(발생)</th>
      <th>소계(검거)</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도(발생)</th>
      <th>폭력(검거)</th>
      <th>폭력(발생)</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>449</td>
      <td>21</td>
      <td>10</td>
      <td>13</td>
      <td>5732</td>
      <td>8617</td>
      <td>1650</td>
      <td>3850</td>
      <td>3705</td>
      <td>4284</td>
      <td>77.728285</td>
      <td>85.714286</td>
      <td>76.923077</td>
      <td>42.857143</td>
      <td>86.484594</td>
      <td>66.519670</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>156</td>
      <td>6</td>
      <td>3</td>
      <td>4</td>
      <td>3171</td>
      <td>5244</td>
      <td>789</td>
      <td>2366</td>
      <td>2248</td>
      <td>2712</td>
      <td>78.846154</td>
      <td>100.000000</td>
      <td>75.000000</td>
      <td>33.347422</td>
      <td>82.890855</td>
      <td>60.469108</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu.rename(columns = {'강간(발생)':'강간', 
                       '강도(발생)':'강도', 
                       '살인(발생)':'살인', 
                       '절도(발생)':'절도', 
                       '폭력(발생)':'폭력'}, inplace=True)
#del frame_by_gu['소계(발생)']
del frame_by_gu['소계(검거)']

frame_by_gu.head(2)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2645             try:
    -> 2646                 return self._engine.get_loc(key)
       2647             except KeyError:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: '소계(검거)'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-82-802f4dc7c13b> in <module>
          5                        '폭력(발생)':'폭력'}, inplace=True)
          6 #del frame_by_gu['소계(발생)']
    ----> 7 del frame_by_gu['소계(검거)']
          8 
          9 frame_by_gu.head(2)
    

    C:\anaconda3\lib\site-packages\pandas\core\generic.py in __delitem__(self, key)
       3757             # there was no match, this call should raise the appropriate
       3758             # exception:
    -> 3759             self._data.delete(key)
       3760 
       3761         # delete from the caches
    

    C:\anaconda3\lib\site-packages\pandas\core\internals\managers.py in delete(self, item)
       1000         Delete selected item (items if non-unique) in-place.
       1001         """
    -> 1002         indexer = self.items.get_loc(item)
       1003 
       1004         is_deleted = np.zeros(self.shape[0], dtype=np.bool_)
    

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2646                 return self._engine.get_loc(key)
       2647             except KeyError:
    -> 2648                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2649         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
       2650         if indexer.ndim > 1 or indexer.size > 1:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: '소계(검거)'



```python
frame_by_gu.head(2)
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
      <th>강간</th>
      <th>강도</th>
      <th>살인(검거)</th>
      <th>살인</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도</th>
      <th>폭력(검거)</th>
      <th>폭력</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>449</td>
      <td>21</td>
      <td>10</td>
      <td>13</td>
      <td>8617</td>
      <td>1650</td>
      <td>3850</td>
      <td>3705</td>
      <td>4284</td>
      <td>77.728285</td>
      <td>85.714286</td>
      <td>76.923077</td>
      <td>42.857143</td>
      <td>86.484594</td>
      <td>66.519670</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>156</td>
      <td>6</td>
      <td>3</td>
      <td>4</td>
      <td>5244</td>
      <td>789</td>
      <td>2366</td>
      <td>2248</td>
      <td>2712</td>
      <td>78.846154</td>
      <td>100.000000</td>
      <td>75.000000</td>
      <td>33.347422</td>
      <td>82.890855</td>
      <td>60.469108</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
population = pd.read_csv('06.seoul_crime/seoul_population.csv',index_col='구별')
population.head()
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
      <th>인구수</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>581760</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>463321</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>334426</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>595691</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>529031</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu = frame_by_gu.join(population)
```


```python
frame_by_gu.head(2)
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
      <th>강간</th>
      <th>강도</th>
      <th>살인(검거)</th>
      <th>살인</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도</th>
      <th>폭력(검거)</th>
      <th>폭력</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
      <th>인구수</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>449</td>
      <td>21</td>
      <td>10</td>
      <td>13</td>
      <td>8617</td>
      <td>1650</td>
      <td>3850</td>
      <td>3705</td>
      <td>4284</td>
      <td>77.728285</td>
      <td>85.714286</td>
      <td>76.923077</td>
      <td>42.857143</td>
      <td>86.484594</td>
      <td>66.519670</td>
      <td>581760</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>156</td>
      <td>6</td>
      <td>3</td>
      <td>4</td>
      <td>5244</td>
      <td>789</td>
      <td>2366</td>
      <td>2248</td>
      <td>2712</td>
      <td>78.846154</td>
      <td>100.000000</td>
      <td>75.000000</td>
      <td>33.347422</td>
      <td>82.890855</td>
      <td>60.469108</td>
      <td>463321</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu.sort_values(by='검거율',ascending=False).head(2)
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
      <th>강간</th>
      <th>강도</th>
      <th>살인(검거)</th>
      <th>살인</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도</th>
      <th>폭력(검거)</th>
      <th>폭력</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
      <th>인구수</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강서구</th>
      <td>262</td>
      <td>13</td>
      <td>8</td>
      <td>7</td>
      <td>5585</td>
      <td>1260</td>
      <td>2096</td>
      <td>2718</td>
      <td>3207</td>
      <td>72.900763</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>60.114504</td>
      <td>84.752105</td>
      <td>75.022381</td>
      <td>595691</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>151</td>
      <td>6</td>
      <td>4</td>
      <td>3</td>
      <td>3781</td>
      <td>888</td>
      <td>1567</td>
      <td>1776</td>
      <td>2054</td>
      <td>80.794702</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>56.668794</td>
      <td>86.465433</td>
      <td>73.948691</td>
      <td>256167</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame_by_gu['범죄/인구수'] = frame_by_gu['소계(발생)']/ frame_by_gu['인구수']
frame_by_gu.sort_values(by = '범죄/인구수',ascending=False).head()
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
      <th>강간</th>
      <th>강도</th>
      <th>살인(검거)</th>
      <th>살인</th>
      <th>소계(발생)</th>
      <th>절도(검거)</th>
      <th>절도</th>
      <th>폭력(검거)</th>
      <th>폭력</th>
      <th>강간검거율</th>
      <th>강도검거율</th>
      <th>살인검거율</th>
      <th>절도검거율</th>
      <th>폭력검거율</th>
      <th>검거율</th>
      <th>인구수</th>
      <th>범죄/인구수</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>중구</th>
      <td>170</td>
      <td>9</td>
      <td>2</td>
      <td>3</td>
      <td>4954</td>
      <td>859</td>
      <td>2548</td>
      <td>1964</td>
      <td>2224</td>
      <td>65.294118</td>
      <td>66.666667</td>
      <td>66.666667</td>
      <td>33.712716</td>
      <td>88.309353</td>
      <td>59.386354</td>
      <td>134329</td>
      <td>0.036880</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>211</td>
      <td>11</td>
      <td>5</td>
      <td>6</td>
      <td>4705</td>
      <td>837</td>
      <td>2184</td>
      <td>1931</td>
      <td>2293</td>
      <td>76.303318</td>
      <td>81.818182</td>
      <td>83.333333</td>
      <td>38.324176</td>
      <td>84.212822</td>
      <td>62.550478</td>
      <td>163822</td>
      <td>0.028720</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>295</td>
      <td>22</td>
      <td>12</td>
      <td>14</td>
      <td>6867</td>
      <td>978</td>
      <td>2964</td>
      <td>2961</td>
      <td>3572</td>
      <td>62.033898</td>
      <td>90.909091</td>
      <td>85.714286</td>
      <td>32.995951</td>
      <td>82.894737</td>
      <td>60.492209</td>
      <td>417811</td>
      <td>0.016436</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>240</td>
      <td>14</td>
      <td>4</td>
      <td>4</td>
      <td>5909</td>
      <td>1277</td>
      <td>3026</td>
      <td>2180</td>
      <td>2625</td>
      <td>91.666667</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>42.200925</td>
      <td>83.047619</td>
      <td>62.734811</td>
      <td>375180</td>
      <td>0.015750</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>194</td>
      <td>14</td>
      <td>5</td>
      <td>5</td>
      <td>3820</td>
      <td>587</td>
      <td>1557</td>
      <td>1704</td>
      <td>2050</td>
      <td>89.175258</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>37.700706</td>
      <td>83.121951</td>
      <td>65.000000</td>
      <td>247909</td>
      <td>0.015409</td>
    </tr>
  </tbody>
</table>
</div>




```python
target_col = ['강간', '강도', '살인', '절도', '폭력','소계(발생)']
max_column = frame_by_gu[target_col].max() # vector
min_column = frame_by_gu[target_col].min()
crime_count_norm = (frame_by_gu[target_col] - min_column)/max_column
crime_count_norm.sort_values(by='소계(발생)',ascending=False).head()
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
      <th>강간</th>
      <th>강도</th>
      <th>살인</th>
      <th>절도</th>
      <th>폭력</th>
      <th>소계(발생)</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>0.772829</td>
      <td>0.727273</td>
      <td>0.785714</td>
      <td>0.723896</td>
      <td>0.652894</td>
      <td>0.690844</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>0.429844</td>
      <td>0.772727</td>
      <td>0.857143</td>
      <td>0.493766</td>
      <td>0.486695</td>
      <td>0.487757</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>0.262806</td>
      <td>0.363636</td>
      <td>0.642857</td>
      <td>0.565195</td>
      <td>0.422035</td>
      <td>0.477428</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>0.485523</td>
      <td>0.318182</td>
      <td>0.500000</td>
      <td>0.426753</td>
      <td>0.422736</td>
      <td>0.427179</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>0.307350</td>
      <td>0.409091</td>
      <td>0.142857</td>
      <td>0.509870</td>
      <td>0.265640</td>
      <td>0.376581</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (10,10))
sns.heatmap(crime_count_norm.sort_values(by='소계(발생)', ascending=False), annot=True, fmt='f', linewidths=.5)
plt.title('서울시 구별 강력범죄 발생빈도')
plt.show()
```


![png](output_23_0.png)



```python
target_col = ['강간', '강도', '살인', '절도', '폭력','소계(발생)']
frame_temp = frame_by_gu[target_col].div(frame_by_gu['인구수'],axis=0)
max_column = frame_temp.max() # vector
min_column = frame_temp.min()
crime_count_norm = (frame_temp - min_column)/max_column
crime_count_norm.head()
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
      <th>강간</th>
      <th>강도</th>
      <th>살인</th>
      <th>절도</th>
      <th>폭력</th>
      <th>소계(발생)</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>0.408703</td>
      <td>0.379011</td>
      <td>0.447146</td>
      <td>0.190242</td>
      <td>0.190517</td>
      <td>0.197138</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>0.070891</td>
      <td>0.034279</td>
      <td>0.072740</td>
      <td>0.110570</td>
      <td>0.099285</td>
      <td>0.102406</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>0.164681</td>
      <td>0.464875</td>
      <td>0.408522</td>
      <td>0.067411</td>
      <td>0.224170</td>
      <td>0.140665</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>0.150958</td>
      <td>0.166430</td>
      <td>0.157865</td>
      <td>0.026851</td>
      <td>0.070914</td>
      <td>0.049731</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>0.279107</td>
      <td>0.179232</td>
      <td>0.301515</td>
      <td>0.111013</td>
      <td>0.122276</td>
      <td>0.120718</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (10,10))
sns.heatmap(crime_count_norm.sort_values(by='소계(발생)', ascending=False), annot=True, fmt='f', linewidths=.5)
plt.title('서울시 구별 인구수대비 강력범죄 발생빈도')
plt.show()
```


![png](output_25_0.png)



```python

```


```python
import re
```


```python

```


```python

```


```python
p.match("")
```


```python
p = re.compile('[a-z]+')
```


```python
m = p.match('tempo'); m.group()
```




    'tempo'




```python
m = p.search('   454 messagezzzz 45 sdf         message')
```


```python
print(m)
```

    <re.Match object; span=(7, 18), match='messagezzzz'>
    


```python
'123'.isdigit()
```




    True




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
