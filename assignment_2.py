import pandas as pd
import numpy as np
df = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5,np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
                  index =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
df=df.fillna(0)
print(df)
result = df.score.describe()
print(result)
