import os
import pathlib

HOURS = 16
MINUTES = 60
SECONDS = 60
FILE_NAME = f'{pathlib.Path().resolve()}\etl\sql\ETL_load_time.sql'
DW_NAME = 'agencyDW'
DIMENSION_NAME = 'Time'

try:
    os.remove(FILE_NAME)
except:
    pass

id = 1
with open(FILE_NAME, 'a+') as sql_file:
    sql_file.write(f'USE {DW_NAME}\n')
    sql_file.write('GO\n')
    sql_file.write('\n')
    for hour in range(8, HOURS):
        for minute in range(MINUTES):
            for second in range(SECONDS):
                sql_file.write(f'INSERT INTO dbo.{DIMENSION_NAME} values({id},{hour},{minute},{second});\n')
                id += 1
