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
        sh_result_list = execute_select_query(connection, query_sh, query_vars_sh)
        win.spending_history_table.update(sh_result_list)

        # TODO: Here i need to somehow convert the DateTimeStamp string values back into DateTime python objects, 
        # extract the month from these objects, check if it is the month selected in the combo box and only keep the 
        # records/rows from the original result set returned from execute_select_query that contain this month. I, then, 
        # need to store these kept records in a new, smaller results set and instead output this to the spending history
        # table.
        if event == 'spending_select_month_combo' or event == 'spending_select_year_combo':  
            smc_month = None
            for i in range(len(win.month_list) - 1):
                if values['spending_select_month_combo'] == win.month_list[i]:
                    smc_month = i + 1
                    break

            month_year_result_list = []
            dt = None
            for row in sh_result_list:
                dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
                if dt.month == smc_month and dt.year == values['spending_select_year_combo']:
                    month_year_result_list.append(row)

            win.spending_history_table.update(month_year_result_list)
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()