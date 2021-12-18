# usr='AyushRanjan', password='Ayush@123', account='kg14021.ap-south-1.aws'
import pandas as pd
import snowflake.connector as sf

conn=sf.connect(user='AyushRanjan',password='Ayush@123',account='kg14021.ap-south-1.aws')

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()


try:
    sql = 'use role {}'.format('SYSADMIN')
    execute_query(conn, sql)

    sql = 'use database {}'.format('TRAINING')
    execute_query(conn, sql)

    sql = 'use warehouse {}'.format('COMPUTE_WH')
    execute_query(conn, sql)

    sql = 'use schema {}'.format('PERSONAL')
    execute_query(conn, sql)

    try:
        sql = 'alter warehouse {} resume'.format('COMPUTE_WH')
        execute_query(conn, sql)
    except:
        pass

    sql = 'truncate table if exists Covid_Master_Data'
    execute_query(conn, sql)

    #sql = 'create table student_math_mark(name varchar, mark double)'
    #execute_query(conn, sql)

    sql = 'drop stage if exists data_stage'
    execute_query(conn, sql)

    sql = 'create stage data_stage file_format = (type = "csv" field_delimiter = "," skip_header = 1)'
    execute_query(conn, sql)

    csv_file = 'C:\\Users\\Ayush\\Downloads\\covid.csv'
    sql = "PUT file://" + csv_file + " @DATA_STAGE auto_compress=true"
    execute_query(conn, sql)

    sql = 'copy into Covid_Master_Data from @DATA_STAGE/covid.csv.gz file_format = (type = "csv" field_delimiter = "," skip_header = 1)' \
          'ON_ERROR = "ABORT_STATEMENT" '
    execute_query(conn, sql)

    columns=input("Enter column name to fetch data seperated by comma: ")

    sql = f'SELECT {columns} FROM "TRAINING"."PERSONAL"."COVID_MASTER_DATA" LIMIT 10'
    cursor = conn.cursor()
    df1=pd.DataFrame(cursor.execute(sql))
    df1.to_csv('D:/sample.csv',index=False)
    print(df1)

except Exception as e:
    print(e)