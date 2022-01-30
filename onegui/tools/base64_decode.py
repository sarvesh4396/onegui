from base64 import b64decode

import PySimpleGUI as sg

from onegui.utils.components import get_window
from onegui.utils.utils import check_close


class Base64_decode:

    "Decodes base64"

    NAME = "Base64 Decoder"

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
            text = b64decode(base64)
            sg.popup(text, title="Decoded String")
            sg.clipboard_set(text)
            window.close()
            break
