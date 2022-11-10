import sqlite3
from sqlite3 import Error
import sys
import app

def create_connection(dbpath):
    connection = None
    try:
        connection = sqlite3.connect(dbpath)
    except Error as e:
        print("Exception caught as {}".format(e))
    
    return connection

def execute_query(connection, query, vars):
    '''
    # check number of placeholders matches number of variables in query
    placeholder_count = 0
    i = 0
    c = query[i]
    while c != None:
        if c == '?':
            placeholder_count += 1
        i += 1
        c = query[i]
        print(c)
    print('placeholder_count: ' + placeholder_count)
    
    if placeholder_count != vars.len():
        print('Error: in sql query, placeholder number does not equal variable number')
        sys.exit(1)
    '''
    
    # execute query itself
    cursor = connection.cursor()
    try:
        cursor.execute(query, vars)
        connection.commit()
    except Error as e:
        print("Exception caught as {}".format(e))
    
    cursor.close()


def execute_select_query(connection, query):
    cursor = connection.cursor()
    select_result = []
    try:
        print("before execute")
        for row in cursor.execute(query):
            select_result.append(row)
        print("after execute")
        connection.commit()
       #select_result = cursor.fetchall()
    except Error as e:
        print("Exception caught as {}".format(e))
    
    cursor.close()
    
    return select_result

def add_home_input_spend(connection, event, values, userID):
    value = None
    query_vars = ()
    query = ''
    
    if event == 'addtodaysspend_but':
        value = values['addtodaysspend_input']
        query_vars = (value, app.current_datetime, userID, app.Type_dw['DAILY'].value)
        query = '''
            INSERT INTO Expenses(Value, DateTimeStamp, UserID, Type)
            VALUES (?, ?, ?, ?);
        ''' 
        execute_query(connection, query, query_vars) 
    elif event == 'addweeksspend_but':
        value = values['addweeksspend_input']
        query_vars =  (value, app.current_datetime, userID, app.Type_dw['WEEKLY'].value)
        query = '''
            INSERT INTO Expenses(Value, DateTimeStamp, UserID, Type)
            VALUES (?, ?, ?, ?);
        '''
        execute_query(connection, query, query_vars)