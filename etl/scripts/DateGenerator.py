import os
import pathlib
import datetime

START_DATE = datetime.date(2020, 10, 24)
END_DATE = datetime.date(2021, 10, 24)
FILE_NAME = f'{pathlib.Path().resolve()}\etl\sql\ETL_load_date.sql'
DW_NAME = 'agencyDW'
DIMENSION_NAME = 'Date'


try:
    os.remove(FILE_NAME)
except:
    pass

id = 1
with open(FILE_NAME, 'a+') as sql_file:
    sql_file.write(f'USE {DW_NAME}\n')
    sql_file.write('GO\n')
    sql_file.write('\n')
    current_date = START_DATE
    while current_date <= END_DATE:
        if current_date.weekday() not in [5,6]:
            sql_file.write(f'INSERT INTO dbo.{DIMENSION_NAME} values({id},\'{current_date}\',{current_date.year},{current_date.strftime("%B")},{current_date.month},{current_date.strftime("%A")},{current_date.weekday()+1});\n')
        current_date += datetime.timedelta(days=1)
        id += 1
