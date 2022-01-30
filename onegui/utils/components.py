import PySimpleGUI as sg


def get_window(title, layout=[]):
    common_layout = [sg.Button("Ok"), sg.Button("Cancel")]
    layout.append(common_layout)
    return sg.Window(title, layout)
