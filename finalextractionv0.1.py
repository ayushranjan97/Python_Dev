import pyodbc
from os import system, name
import snowflake.connector
import pandas as pd
from time import sleep
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def extract_snowflake():
    try:
        conn = snowflake.connector.connect(
            user='AyushRanjan',
            password='Ayush@123',
            account='kg14021.ap-south-1.aws'
        )
        print("Connection established successfully")
        db = input("Please enter database name you want to use: ")
        schema = input("Please enter schema you want to use: ")
        table = input("Please enter the table name you want to use: ")
        columns = input("Please enter columns comma seperated or use * to get full table: ")
        cur = conn.cursor()
        try:
            sql = f'SELECT {columns} FROM "{db}"."{schema}"."{table}"'
            print(f'Executing "{sql}"')
            df1 = pd.read_sql(sql,conn)
            path=input("Please enter location of the file to save")
            df1.to_csv(f'{path}/{table}.csv',index=False)
            print(f'Your file has been extracted as {table}.csv in location {path}')
        finally:
            cur.close()
            conn.close()
    except:
        print("Please enter the details  correctly or check if you are authorized to access the data")

def sql_extration():
    try:
        server=input("Please Enter hostname\servername: ")
        db=input("Please enter database name")

        #Create sql connection
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                              ';DATABASE=' + db +
                              ';Trusted_Connection=yes')
        #Query
        schema=input("Please enter schema name: ")
        table=input("Please enter tablename: ")
        columns=input("Please enter the column comma seperated or * for full table: ")
        sql = f"select {columns} from [{schema}].[{table}]"
        print(f'Executing "{sql}"')
        data_frame = pd.read_sql(sql, conn)
        path=input("Enter path to save your exported csv: ")
        data_frame.to_csv(f'{path}/{table}.csv',index = False)
        print(f"Your CSV has been extracted successfully as {table}.csv to location {path}")
    except:
        print("Please enter the details  correctly or check if you are authorized to access the data")

def csv_extract():
    try:
        path = input("Please enter the path of csv")
        df1 = pd.read_csv(f"{path}")
        print(df1)
    except:
        print("Please enter the details correctly")

clear()
try:
    print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
    print("1 Snowflake Data Extraction")
    print("2 SQL file Extraction")
    print("3 CSV Extraction")
    n=int(input("Please enter your choice for extraction: "))
    if(n==1):
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        extract_snowflake()
        print("Thank you for using our service")
    elif(n==2):
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        sql_extration()
        print("Thank you for using our service")
    elif(n==3):
        clear()
        print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
        csv_extract()
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