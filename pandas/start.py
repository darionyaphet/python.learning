'''
    10 Minutes to pandas:
    http://pandas.pydata.org/pandas-docs/stable/10min.html
'''

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

#Creating a Series by passing a list of values, letting pandas create a default integer index
s = pd.Series([1,3,5,np.nan,6,8])
'''
0     1
1     3
2     5
3   NaN
4     6
5     8
dtype: float64
'''

#Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
'''
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D', tz=None)
'''

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
'''
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
'''

#Creating a DataFrame by passing a dict of objects that can be converted to series-like
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

'''
   A          B  C  D      E    F
   0  1 2013-01-02  1  3   test  foo
   1  1 2013-01-02  1  3  train  foo
   2  1 2013-01-02  1  3   test  foo
   3  1 2013-01-02  1  3  train  foo
'''

df2.dtypes
'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
'''

df.head()
'''
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
'''

df.tail(3)
'''
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
'''



