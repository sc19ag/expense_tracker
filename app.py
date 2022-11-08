import PySimpleGUI as gui
from windows import *

default_theme = 'DarkBlue12'

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