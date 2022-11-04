import PySimpleGUI as gui

def main():
    home_title = 'Home'
    
    gui.theme('DarkBlue12')
   

    home_layout = [ [gui.Titlebar(home_title)],
                [gui.Text('Expense Tracker')],
                [gui.Text('Add to Today\'s spending',  pad=((75,0), (10,10))), gui.Text('Add to this Week\'s spending', pad=((100,0), (10,10)))],
                [gui.InputText(), gui.InputText()],
                [gui.Text('Today\'s spending'), gui.Text('[Month]\'s spending')],
                [gui.Text('£[value1]'), gui.Text('£[value2]')],
                [gui.Graph((200,200), (0,0), (200,200)), gui.Graph((200,200), (0,0), (200,200))], 
                [] ]
    
    home_window = gui.Window(home_title, home_layout)

    while True:
        event, values = home_window.read()
        if event == gui.WINDOW_CLOSED:
            break
    
    home_window.close()

if __name__ == '__main__':
    main()