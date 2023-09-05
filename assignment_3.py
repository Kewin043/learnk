import pandas as pd
data = pd.Series([1,2,3,3,3,4,5,2,1,3])
print(data)
result = data.mode()
print(result)
