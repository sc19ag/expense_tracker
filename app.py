from enum import Enum
import PySimpleGUI as gui
import sqlite3
import windows as win
from database import *
from datetime import datetime

default_theme = 'DarkBlue12'

class Type_dw(Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"

def main():
    gui.theme(default_theme)
    current_datetime = datetime.now()
    
    home_window = win.make_home_window()
    settings_window, spending_window, insights_window = None, None, None

    connection = create_connection("sqlite.db")
    userID = 1 # TODO: will need to have this map to whichever user is logged in at the time this is executed
    query_vars = ()
    query = None
    
    loop = 0
    while True:
        loop += 1
        window, event, values = gui.read_all_windows()
        if event in (gui.WINDOW_CLOSED, 'exit'):
            window.close()
            if window == home_window:
                break
            elif window == settings_window:
                settings_window = None
            elif window == spending_window:
                spending_window = None
            elif window == insights_window:
                insights_window = None
        elif event == 'opensettings_but' and not settings_window:
            settings_window = win.make_settings_window()
        elif event == 'openspending_but' and not spending_window:
            spending_window = win.make_spending_window()
        elif event == 'openinsights_but' and not insights_window:
            insights_window = win.make_insights_window()
        elif event == 'addtodaysspend_but':
            value = values['addtodaysspend_input']
            userID_tsb = 1 # TODO: will need to have this map to whichever user is logged in at the time this is executed
            query_vars_tsb = (value, current_datetime, userID_tsb, Type_dw['DAILY'].value)
            query_tsb = '''
                INSERT INTO Expenses(Value, DateTimeStamp, UserID, Type)
                VALUES (?, ?, ?, ?);
            ''' 
            execute_query(connection, query_tsb, query_vars_tsb) 
        
        # keep spending history table always updated
        #userID_sht = 1 # TODO: will need to have this map to whichever user is logged in at the time this is executed 
        #query_vars_sht = (userID_sht)
        query_sht = '''
            SELECT DateTimeStamp, Value, Type FROM Expenses;
        '''
        #print('userID = {}, loop = {}'.format(userID_sht, loop))
        result_list = execute_select_query(connection, query_sht)
        win.spending_history_table.update(values=result_list)
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()