import PySimpleGUI as gui
import sqlite3
from windows import *
from database import *
from datetime import datetime

default_theme = 'DarkBlue12'

def main():
    gui.theme(default_theme)
    current_datetime = datetime.now()
    
    home_window = make_home_window()
    settings_window, spending_window, insights_window = None, None, None
    
    while True:
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
            settings_window = make_settings_window()
        elif event == 'openspending_but' and not spending_window:
            spending_window = make_spending_window()
        elif event == 'openinsights_but' and not insights_window:
            insights_window = make_insights_window()
        elif event == 'addtodaysspend_but':
            connection = create_connection("sqlite.db")
            value = values['addtodaysspend_input']
            date = current_datetime.date() # sqlite database is not compatible with this type 
            time = current_datetime.time() # convert these to a datetime object representing the current time
            userID = 0
            query_vars = (value, date, time, userID)
            query = '''
                INSERT INTO Expenses(Value, Date, Time, Type, UserID)
                VALUES (?, ?, ?, 'Daily', ?);
            ''' # Change query_vars and placeholders to have seperate date and time as only datetime. Expenses table is already changed.
            execute_query(connection, query, query_vars) 
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()