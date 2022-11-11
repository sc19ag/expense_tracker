from enum import Enum
import PySimpleGUI as gui
import sqlite3
import windows as win
from database import *
from datetime import datetime

default_theme = 'DarkBlue12'
current_datetime = datetime.now()

class Type_dw(Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"

def main():
    gui.theme(default_theme)
    
    home_window = win.make_home_window()
    settings_window, spending_window, insights_window = None, None, None

    connection = create_connection("sqlite.db")
    
    #loop = 0
    while True:
        #loop += 1
        userID = 1 # TODO: will need to have this map to whichever user is logged in at the time this is executed

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

        # insert user's input spent amounts into database    
        add_home_input_spend(connection, event, values, userID)
        
        # keep spending history table always correctly updated
        query_vars_sh = (userID, )
        query_sh = '''
            SELECT DateTimeStamp, Value, Type FROM Expenses WHERE userID = ? ORDER BY DateTimeStamp DESC;
        '''
        result_list = execute_select_query(connection, query_sh, query_vars_sh)
        win.spending_history_table.update(result_list)
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()