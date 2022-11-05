import PySimpleGUI as gui

default_theme = 'DarkBlue12'
default_theme_list = ['Dark', 'Blue', 12]

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
    
    return gui.Window(title, layout, finalize=True)

def make_settings_window():
    title = 'Settings'
    layout = [ [gui.Text('Settings',  pad=gtp(240,240,15,15), font='TimesNewRoman 21')],
                        [gui.Text('Notifications', pad=gtp(0,0,15,0))],
                        [gui.Text('Daily Reminder'), gui.Combo(['On', 'Off'], 'On', k='dr_combo', enable_events=True)], 
                        [gui.Text('Weekly Reminder'), gui.Combo(['On', 'Off'], 'On', k='wr_combo', enable_events=True)],
                        [gui.Text('Appearance', pad=gtp(0,0,15,0))],
                        [gui.Text('Graph Type'), gui.Combo(['Line', 'Bar', 'Pie'], 'Line', k='graphtype_combo', enable_events=True)],
                        [gui.Text('Application Theme'), gui.Combo(['Dark', 'Light', 'Gray'], default_theme_list[0], k='themep1_combo', enable_events=True), 
                            gui.Combo(['Blue', 'Green', 'Black', 'Gray', 'Purple', 'Brown', 'Teal', 'Red'], default_theme_list[1], k='themep2_combo', enable_events=True), 
                            gui.Combo(['None', 'Gray', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], default_theme_list[2], k='themep3_combo', enable_events=True)] ]
    
    return gui.Window(title, layout, finalize=True)

def main():
    gui.theme(default_theme)
    
    home_window = make_home_window()
    settings_window = None
    
    while True:
        window, event, values = gui.read_all_windows()
        if event in (gui.WINDOW_CLOSED, 'exit'):
            window.close()
            if window == home_window:
                break
            elif window == settings_window:
                settings_window = None
        elif event == 'opensettings_but' and not settings_window:
            settings_window = make_settings_window()
    
    home_window.close()        
                    

if __name__ == '__main__':
    main()