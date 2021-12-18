import pandas as pd
from sqlalchemy import create_engine
def load_sql():
    df = pd.read_csv('emp.csv')
    ServerName='Ayush-Dell\dev17'
    Database='personal'
    conn = create_engine('mssql+pyodbc://' + ServerName + '/' + Database+'?driver=SQL+Server+Native+Client+11.0')
    df.to_sql('emp', conn, method='multi',index=False, if_exists='replace')
    print('data has been loaded successfully')

load_sql()