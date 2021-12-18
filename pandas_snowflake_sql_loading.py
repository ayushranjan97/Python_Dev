import pandas as pd
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
def snow_load():
    try:
        # account = 'kg14021.ap-south-1.aws',
        #     user = 'AyushRanjan',
        #     password = 'Ayush@123',
        #     database = 'TRAINING',
        #     schema = 'PERSONAL',

        acc = input('Enter the Acoount name: ')
        usr = input('Enter the user name: ')
        pswd = input('Enter your password: ')
        db = input('Enter the database name: ')
        schema_name = input('Enter schema name: ')

        engine = create_engine(URL(
            account=acc,
            user=usr,
            password=pswd,
            database=db,
            schema=schema_name,
            warehouse='COMPUTE_WH',
            role='SYSADMIN',

        ))
        df = pd.read_csv('emp.csv')
        connection = engine.connect()
        try:
            table_name = input('Enter the table name where data is to be loaded: ')
            df.to_sql(table_name, connection, method='multi', index=False, if_exists='replace')
            print('data has been loaded successfully')

        finally:
            connection.close()
        engine.dispose()
    except:
        print("Please enter the details  correctly or check if you are authorized to access the data")


snow_load()