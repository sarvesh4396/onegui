import PySimpleGUI as sg


def check_close(event):
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        return True
    return False
