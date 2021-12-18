# import pandas module
import pandas as pd
# making dataframe
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}
path = "C:\\Users\\Ayush\\Downloads"
df1 = pd.read_csv(f'{path}\\covid.csv')
print(df1.date)
df2 = pd.DataFrame(dummy_data1, columns = ['id','Feature1', 'Feature2'])
df_col=pd.concat([df1,df2],axis=1)
# output the dataframe
df_col.to_csv(f'{path}\\sample.csv',columns=['date','location','Feature1','Feature2'],index=False,encoding='utf-8')
print('done')
