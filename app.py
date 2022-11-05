import PySimpleGUI as gui

default_theme = 'DarkBlue12'
default_theme_list = ['Dark', 'Blue', 12]
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year_list = [n for n in range(2000, 2050)] 

def gtp(left, right, top, bottom):
    return ((left, right), (top, bottom))

def make_home_window():
    title = 'Home'
    layout = [ [gui.Text('Expense Tracker', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                [gui.Text('Add to Today\'s spending',  pad=((75,0), (10,10))), gui.Text('Add to this Week\'s spending', pad=((100,0), (10,10)))],
                [gui.InputText(k='addtodaysspend_input', enable_events=True), gui.InputText(k='addweeksspend_input', enable_events=True)],
                [gui.Text('Today\'s spending'), gui.Text('[Month]\'s spending')],
                [gui.Text('£[value1]'), gui.Text('£[value2]')],
                [gui.Graph((200,200), (0,0), (200,200), background_color='red', k='weekspend_graph'), 
                    gui.Graph((200,200), (0,0), (200,200), background_color='green', k='monthspend_graph')], 
                [gui.Text('[Year\'s] spending')],
                [gui.Text('£[valueY]')], 
                [gui.Graph((200,200), (0,0), (200,200), background_color='yellow', k='yearspend_graph')],
                [gui.Text('See a more detailed breakdown of your spending. Edit your spending.'), gui.Button('Open Spending', k='openspending_but')], 
                [gui.Text('Get insights into your spending habits.'), gui.Button('Open Insights', k='openinsights_but')], 
                [gui.Text('Customise your preferences and settings for this application.'),  gui.Button('Open Settings', k='opensettings_but')] ]
    
    return gui.Window(title, layout, finalize=True, location=(400,50))

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
    spending_history_table_data = [ ['[Day]/[Month]/[Year]', '[Value1]', '[D|W]'],
                                    ['[Day]/[Month]/[Year]', '[Value2]', '[D|W]'] ]
    layout = [ [gui.Text('Spending', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                [gui.Text('Spending History'), gui.Button('Edit', k='spending_edit_but')],
                [gui.Combo(month_list, 'Select Month', s=10, k='spending_select_month_combo', enable_events=True),
                    gui.Combo(year_list, 'Select Year', s=10, k='spending_select_year_combo', enable_events=True)], 
                  [gui.Table(spending_history_table_data, ['Date', 'Amount', 'D/W'])] ]
    
    return gui.Window(title, layout, finalize=True, location=(15,80))

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

def main():
    gui.theme(default_theme)
    
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
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()