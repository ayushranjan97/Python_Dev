import pandas as pd
from os import system, name
import pyodbc
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')
def sql_load():
     try:
        path = input("Enter the path: ")
        file = input("Enter the file name to be loaded: ")
        df = pd.read_csv(f"{path}/{file}.csv")
        print(f"Reading {file}.csv from {path}")
        server = input("Please Enter hostname\servername: ")
        db = input("Please enter database name: ")

        # Create sql connection
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                              ';DATABASE=' + db +
                              ';Trusted_Connection=yes')

        # sql=input("Enter the insert statement in the format : \n\'\'\'INSERT INTO SCHEMA.TABLE(COL1,COL2,COL3)values(?,?,?)\'\'\',row.COL1,row.COL2,row.COL3:\n")
        # print(f'Executing {sql}')
        cursor=conn.cursor()
        for row in df.itertuples():
            cursor.execute('''INSERT INTO dbo.emp(EMPNO,ENAME,JOB) values(?,?,?)''',row.EMPNO,row.ENAME,row.JOB
)
        conn.commit()
     except:
        print("Please enter the details  correctly or check if you are authorized to access the data")
clear()
#try:
print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
print("1 Snowflake Data Loading")
print("2 SQL Data Loading")
n = int(input("Please enter your choice for extraction: "))
if(n== 2):
     clear()
     print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
     sql_load()
     print("Thank you for using our service")
else:
    clear()
    print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
    print("Please proceed with a valid choice")
    print("Thank you for using our service")
# except:
#         clear()
#         print("\t\t\t\t\t\t****Welcome to SwarnAyu most simplistic ETL Tool****")
#         print("Please enter a numerical value")
#         print("Thank you for using our service")