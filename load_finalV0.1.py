import pandas as pd
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy import create_engine

from os import system, name
import pyodbc
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')
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

def sql_load():
      try:
        path = input("Enter the path: ")
        file = input("Enter the file name to be loaded: ")
        df = pd.read_csv(f"{path}/{file}.csv")
        ServerName = input("Please Enter hostname\servername: ")
        Database = input("Please enter database name: ")
        conn = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + '?driver=SQL+Server+Native+Client+11.0')
        df.to_sql('EMP', conn, method='multi', index=False, if_exists='replace')
        print('data has been loaded successfully')

      except:
        print("Please enter the details  correctly or check if you are authorized to access the data")
clear()
try:
    print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
    print("1 Snowflake Data Loading")
    print("2 SQL Data Loading")
    n = int(input("Please enter your choice for extraction: "))
    if (n == 1):
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        snow_load()
        print("Thank you for using our service")
    elif(n== 2):
         clear()
         print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
         sql_load()
         print("Thank you for using our service")
    else:
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        print("Please proceed with a valid choice")
        print("Thank you for using our service")
except:
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        print("Please enter a numerical value")
        print("Thank you for using our service")
