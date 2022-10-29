import PySimpleGUI as gui

def main():
    home_title = 'Home'
    
    gui.theme('DarkBlue12')

    home_layout = [ [gui.Titlebar(home_title)],
                [gui.Text('Expense Tracker')],
                [gui.Text('Add to Today\'s spending'), gui.Text('Add to this Week\'s spending')],
                [gui.InputText(), gui.InputText()],
                [] ]
    
    home_window = gui.Window(home_title, home_layout)

    while True:
        event, values = home_window.read()
        if event == gui.WINDOW_CLOSED:
            break
    
    home_window.close()

if __name__ == '__main__':
    main()