import PySimpleGUI as sg

from onegui.utils.components import get_window

from .tools import tools
from .utils import check_close


def main():
    tool_layouts = []
    for tool in tools:
        tool_layout = [
            sg.Button(tool, button_color=("gray34", "springgreen4"), key=tool)
        ]
        tool_layouts.append(tool_layout),

    layout = [
        tool_layouts,
    ]
    # Create the Window
    window = get_window("OneGui", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if check_close(event):
            window.close()
            break
        _selected = tools.get(event, False)
        if _selected is not False:
            tools[event]().run()
