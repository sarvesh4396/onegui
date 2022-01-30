from base64 import b64encode

import PySimpleGUI as sg

from onegui.utils.components import get_window
from onegui.utils.utils import check_close


class Base64_encode:
    "Encodes base64"
    NAME = "Base64 Encoder"

    def run(self):
        layout = [
            [sg.Text("Enter base64 "), sg.InputText()],
        ]
        window = get_window(self.NAME, layout)
        while True:
            event, values = window.read()
            if check_close(event):
                window.close()
                break
            base64 = values[0]
            text = b64encode(bytes(base64, "utf-8"))
            sg.popup(text, title="Encoded String")
            sg.clipboard_set(text)
            window.close()
            break
