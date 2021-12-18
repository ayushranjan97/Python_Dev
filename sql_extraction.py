import pandas.io.sql
import pandas as pd
import pyodbc
import sys

server = 'Ayush-Dell\dev17'
db = 'personal'
#db2 = 'example'

#Create sql connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                      ';DATABASE=' + db +
                      ';Trusted_Connection=yes')
#Query db
sql = "select * from emp"
data_frame = pd.read_sql(sql, conn)
print (data_frame)
data_frame.to_csv('/Users/Ayush/Downloads/sample_extract1.csv',index = False)

