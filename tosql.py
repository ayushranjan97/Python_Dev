import pandas as pd
import sqlalchemy as sa
from os import system, name
import pyodbc
import urllib
# path = input("Enter the path: ")
# file = input("Enter the file name to be loaded: ")
df = pd.read_csv('emp.csv')
ServerName='Ayush-Dell\dev17'
Database='personal'
engine = sa.create_engine('mssql+pyodbc://' + ServerName + '/' + Database+'?driver=SQL+Server+Native+Client+11.0')
conn=engine.connect()
df.to_sql('emp',con=conn,schema='dbo',if_exists='replace',method='multi',index=False)
conn.close()