from datetime import datetime
import sqlite3
import database as dbase
import windows as win

def get_current_day():
    return datetime.now().day

def get_current_month():
    return datetime.now().month

def get_current_year():
    return datetime.now().year

def get_current_month_str():
    current_month = get_current_month()
    
    for i in range(len(win.month_num_list) - 1):
        if current_month == win.month_num_list[i]:
            return win.month_list[i]

def get_current_year_str():
    current_year = get_current_year()

    for year in win.year_list:
        if year == current_year:
            return str(year)

def get_date_elem_total_value(elem):
    con = sqlite3.connect('sqlite.db')

    query_vars = (win.userID, )
    query = '''
        SELECT DateTimeStamp, Value FROM Expenses WHERE userID = ?; 
    '''

    results_list = dbase.execute_select_query(con, query, query_vars)

    dt = None
    total = 0
    for row in results_list:
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
        if dt.day == elem or dt.month == elem or dt.year == elem:
            total += row[1] # Add value of record to returned total IF date element matches record's
    
    return total