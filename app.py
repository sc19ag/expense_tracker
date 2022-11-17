from enum import Enum
import PySimpleGUI as gui
import windows as win
import database as dbase
from datetime import datetime
import mytime as t
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

default_theme = 'DarkBlue12'
current_datetime = datetime.now()

class Type_dw(Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"


def main():
    gui.theme(default_theme)
    
    home_window = win.make_home_window()
    home_window_open = True

    settings_window = win.make_settings_window()
    settings_window.hide()
    settings_window_open = False

    spending_window = win.make_spending_window()
    spending_window.hide()
    spending_window_open = False

    insights_window = win.make_insights_window()
    insights_window.hide()
    insights_window_open = False

    connection = dbase.create_connection("sqlite.db")
    
    #loop = 0
    while True:
        #loop += 1
        userID = win.userID

        window, event, values = gui.read_all_windows()
        if event in (gui.WINDOW_CLOSED, 'exit'):
            window.hide()
            if window == home_window:
                break
            elif window == settings_window:
                settings_window_open = False
            elif window == spending_window:
                spending_window_open = False
            elif window == insights_window:
                insights_window_open = False
        elif event == 'opensettings_but':
            settings_window.un_hide()
            settings_window_open = True
        elif event == 'openspending_but':
            spending_window.un_hide()
            spending_window_open = True
        elif event == 'openinsights_but':
            insights_window.un_hide()
            insights_window_open = True

        '''
            insert user's input spent amounts into database and, then, update 
            total value text for all date parts on home window  
        '''  
        dbase.add_home_input_spend(connection, event, values, userID)
        if event == 'addtodaysspend_but':
            win.home_day_tot_val.update('£{}'.format(str(t.get_date_elem_total_value(t.get_current_day()))))
            win.home_month_tot_val.update('£{}'.format(str(t.get_date_elem_total_value(t.get_current_month()))))
            win.home_year_tot_val.update('£{}'.format(str(t.get_date_elem_total_value(t.get_current_year()))))
        elif event == 'addweeksspend_but':
            win.home_month_tot_val.update('£{}'.format(str(t.get_date_elem_total_value(t.get_current_month()))))
            win.home_year_tot_val.update('£{}'.format(str(t.get_date_elem_total_value(t.get_current_year()))))
        
        if spending_window_open: 
            # TODO: something wrong with this set of control structures that needs to be fixed, in terms of what is displayed
            # in the spending history table
            if event == 'spending_select_month_combo' or event == 'spending_select_year_combo':
                if values['spending_select_month_combo'] != 'None' and values['spending_select_year_combo'] != 'None':
                # TODO: this can be simpified by using win.month_num_list instead of month_list
                    smc_month = None
                    for i in range(len(win.month_list) - 1):
                        if win.month_list[i] == 'None' or win.month_list[i] == 'none':
                            continue

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
            else:
                # keep spending history table always correctly updated
                query_vars_sh = (userID, )
                query_sh = '''
                    SELECT DateTimeStamp, Value, Type FROM Expenses WHERE userID = ? ORDER BY DateTimeStamp DESC;
                '''
                sh_result_list = dbase.execute_select_query(connection, query_sh, query_vars_sh)
                win.spending_history_table.update(sh_result_list)
        
        # always update graphs on the home window
        wg_fig = win.create_home_graph_figure(win.Graph_type['WEEK_GRAPH'].value)
        win.draw_figure(wg_fig, window['home_week_graph'].TKCanvas)

        mg_fig = win.create_home_graph_figure(win.Graph_type['MONTH_GRAPH'].value)
        win.draw_figure(mg_fig, window['home_month_graph'].TKCanvas)

        yg_fig = win.create_home_graph_figure(win.Graph_type['YEAR_GRAPH'].value)
        win.draw_figure(yg_fig, window['home_year_graph'].TKCanvas)    
       
    
    home_window.close() 
    settings_window.close()
    spending_window.close()
    insights_window.close()       
                    

if __name__ == '__main__':
    main()