import PySimpleGUI as gui

def main():
    gui.theme('DarkAmber')

    layout = [ [gui.Text('Expense Tracker')],
                [gui.Text('Add to Today\'s spending'), gui.Text('Add to this Week\'s spending')],
                [gui.InputText(), gui.InputText()],
                [] ]
    
    window = gui.Window('Home', layout)

    while True:
        event, values = window.read()
        if event == gui.WINDOW_CLOSED:
            break
    
    window.close()

if __name__ == '__main__':
    main()