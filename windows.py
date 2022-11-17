import PySimpleGUI as gui
import mytime as t
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as mpl
from enum import Enum

# User currently logged in (will be better as an attribute of a User class)
userID = 1 # TODO: will need to have this map to whichever user is logged in at the time this is executed

default_theme_list = ['Dark', 'Blue', 12]
day_list = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
month_list = ['None', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_num_list = [n for n in range(1, 13)] 
year_list = [n for n in range(2000, 2030)] 
year_list.insert(0, 'None')

spending_history_table_data = []
spending_history_table = gui.Table(spending_history_table_data, ['Date & Time', 'Amount', 'D/W'], k="spending_history_table", 
                                        col_widths=[23, 7, 7], max_col_width=27, auto_size_columns=False, justification="centre")

home_day_tot_val = gui.Text('£{}'.format(str(t.get_date_elem_total_value(t.get_current_day()))), k='home_day_tot_val')
home_month_tot_val = gui.Text('£{}'.format(str(t.get_date_elem_total_value(t.get_current_month()))), k='home_month_tot_val')
home_year_tot_val = gui.Text('£{}'.format(str(t.get_date_elem_total_value(t.get_current_year()))), k='home_year_tot_val')

class Graph_type(Enum):
    WEEK_GRAPH = "week_graph"
    MONTH_GRAPH = "month_graph"
    YEAR_GRAPH = "year_graph"

def equate_dimensions_y(y_list, x_list):
    n = -100
    for i in range(len(x_list)):
        y_list.append(n + 100)
        n += 100

    return y_list

def create_home_graph_figure(option):
    x_axis, y_axis = None, None
    week_ylist, month_ylist, year_ylist = [], [], []
    weeksinmonths_list = None

    fig, ax = mpl.pyplot.subplots()
    
    # TODO: in ax, x and y axis must both have the same first dimension size
    if option == "week_graph":
        week_ylist = equate_dimensions_y(week_ylist, day_list)
        x_axis = np.array(day_list)
        y_axis = np.array(week_ylist)
        ax.set_xlabel('Day')
    elif option == "month_graph":
        weeksinmonths_list = ['W1', 'W2', 'W3', 'W4']
        month_ylist = equate_dimensions_y(month_ylist, weeksinmonths_list)
        x_axis = np.array(weeksinmonths_list)
        y_axis = np.array(month_ylist)
        ax.set_xlabel('Week')
    elif option == "year_graph":
        year_ylist = equate_dimensions_y(year_ylist, month_list)
        x_axis = np.array(month_list)
        y_axis = np.array(year_ylist)
        ax.set_xlabel('Month') 
    else:
        return "Graph error: option must be one of the Graph_type enum values"

    ax.plot(x_axis, y_axis)
    ax.set_ylabel('Amount')
    
    return fig


mpl.use("TkAgg")

def draw_figure(figure, canvas):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def gtp(left, right, top, bottom):
    return ((left, right), (top, bottom))


def make_home_window():    
    title = 'Home'
    layout = [ [gui.Text('Expense Tracker', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                [gui.Text('Add to Today\'s spending',  pad=((75,0), (10,10))), gui.Text('Add to this Week\'s spending', pad=((100,0), (10,10)))],
                [gui.InputText(k='addtodaysspend_input'), gui.InputText(k='addweeksspend_input')],
                [gui.Button('Submit', k='addtodaysspend_but'), gui.Button('Submit', k='addweeksspend_but')],
                [gui.Text('Today\'s spending'), gui.Text('{} spending'.format(t.get_current_month_str()))],
                [home_day_tot_val, home_month_tot_val],
                [gui.Canvas(k='home_week_graph'), gui.Canvas(k='home_month_graph')], 
                [gui.Text('{} spending'.format(t.get_current_year_str()))],
                [home_year_tot_val], 
                [gui.Canvas(k='home_year_graph')],
                [gui.Text('See a more detailed breakdown of your spending. Edit your spending.'), gui.Button('Open Spending', k='openspending_but')], 
                [gui.Text('Get insights into your spending habits.'), gui.Button('Open Insights', k='openinsights_but')], 
                [gui.Text('Customise your preferences and settings for this application.'),  gui.Button('Open Settings', k='opensettings_but')] ]
    
    return gui.Window(title, layout, finalize=True, location=(400,40))

def make_settings_window():
    title = 'Settings'
    layout = [ [gui.Text('Settings',  pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                        [gui.Text('Notifications', pad=gtp(0,0,15,0))],
                        [gui.HorizontalSeparator()],
                        [gui.Text('Daily Reminder'), gui.Combo(['On', 'Off'], 'On', k='set_dr_combo', enable_events=True)], 
                        [gui.Text('Weekly Reminder'), gui.Combo(['On', 'Off'], 'On', k='wr_combo', enable_events=True)],
                        [gui.Text('Appearance', pad=gtp(0,0,15,0))],
                        [gui.HorizontalSeparator()],
                        [gui.Text('Graph Type'), gui.Combo(['Line', 'Bar', 'Pie'], 'Line', k='set_graphtype_combo', enable_events=True)],
                        [gui.Text('Application Theme'), gui.Combo(['Dark', 'Light', 'Gray'], default_theme_list[0], k='set_themep1_combo', enable_events=True), 
                            gui.Combo(['Blue', 'Green', 'Black', 'Gray', 'Purple', 'Brown', 'Teal', 'Red'], default_theme_list[1], k='set_themep2_combo', enable_events=True), 
                            gui.Combo(['None', 'Gray', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], default_theme_list[2], k='set_themep3_combo', enable_events=True)] ]
    
    return gui.Window(title, layout, finalize=True, location=(15,400))

def make_spending_window():
    title = 'Spending'
    '''
        TODO: create a grid layout next to the table for elements used to edit spending history table records,
        which would have to communicate with the database first, to actually alter the underlying data before presenting
        it
    '''
    # sub_layout_one = [ [gui.Button('Edit', k='spending_edit_but')] ]
    main_layout = [ [gui.Text('Spending', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                [gui.Text('Spending History')],
                [gui.Combo(month_list, 'Select Month', s=10, k='spending_select_month_combo', enable_events=True),
                    gui.Combo(year_list, 'Select Year', s=10, k='spending_select_year_combo', enable_events=True)], 
                  [spending_history_table, gui.Button('Edit', k='spending_edit_but')] ]
    
    return gui.Window(title, main_layout, finalize=True, location=(15,80))

def make_insights_window():
    title = 'Insights'
    layout = [ [gui.Text('Insights', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                [gui.Text('Insight of the Day')],
                [gui.Text(s=(20,5))],
                [gui.Text('Comparisons')],
                [gui.HorizontalSeparator()],
                [gui.Combo(month_list, 'Select Month', s=10, k='spending_select_month_combo', enable_events=True),
                    gui.Combo(year_list, 'Select Year', s=10, k='spending_select_year_combo', enable_events=True),
                    gui.Combo(month_list, 'Select Month', s=10, k='spending_select_month_combo', enable_events=True),
                    gui.Combo(year_list, 'Select Year', s=10, k='spending_select_year_combo', enable_events=True)],
                [gui.Text('[+/-][value1]'), gui.Text('[+/-][value2]')] ]
    
    return gui.Window(title, layout, finalize=True, location=(800,80))