import PySimpleGUI as gui

def gtp(left, right, top, bottom):
    return ((left, right), (top, bottom))

def main():
    home_title = 'Home'
    settings_title = 'Settings'
    default_theme = 'DarkBlue12'
    default_theme_list = ['Dark', 'Blue', 12]
   
    gui.theme(default_theme)

    home_layout = [ [gui.Text('Expense Tracker', pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
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
    
    settings_layout = [ [gui.Text('Settings',  pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                        [gui.Text('Notifications', pad=gtp(0,0,15,0))],
                        [gui.Text('Daily Reminder'), gui.Combo(['On', 'Off'], 'On', k='dr_combo', enable_events=True)], 
                        [gui.Text('Weekly Reminder'), gui.Combo(['On', 'Off'], 'On', k='wr_combo', enable_events=True)],
                        [gui.Text('Appearance', pad=gtp(0,0,15,0))],
                        [gui.Text('Graph Type'), gui.Combo(['Line', 'Bar', 'Pie'], 'Line', k='graphtype_combo', enable_events=True)],
                        [gui.Text('Application Theme'), gui.Combo(['Dark', 'Light', 'Gray'], default_theme_list[0], k='themep1_combo', enable_events=True), 
                            gui.Combo(['Blue', 'Green', 'Black', 'Gray', 'Purple', 'Brown', 'Teal', 'Red'], default_theme_list[1], k='themep2_combo', enable_events=True), 
                            gui.Combo(['None', 'Gray', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], default_theme_list[2], k='themep3_combo', enable_events=True)] ]
    
    home_window = gui.Window(home_title, home_layout)
    settings_window = gui.Window(settings_title, settings_layout)

    settings_win_active = False
    while True:
        home_event, home_values = home_window.read()
        if home_event in (gui.WINDOW_CLOSED, 'Exit'):
            break

        if not settings_win_active and home_event == 'opensettings_but':
            settings_win_active = True
            while settings_win_active:
                settings_event, settings_values = settings_window.read()
                if settings_event in (gui.WINDOW_CLOSED, 'Exit'):
                    settings_win_active = False
                    settings_window.close()

    
    home_window.close()

if __name__ == '__main__':
    main()